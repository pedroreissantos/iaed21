# Hash Tables

## ex01

Considere a seguinte função de dispersão:

    int hash(int value, int M) {
    return value % M;
    }

Usando uma tabela de dispersão por encadeamento externo (external chaining) para guardar elementos com as seguintes chaves

    0, 32, 1, 35, 2, 33, 38, 10, 4, 3 e 6,

e a função de dispersão definida em cima, e sabendo que `M = 10`, qual ou quais são as chaves dos elementos guardados na posição 3 da tabela (A primeira posição da tabela é a posição zero)?

## ex02

Qual o número total de conflitos (elementos adicionados a uma posição já contendo pelo menos um elemento) quando o último valor da sequência `< 17, 7, 28, 12, 0, 25, 37, 11 >` é introduzido numa tabela de dispersão de dimensão 10 com resolução por encadeamento externo (external chaining), inicialmente vazia, sabendo que a função de hash é `hash(k) = k mod 3`.

## ex03

Qual a posição em que é colocado o último valor da sequência `< 17, 7, 28, 12, 0, 25, 37, 11, 24 >` ao serem introduzidos numa tabela de dispersão de dimensão `M = 13` por linear probing, inicialmente vazia, sabendo que a função de hash é `hash(k) = k mod M`?

## ex04

Considere uma tabela de dispersão com resolução por procura linear (linear probing), que permite guardar números inteiros. A tabela tem dimensão `M = 10`, e a respectiva função de dispersão é `hash(k) = k mod M`. Indique, para a inserção na tabela da sequência `< 10, 18, 5, 25, 46, 101, 39, 17 >`, qual será o índice da entrada da tabela em que é inserido o último elemento ?

## ex05

Considere uma tabela de dispersão com resolução por dispersão dupla (double hashing), com dimensão `M = 10`, em que as funçõees de dispersão são dadas por:

    hashone(k) = k mod M
    hashtwo(k) = (1 + 3k)

Qual o índice da posição na tabela em que é colocado o último valor da sequência `< 10, 12, 7, 9, 3, 11, 2 >` assumindo que a tabela se encontra inicialmente vazia ?
