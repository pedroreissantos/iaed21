CC=gcc
CFLAGS=-O3 -fomit-frame-pointer -s
all: fibiter fibrec fiblong

fib12:: all
	time python fibiter.py 12
	time python fibrec.py 12
	time ./fibiter 12
	time ./fibrec 12

clean::
	rm -f fibiter fibrec fiblong
