#!/usr/bin/python
# vim: set fileencoding=UTF-8
a = int(input("? "))
b = int(input("? "))
if a <= 0 or b <= 0 :
  print("Os números devem ser inteiros positivos")
else:
  m,d,i = a,1,2
  if a > b :
    m = b
  while i <= m :
    if a % i == 0 and b % i == 0 :
      d = i
    i = i + 1
  print(d, "é o maior divisor comum entre", a, "e", b)
