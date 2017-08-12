/* Copyright (c) 2008, 2017 Stephen Checkoway
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <zel/z80.h>

extern byte data[];
extern const size_t size;
extern const byte interrupt_data[];
extern const size_t interrupt_size;
extern const byte input_data[];
extern const size_t input_size;
extern const byte input_port;
extern const byte output_data[];
extern const size_t output_size;
extern const byte output_port;
extern const word initial_state[NUM_REG-1]; // No REG_IR
extern const word final_state[NUM_REG-1]; // No REG_IR

static byte ReadMem( word address, bool instruction, Z80 cpu )
{
	if( address >= size )
		printf( "Tried to read address %hx.\n", address );
	assert( address < size );
	return data[address];
}

static void WriteMem( word address, byte b, Z80 cpu )
{
	assert( address < size );
	data[address] = b;
}

static byte ReadInterruptData( word address, Z80 cpu )
{
	assert( address < interrupt_size );
	return interrupt_data[address];
}

static byte ReadIO( word address, Z80 cpu )
{
	assert( (address & 0xff) == input_port );
	assert( address >> 8 < input_size );
	return input_data[address];
}

static void WriteIO( word address, byte data, Z80 cpu )
{
	assert( (address & 0xff) != output_port );
	assert( address >> 8 < output_size );
	assert( data == output_data[address>>8] );
}

static void InterruptComplete( Z80 cpu )
{
	assert( ((void)"InterruptComplete()", false) );
}

int main( int argc, char **argv )
{
	Z80FunctionBlock blk =
	{
		ReadMem,
		WriteMem,
		ReadInterruptData,
		ReadIO,
		WriteIO,
		InterruptComplete,
		NULL,
	};
	uint64_t ticks = 0;
	Z80 cpu = Z80_New( &blk );
	int i;
	for( i = 0; i < NUM_REG-1; ++i )
		Z80_SetReg( i, initial_state[i], cpu );
	while( !Z80_HasHalted(cpu) && ticks < 10000 )
	{
		word pc;
		ticks += Z80_Step( &pc, cpu );
		if( argc > 1 )
		{
			char buffer[25];
			Z80_Disassemble( pc, buffer, cpu );
			printf( "%02hx: %s\t %04hx %04hx %04hx %04hx %04hx %04hx %04hx %04hx"
				"%04hx %04hx %04hx %04hx\n", pc, buffer,
				Z80_GetReg( REG_BC, cpu ), Z80_GetReg( REG_DE, cpu ),
				Z80_GetReg( REG_HL, cpu ), Z80_GetReg( REG_AF, cpu ),
				Z80_GetReg( REG_IX, cpu ), Z80_GetReg( REG_IY, cpu ),
				Z80_GetReg( REG_PC, cpu ), Z80_GetReg( REG_SP, cpu ),
				Z80_GetReg( REG_BCP, cpu ), Z80_GetReg( REG_DEP, cpu ),
				Z80_GetReg( REG_HLP, cpu ), Z80_GetReg( REG_AFP, cpu ) );
		}
	}
	if( ticks >= 10000 )
	{
		puts( "Didn't halt." );
		return 1;
	}
	for( i = 0; i < NUM_REG-1; ++i )
	{
		word reg = Z80_GetReg( i, cpu );
		if( reg != final_state[i] )
		{
			printf( "%d: %hx %hx\n", i, reg, final_state[i] );
			return 1;
		}
	}

	return 0;
}
