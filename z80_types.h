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

/*! \file
 *
 * Types used by the z80.
 * \author Stephen Checkoway
 * \version 0.1
 * \date 2008
 */
#ifndef ZEL_Z80_TYPES_H
#define ZEL_Z80_TYPES_H

#ifdef __cplusplus
extern "C" {
#endif

/*! A single byte. */
typedef uint8_t byte;
/*! A signed byte used for displacement. */
typedef int8_t sbyte;
/*! A 16 bit z80 word. */
typedef uint16_t word;

#ifdef __cplusplus
}
#endif
#endif
