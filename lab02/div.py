#!/usr/bin/python
# vim: set fileencoding=UTF-8
d = 0
n = int(input("? "))
if n > 0 :
  i = 2
  while i <= n // 2 :
    if n % i == 0 :
      print(n, 'é divisível por', i)
      d = d + 1
    i = i + 1
  if d == 0 :
    print(n, 'é primo.')
