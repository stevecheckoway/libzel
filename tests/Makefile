# Copyright (c) 2008 Steve Checkoway
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

sources = $(wildcard test_*.c)
tests = $(sources:.c=)
itests = $(subst test,itest,$(tests))

CPPFLAGS += -I../include
CFLAGS += -O3 -Wall -Werror
LDFLAGS += -L..
LIBS += -lzel

.PHONY: all check clean force

all:
force:
check: $(itests) $(tests)
	@passed=0; \
	total=0; \
	for i in $^; do \
		total=`expr $$total + 1`; \
		if ./$$i; then \
			echo PASS: $$i; \
			passed=`expr $$passed + 1`; \
		else \
			echo FAIL: $$i; \
		fi; \
	done; \
	echo $$passed of $$total tests passed

test_%: test_%.o test.o force
	$(CC) $(LDFLAGS) -o $@ $< test.o $(LIBS)
itest_%: test_%.o itest.o force
	$(CC) $(LDFLAGS) -o $@ $< itest.o $(LIBS)

test.o: test.c
itest.o: itest.c

clean:
	$(RM) $(sources:.c=.o) $(itests) $(tests) itest.o test.o
