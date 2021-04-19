# Algoritmos de Ordenação Eficiente

## Ex 1

Diga quais dos seguintes vectores corresponde a um amontoado (heap)?

- `<50, 25, 30, 27, 24, 21, 28>`
- `<50, 30, 25, 27, 24, 28, 21>`
- `<60, 50, 9, 40, 41, 10, 8>`
- `<40, 15, 18, 13, 11, 14, 16>`
- `<60, 30, 80, 10, 35, 70, 40>`

## Ex 2

A primeira operação do algoritmo heapsort é transformar o vector num amontoado. Considere que o vector de entrada do algoritmo é `<20, 11, 16, 9, 12, 14, 17, 19, 13, 15>`.

- Indique o conteúdo do vector após o passo de transformação num amontoado.
- Indique o conteúdo do vector após os dois maiores elementos terem sido ordenados (colocados na sua posição final), durante a operação de ordenação (heapsort).

## Ex 3

Qual o conteúdo do seguinte vector `<25, 19, 23, 15, 18, 16, 21, 12>` depois de os dois primeiros elementos (i.e. os dois maiores) terem sido ordenados, utilizando o algoritmo de ordenação heapsort?

## Ex 4

- (Radix LSD) Considere a aplicação do algoritmo radix sort LSD, em que cada passo os elementos são ordenados considerando um dígito, ao seguinte vector:

`<48372, 62309, 83861, 91874, 18913, 33829, 47812, 95954, 52377, 22394, 56108, 60991>`

Qual é o terceiro número da sequência, após o algoritmo ter considerado três digitos?

## Ex 5

- (Radix MSD) Considere o seguinte vector de números inteiros sem sinal de 6 bits:

`<32, 2, 34, 9, 6, 1, 20, 18, 10>`

Qual o conteúdo do vector após os primeiros dois passos do algoritmo de ordenação radix sort MSD, em que em cada passo os elementos são ordenados considerando 2 bits?

Nota: considere que o algoritmo é baseado numa versão estável do algoritmo counting sort. O algoritmo deve apenas processar os 6 bits menos significativos de cada número, independentemente dos números poderem ser guardados em palavras com maior número de bits.
