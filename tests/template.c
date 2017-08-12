/* Written by Stephen Checkoway, 2008, 2017. Released into the public domain. */
#include <stdlib.h>
#include <z80.h>

#include "z80_types.h"

byte data[] = {};
const byte interrupt_data [] = {};
const byte input_data[] = {};
const byte input_port = 0;
const byte output_data[] = {};
const byte output_port = 0;
const word initial_state[NUM_REG] = { 0x0000, 0x0000, 0x0000, 0x0000,   // BC, DE, HL, AF
				      0x0000, 0x0000, 0x0000, 0x0000,   // IX, IY, PC, SP
				      0x0000, 0x0000, 0x0000, 0x0000 }; // BC', DE', HL', AF'

const word final_state[NUM_REG] =   { 0x0000, 0x0000, 0x0000, 0x0000,   // BC, DE, HL, AF
				      0x0000, 0x0000, sizeof(data),  0x0000,   // IX, IY, PC, SP
				      0x0000, 0x0000, 0x0000, 0x0000 }; // BC', DE', HL', AF'
const size_t size = sizeof(data);
const size_t interrupt_size = sizeof(interrupt_data);
const size_t input_size = sizeof(input_data);
const size_t output_size = sizeof(output_data);
