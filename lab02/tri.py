#!/usr/bin/python
# vim: set fileencoding=UTF-8
a = int(input("? "))
b = int(input("? "))
c = int(input("? "))
if a < 1 or b < 1 or c < 1 :
  print("As dimensões dos lados do triângulo devem ser todas positivas")
else:
  if a + b <= c or a + c <= b or c + b <= a :
    print("Não é triângulo")
  else:
    if a == b and b == c :
      print("O triângulo é equilátero")
    else:
      if a == b or b == c or c == a :
        print("O triângulo é isósceles")
      else:
        print("O triângulo é escaleno")
