#!/usr/bin/python
# vim: set fileencoding=UTF-8
# The following function will print a non-negative number, n, to
# the base b, where 2<=b<=10,  This routine uses the fact that
# in the ASCII character set, the digits O to 9 have sequential
# code values.
def printn(n, b) :
  a = int(n // b)
  if a != 0 :
    printn(a, b)
  print(str(n % b), end="")
n = int(input("? "))
b = int(input("? "))
printn(n, b)
print("")
