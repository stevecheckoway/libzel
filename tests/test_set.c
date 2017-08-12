/* Written by Stephen Checkoway, 2008, 2017. Released into the public domain. */
#include <stdlib.h>
#include <zel/z80.h>

#include "z80_types.h"

const char *disasm[] = {
	"ld ix,0020h",
	"set 0,(ix-10h)",
	"set 4,(ix-10h)",
	"ld b,(ix-10h)",
	"halt",
	NULL,
};
byte data[] = { 0xdd, 0x21, 0x20, 0x00, // ld ix 0020h
		0xdd, 0xcb, 0xf0, 0xc6, // set 0,(ix-10h)
		0xdd, 0xcb, 0xf0, 0xe6, // set 4,(ix-10h)
		0xdd, 0x46, 0xf0, 0x76, // ld b,(ix-10h); halt
		0x00 };			// byte 0x0010
const byte interrupt_data [] = {};
const byte input_data[] = {};
const byte input_port = 0;
const byte output_data[] = {};
const byte output_port = 0;
const word initial_state[NUM_REG] = { 0x0000, 0x0000, 0x0000, 0x0000,   // BC, DE, HL, AF
				      0x0000, 0x0000, 0x0000, 0x0000,   // IX, IY, PC, SP
				      0x0000, 0x0000, 0x0000, 0x0000 }; // BC', DE', HL', AF'

const word final_state[NUM_REG] =   { 0x1100, 0x0000, 0x0000, 0x0000,   // BC, DE, HL, AF
				      0x0020, 0x0000, 0x0010, 0x0000,   // IX, IY, PC, SP
				      0x0000, 0x0000, 0x0000, 0x0000 }; // BC', DE', HL', AF'
const size_t size = sizeof(data);
const size_t interrupt_size = sizeof(interrupt_data);
const size_t input_size = sizeof(input_data);
const size_t output_size = sizeof(output_data);
