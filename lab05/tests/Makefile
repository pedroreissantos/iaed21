# Copyright (C) 2021, Pedro Reis dos Santos
.SUFFIXES: .in .out .diff
MAKEFLAGS += --no-print-directory # No entering and leaving messages
OK="\e[1;32mtest $< PASSED\e[0m"
KO="\e[1;31mtest $< FAILED\e[0m"
CC=gcc
CFLAGS=-g -Wall -Wextra -Werror -ansi -pedantic
ALL=ex01 ex02 ex03 ex04
ex01=0 1 2 3
ex02=0 1 2
ex03=0 1
ex04=0 1 2 3 4 5 6 7 8 9 10

all:: clean # run regression tests
	@for i in $(ALL); do $(MAKE) $(MFLAGS) $$i; done

%: ../%.c
	$(LINK.c) -o $@ $<
	@rm -f $*_*.diff
	@for i in $($@:%=$@_%.diff); do $(MAKE) $(MFLAGS) EXE=./$@ $$i; done

.in.diff:
	@-$(EXE) < $< | diff - $*.out > $@
	@if [ `wc -l < $@` -eq 0 ]; then echo $(OK); else echo $(KO); fi;

clean::
	rm -f *.diff ex??
