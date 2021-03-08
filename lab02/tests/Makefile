# Copyright (C) 2021, Pedro Reis dos Santos
.SUFFIXES: .in .out .diff
MAKEFLAGS += --no-print-directory # No entering and leaving messages
OK="\e[1;32mtest $< PASSED\e[0m"
KO="\e[1;31mtest $< FAILED\e[0m"
CC=gcc
CFLAGS=-g -Wall -Wextra -Werror -ansi -pedantic
ALL=ex01 ex02 ex03 ex04 ex05 ex06 ex07 ex08 ex09 ex10 ex11 ex12 ex13 ex14 ex15
ex01=0 1 2 3 4 5 6
ex02=0 1 2
ex03=0 1 2 3
ex04=0 1 2
ex05=0 1 2 3
ex06=0 1 2
ex07=0 1 2
ex08=0 1 2 3
ex09=0 1 2 3 4
ex10=0 1 2 3
ex11=0 1 2 3
ex12=0 1 2 3
ex13=0 1 2 3
ex14=0 1 2 3
ex15=0 1 2 3

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
