/* Copyright (c) 2008 Steve Checkoway
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
#include <string.h>
#include <zel/z80_instructions.h>

extern const char *disasm[];
extern byte data[];

static byte ReadMem( word address, void *unused )
{
	return data[address];
}

int main()
{
	int i;
	word address = 0;
	char buffer[25];
	bool failed = false;

	for( i = 0; disasm[i]; ++i )
	{
		Instruction inst;
		address += IF_ID( &inst, address, ReadMem, NULL );
		DisassembleInstruction( &inst, buffer );
		if( strcmp(disasm[i], buffer) )
		{
			printf( "Expected \"%s\" got \"%s\"\n", disasm[i], buffer );
			failed = true;
		}
	}
	return failed;
}
