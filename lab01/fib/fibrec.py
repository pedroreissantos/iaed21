import sys

def fib(n):
  if n < 2:
    return n
  return fib(n-2) + fib(n-1)

n=42
if len(sys.argv) > 1:
  n=int(sys.argv[1])
print (fib(n))
