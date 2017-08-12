/* Written by Stephen Checkoway, 2008, 2017. Released into the public domain. */
#include <stdlib.h>
#include <zel/z80.h>

const char *disasm[] = {
	"ld a,15h",
	"ld b,a",
	"ld c,(hl)",
	"ld d,(ix+02h)",
	"ld iyl,03h",
	"ld e,(iy-01h)",
	"ld a,(hl)",
	"ld ixh,a",
	"ld a,(0007h)",
	"halt",
	NULL,
};
byte data[] = { 0x3e, 0x15, 0x47, 0x4e, 0xdd, 0x56, 0x02, 0xfd, 0x2e, 0x03, 0xfd, 0x5e, 0xff, 
		0x7e, 0xdd, 0x67, 0x3a, 0x07, 0x00, 0x76 };
const byte interrupt_data [] = {};
const byte input_data[] = {};
const byte input_port = 0;
const byte output_data[] = {};
const byte output_port = 0;
const word initial_state[NUM_REG] = { 0x0000, 0x0000, 0x0000, 0x0000,   // BC, DE, HL, AF
				      0x0000, 0x0000, 0x0000, 0x0000,   // IX, IY, PC, SP
				      0x0000, 0x0000, 0x0000, 0x0000 }; // BC', DE', HL', AF'

const word final_state[NUM_REG] =   { 0x153e, 0x4747, 0x0000, 0xfd00,   // BC, DE, HL, AF
				      0x3e00, 0x0003, sizeof(data), 0x0000,   // IX, IY, PC, SP
				      0x0000, 0x0000, 0x0000, 0x0000 }; // BC', DE', HL', AF'
const size_t size = sizeof(data);
const size_t interrupt_size = sizeof(interrupt_data);
const size_t input_size = sizeof(input_data);
const size_t output_size = sizeof(output_data);
