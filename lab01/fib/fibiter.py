import sys

def fib(n):
  a,b = 0,1
  while n > 1:
    a,b,n = b,a+b,n-1
  return b

n=42
if len(sys.argv) > 1:
  n=int(sys.argv[1])
print (fib(n))
