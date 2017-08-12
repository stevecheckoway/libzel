#!/usr/bin/perl
# Copyright (c) 2008, 2017 Stephen Checkoway
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
use strict;
use warnings;

sub parse_arg($)
{
	my $arg = shift;
	if( $arg =~ /^[ABCDEFHLIR]$/ or $arg =~ /^I[XY][HL]/)
	{
		return ( '_R', "REG_$arg", '', "\L$arg" );
	}
	if( $arg eq "AF'" )
	{
		return ( '_RR', 'REG_AFP', '', "\L$arg" );
	}
	if( $arg =~ /^(?:AF|BC|DE|HL|SP|IX|IY)$/ )
	{
		return ( '_RR', "REG_$arg", '', "\L$arg" );
	}
	if( $arg eq 'n' )
	{
		return ( '_N', 'INV', '_IMM_N', '%02hhXh' );
	}
	if( $arg eq 'nn' )
	{
		return ( '_NN', 'INV', '_IMM_NN', '%04hXh' );
	}
	if( $arg =~ /^\((BC|DE|HL|SP|IX|IY)\)$/ )
	{
		return ( '_MRR', "REG_$1", '', "\L$arg" );
	}
	if( $arg eq '(C)' )
	{
		return ( '_R', 'REG_C', '', '(c)' );
	}
	if( $arg eq '(n)' )
	{
		return ( '_MN', 'INV', '_IMM_N', '(%02hhXh)' );
	}
	if( $arg eq '(nn)' )
	{
		return ( '_MNN', 'INV', '_IMM_NN', '(%04hXh)' );
	}
	# Make c lowercae here so it doesn't match above.
	if( $arg =~ /^(?:NZ|Z|NC|c|PE|PO|P|M)$/ )
	{
		return ( '_C', "COND_\u$arg", '', "\L$arg" );
	}
	if( $arg eq '(IX+d)' )
	{
		return ( '_I', 'REG_IX', '_OFFSET', '(ix%c%02Xh)' );
	}
	if( $arg eq '(IY+d)' )
	{
		return ( '_I', 'REG_IY', '_OFFSET', '(iy%c%02Xh)' );
	}
	if( $arg eq '(PC+e)' )
	{
		return ( '', 'INV', '_DISP', '(pc%c%Xh)' );
	}
	if( $arg =~ /^([123]?[08])H$/ )
	{
		return ( '', "0x$1", '', "$1h" );
	}
	if( $arg =~ /^[0-7]$/ )
	{
		return ( '', $arg, '', $arg );
	}
	die $arg;
}

my $previous = -1;
while( <> )
{
	my @part = split /\t+/;
	$part[0] =~ /^[DF]DCB d ([0-9A-F]{2})/ or
		$part[0] =~ /^(?:CB|DD|ED|FD)?([0-9A-F]{2})(?: |$)/
		or die 'bad opcode';
	my $op = hex $1;
	while( ++$previous < $op )
	{
		printf "{ NOP, INV, INV, INV, 8, TYPE_NONE, \"nop\" },\t// %02x\n",
			$previous;
	}
	$previous = $op;
	$part[2] =~ /^(\d+)(?:\/(\d+))?$/ or die $part[2];
	my $tstate = $1;
	my $extra = 'INV';
	if( defined $2 )
	{
		$extra = $2;
		($tstate,$extra) = ($extra,$tstate) if $tstate < $extra;
	}
	my $mnemonic = '';
	if( $part[1] =~
	    /LD ([BCDEHLAF]),((?:RLC|RRC|RL|RR|SLA|SRA|SLL|SRL|BIT|RES|SET).*)/ )
	{
		$extra = "REG_$1";
		$mnemonic = "LD $1,";
		$part[1] = $2;
	}
	@part = split / /, $part[1];
	my $type = $part[0];
	$mnemonic = "\L$mnemonic$type";

	print '{ ';
	if( $#part == 1 )
	{
		my @args = split /,/, $part[1];
		my ($suffix, $operand, $op_type, $fmt) = parse_arg $args[0];
		if( $#args == 0 )
		{
			$op_type = '_NONE' unless $op_type ne '';
			print "$type$suffix, $operand, INV, ",
			      "$extra, $tstate, TYPE$op_type, \"$mnemonic $fmt\"";
		}
		else
		{
			my ($suffix2, $operand2, $op_type2, $fmt2) = parse_arg $args[1];
			$op_type = '_NONE' unless $op_type ne '' or $op_type2 ne '';
			print "$type$suffix$suffix2, $operand, $operand2, ",
			      "$extra, $tstate, TYPE$op_type$op_type2, ",
			      qq{"$mnemonic $fmt,$fmt2"};
		}
	}
	else
	{
		print qq/$type, INV, INV, $extra, $tstate, TYPE_NONE, "$mnemonic"/;
	}
	printf " },\t// %02x\n", $op;
}
while( ++$previous <= 0xff )
{
	printf "{ NOP, INV, INV, INV, 8, TYPE_NONE, \"nop\" },\t// %02x\n", $previous;
}
