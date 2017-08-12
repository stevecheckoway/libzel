/* Written by Steve Checkoway, 2008. Released into the public domain. */
#include <stdlib.h>
#include <zel/z80.h>

const char *disasm[] = {
	"add a,b",
	"sub c",
	"adc a,d",
	"sbc a,e",
	"and h",
	"or l",
	"xor FFh",
	"halt",
	NULL,
};
byte data[] = { 0x80, 0x91, 0x8a, 0x9b, 0xa4, 0xb5, 0xee, 0xff, 0x76 };
const byte interrupt_data [] = {};
const byte input_data[] = {};
const byte input_port = 0;
const byte output_data[] = {};
const byte output_port = 0;
const word initial_state[NUM_REG] = { 0x35ff, 0x0005, 0x0f50, 0x1200,   // BC, DE, HL, AF
				      0x0000, 0x0000, 0x0000, 0x0000,   // IX, IY, PC, SP
				      0x0000, 0x0000, 0x0000, 0x0000 }; // BC', DE', HL', AF'

const word final_state[NUM_REG] =   { 0x35ff, 0x0005, 0x0f50, 0xaba8,   // BC, DE, HL, AF
				      0x0000, 0x0000, sizeof(data), 0x0000,   // IX, IY, PC, SP
				      0x0000, 0x0000, 0x0000, 0x0000 }; // BC', DE', HL', AF'
const size_t size = sizeof(data);
const size_t interrupt_size = sizeof(interrupt_data);
const size_t input_size = sizeof(input_data);
const size_t output_size = sizeof(output_data);
