CC=gcc
CFLAGS= -g -O2 -Wall -Wextra -Werror -pedantic -ansi

OBJECTS1= main.o recurs.o
OBJECTS2= main.o iter.o

all: factorial-recurs factorial-iter

factorial-recurs : $(OBJECTS1)
	$(LINK.c) -o $@ $(OBJECTS1)

factorial-iter : $(OBJECTS2)
	$(LINK.c) -o $@ $(OBJECTS2)

main.o: main.c fact.h
iter.o: iter.c fact.h
recurs.o: recurs.c fact.h

clean::
	rm -f factorial-recurs factorial-iter *.o
run::
	./factorial-iter
