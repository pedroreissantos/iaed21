## Nota prévia:
para testar os seus programas pode usar as sequências disponibilizadas na directoria de `tests/`. Os ficheiros `.in` contêm as sequências de entrada e os respetivos ficheiros `.out` a saída esperada para um programa correto.
O processo pode ser automatizado com recurso à `Makefile` aí existente, para tal os programas devem ter o nome do exercício (`ex01.c` para o primeiro exercício).
O comando `make -C tests ex01` compila e executa os testes disponíveis para o exercício `ex01`.
Para testar todos os exercícios basta executar `make -C tests` (ou apenas `make` se estiver na diretoria `tests/`). Os ficheiros __C__ devem ser desenvolvidos no diretório do laboratório (não na diretoria de `tests/`).
---

# Converta de python para C

Considere o programa em **python** que soma 12 ([duzia.py](duzia.py)) ao valor lido do terminal:
```
n = int(input("? "))
print(12 + n)
```
e o equivalente programa em **C** ([duzia.c](duzia.c))
```
#include <stdio.h>
int main() {
    int n;
    printf("? ");
    scanf("%d", &n);
    printf("%d\n", 12 + n);
    return 0;
}
```
onde `scanf("%d", &n);` é a função de leitura de um inteiro decimal (que devolve o número de parâmetros lidos) e `printf("%d\n", n);` é a função escrita de um inteiro decimal (que devolve o número de carateres impressos no terminal).

Pretende-se converter para **C** os exemplos seguintes:

## ex01
Classificador de triângulos: ([tri.py](tri.py))
```
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
```

## ex02
Divisores de um número: ([div.py](div.py))
```
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
```

## ex03
Maior divisor comum: ([gcd.py](gcd.py))
```
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
```

## ex04
Somatório de inteiros: ([sum.py](sum.py))
```
    sum = 0
    a = input("? ")
    while a.lstrip('-').isdigit() :
        sum = sum + int(a)
        a = input("? ")
    print(sum)
```

## ex05
Impressão de inteiro em base dada: ([printn.py](printn.py))
```
    def printn(n, b) :
        a = int(n // b)
        if a != 0 :
            printn(a, b)
        print(str(n % b), end="")
    n = int(input("? "))
    b = int(input("? "))
    printn(n, b)
    print("")
```

# Codifique directamente em C
## ex06

(Maior de Três) Escreva um programa que determine e imprima o maior de três números inteiros dados pelo utilizador.

## ex07

(Maior e Menor) Escreva um programa que determine o maior e o menor número de `N` números reais dados pelo utilizador. Considere que `N` é um valor pedido ao utilizador.

O resultado deve ser impresso com o comando `printf("min: %f, max: %f\n", min, max)`.

*Sugestão:* inicialize o maior e o menor com o primeiro valor lido.

## ex08

(Divisores) Escreva um programa que pede ao utilizador um inteiro positivo `N` e imprima o número de divisores de `N`. Recorde que os números primos têm 2 divisores.

## ex09

(Média) Escreva um programa que calcule e imprima a média de `N` números reais dados pelo
utilizador.  O programa deverá primeiro pedir ao utilizador um inteiro `N`, representando
a quantidade de números que vão ser introduzidos. Os números reais devem ser representados
pelo tipo `float`. O resultado deve ser impresso com o comando `printf("%.2f\n", media);`.

## ex10

(Conversão) Escreva um programa que pede ao utilizador um valor `N` correspondente a um certo período de tempo em segundos. O programa deverá apresentar no output esse período de tempo no formato `HH:MM:SS`.

*Sugestão:* utilize o operador que calcula o resto da divisão (`%`).

## ex11

(Dígitos) Escreva um programa que pede ao utilizador um valor positivo `N`. No output, deverá mostrar o número de dígitos que compõem `N` (na primeira linha), assim como a soma dos dígitos de `N` (na segunda linha). Por exemplo, o número 12345 tem 5 dígitos e a soma desses dígitos é 15.

## ex12

(Ordena 2) Escreva um programa que leia dois inteiros `N, M` e imprima o menor deles
na primeira linha e o maior na segunda.

## ex13

(Divisor) Escreva um programa que leia dois inteiros positivos `N, M` e imprima "yes"
se `M` é um divisor de `N`, caso contrário, imprima "no".

## ex14

(Ordena 3) Escreva um programa que leia três inteiros e imprima-os por ordem na mesma linha.

O menor dos números deve aparecer como primeiro.

## ex15

(Ciclo) Escreva um programa que leia um inteiro positivo `N` e imprima os números `1..N`, um por linha.

