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

CPPFLAGS += -Iinclude
CFLAGS += -O3

package := zel
version := 0.1
distname := lib$(package)-$(version)

prefix		:= /usr/local
exec_prefix	:= $(prefix)
includedir	:= $(prefix)/include
datarootdir	:= $(prefix)/share
datadir		:= $(datarootdir)
docdir		:= $(datarootdir)/doc/$(package)
htmldir		:= $(docdir)
pdfdir		:= $(docdir)
libdir		:= $(exec_prefix)/lib
mandir		:= $(datarootdir)/man
man3dir		:= $(mandir)/man3

INSTALL		:= install
INSTALL_PROGRAM	:= $(INSTALL) -m 0755
INSTALL_DATA	:= $(INSTALL) -m 0644

spec	:= $(wildcard tables/*.spec)
itables := $(spec:.spec=.tab)

here	:= $(shell pwd)

dist_source := z80.c \
	       z80_instructions.c \
	       include/zel/z80.h \
	       include/zel/z80_instructions.h \
	       include/zel/z80_types.h \
	       include/zel/z80_instruction_types.h \
	       tables/gen.pl \
	       $(spec) \
	       $(itables) \
	       Makefile \
	       Doxyfile \
	       LICENSE \
	       tests/Makefile \
	       $(wildcard tests/*.c) \
	       doc/$(distname).pdf

.PHONY: all check clean distclean mostlyclean maintainer-clean dist distcheck doc-clean \
	install install-html install-pdf html pdf uninstall uninstall-doc install-doc installcheck

all: libzel.a

libzel.a: z80.o z80_instructions.o
	$(AR) -cr $@ $?
	ranlib $@

tables/%.tab: tables/%.spec tables/gen.pl
	perl tables/gen.pl $< > $@

include/zel/z80_instruction_types.h: $(itables)
	sed -e '1s,^,/* ,;2,$$s,^, * ,' LICENSE >$@
	echo ' */' >>$@
	echo >>$@
	echo '/*! \\file' >>$@
	echo ' *' >>$@
	echo ' * z80 instruction types.' >>$@
	echo ' * \\author Stephen Checkoway' >>$@
	echo ' * \\version 0.1' >>$@
	echo ' * \\date 2008, 2017' >>$@
	echo ' */' >>$@
	echo '#ifndef ZEL_Z80_INSTRUCTION_TYPES_H' >>$@
	echo '#define ZEL_Z80_INSTRUCTION_TYPES_H' >>$@
	echo >>$@
	echo '#ifdef __cplusplus' >>$@
	echo 'extern "C" {' >>$@
	echo '#endif' >>$@
	echo >>$@
	echo 'typedef enum' >>$@
	echo '{' >>$@
	awk '{ split($$2,a,/_/); sub(/,/,"",a[1]); printf "\t%s //!< %s\n", $$2, tolower(a[1]) }' \
		$(itables) |sort|uniq >>$@
	echo '} InstructionType;' >>$@
	echo >>$@
	echo '#ifdef __cplusplus' >>$@
	echo '}' >>$@
	echo '#endif' >>$@
	echo >>$@
	echo '#endif' >>$@

z80.o: z80.c include/zel/z80.h include/zel/z80_instructions.h include/zel/z80_types.h include/zel/z80_instruction_types.h
z80_instructions.o: z80_instructions.c include/zel/z80_instructions.h include/zel/z80.h include/zel/z80_types.h include/zel/z80_instruction_types.h $(itables)

check: all
	$(MAKE) -C tests check

installcheck:
	$(MAKE) -C tests LDFLAGS='-L$(DESTDIR)$(libdir)' CPPFLAGS='-I$(DESTDIR)$(includedir)' check

doc-clean:
	$(RM) -r doc

clean: doc-clean
	$(MAKE) -C tests clean
	$(RM) libzel.a z80.o z80_instructions.o *~

doc: Doxyfile $(wildcard include/zel/*.h) include/zel/z80_instruction_types.h
	doxygen

pdf: doc/$(distname).pdf

doc/$(distname).pdf: doc
	$(MAKE) -C doc/latex -j1
	cp doc/latex/refman.pdf doc/$(distname).pdf

html: doc

man: doc

# XXX: Install the man pages once those get sorted out
install:
	$(INSTALL) -d $(DESTDIR)$(libdir)
	$(INSTALL_PROGRAM) libzel.a $(DESTDIR)$(libdir)
	$(INSTALL) -d $(DESTDIR)$(includedir)/zel
	$(INSTALL_DATA) include/zel/z80.h $(DESTDIR)$(includedir)/zel
	$(INSTALL_DATA) include/zel/z80_instructions.h $(DESTDIR)$(includedir)/zel
	$(INSTALL_DATA) include/zel/z80_types.h $(DESTDIR)$(includedir)/zel
	$(INSTALL_DATA) include/zel/z80_instruction_types.h $(DESTDIR)$(includedir)/zel

uninstall: uninstall-doc
	$(RM) $(DESTDIR)$(libdir)/libzel.a
	$(RM) $(DESTDIR)$(includedir)/zel/z80.h
	$(RM) $(DESTDIR)$(includedir)/zel/z80_instructions.h
	$(RM) $(DESTDIR)$(includedir)/zel/z80_types.h
	$(RM) $(DESTDIR)$(includedir)/zel/z80_instruction_types.h
	rmdir $(DESTDIR)$(includedir)/zel

install-doc: install-html install-pdf

uninstall-doc:
	$(RM) -r $(DESTDIR)$(htmldir)/html
	$(RM) $(DESTDIR)$(pdfdir)/$(distname).pdf
	rmdir $(DESTDIR)$(htmldir)
	if [ x$(DESTDIR)$(htmldir) != x$(DESTDIR)$(pdfdir) ]; then \
		rmdir $(DESTDIR)$(pdfdir); \
	fi

install-html:
	$(INSTALL) -d $(DESTDIR)$(htmldir)/html
	$(INSTALL_DATA) doc/html/* $(DESTDIR)$(htmldir)/html

install-pdf:
	$(INSTALL) -d $(DESTDIR)$(pdfdir)
	$(INSTALL_DATA) doc/$(distname).pdf $(DESTDIR)$(pdfdir)

dist: $(distname).tar.gz

$(distname).tar.gz: $(dist_source)
	mkdir $(distname)
	for i in $(dist_source); do \
		d=`dirname $$i`; \
		mkdir -p $(distname)/$$d; \
		cp $$i $(distname)/$$i; \
	done
	cp -r doc/html $(distname)/doc
	cp -r doc/man $(distname)/doc
	tar zcf $(distname).tar.gz $(distname)
	$(RM) -r $(distname)

distcheck: $(distname).tar.gz
	tar zxf $(distname).tar.gz
	$(MAKE) -C $(distname) prefix=$(here)/$(distname)/_inst check
	$(MAKE) -C $(distname) prefix=$(here)/$(distname)/_inst doc
	$(MAKE) -C $(distname) prefix=$(here)/$(distname)/_inst install
	$(MAKE) -C $(distname) prefix=$(here)/$(distname)/_inst install-doc
	$(MAKE) -C $(distname) prefix=$(here)/$(distname)/_inst installcheck
	$(MAKE) -C $(distname) prefix=$(here)/$(distname)/_inst uninstall
	$(RM) -r $(distname)

distclean: clean
mostlyclean: clean
maintainer-clean: clean
	$(RM) include/zel/z80_instruction_types.h $(itables)
