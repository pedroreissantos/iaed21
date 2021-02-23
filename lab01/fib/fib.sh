#! /bin/sh
fib() {
	local n_1 n_2 fib_1
#	echo "FIB($1)"
	if [ $1 -lt 2 ]; then return $1; fi
	n_1=`expr $1 - 1`
	fib $n_1
	fib_1=$?
	n_2=`expr $1 - 2`
	fib $n_2
	return `expr $fib_1 + $?`
}

n=2
if [ $# -eq 1 ]; then n=$1; fi
fib $n
echo "fib($n)=$?"
