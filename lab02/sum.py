#!/usr/bin/python
# vim: set fileencoding=UTF-8
sum = 0
a = input("? ")
while a.lstrip('-').isdigit() :
  sum = sum + int(a)
  a = input("? ")
print(sum)
# end with a non-integer value: 1. (for example)
