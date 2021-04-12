Considere que os algoritmos de ordenação ordenam sempre de forma não decrescente.

## ex01 (Análise Assimptótica)

Considere a seguinte função de procura de um elemento num vector ordenado.
A função recebe um vector **a**, o número de elementos *n* e o valor *elem*
que se pretende encontrar no vector.

```
int search(int a[], int n, int elem) {
  int left = 0, right = n-1;
  int med;

  while (left <= right) {
    int med = (left + right) / 2;
    if (a[med] == elem)
      return med;
    else if (a[med] < elem)
      left = med+1;
    else
      right = med-1;
  }
  return -1;
}
```

Indique a complexidade assimptótica da função search numa análise de pior caso
e numa análise de melhor caso.

## ex02 (Análise Assimptótica)

Indique a complexidade assimptótica da função abaixo numa análise de pior caso.
Indique ainda se o limite assimptótico é apertado ou se é apenas um limite superior.

```
int funcao (int a[], int n) {
  int i, sum = 0;

  for (i = 0; i < n/2; i++) 
    sum += a[i] + a[n-i-1];
  return sum;
}
```


## ex03 (Análise Assimptótica)

Considere a função abaixo que recebe dois vectores (**a** e **b**) onde
*n* e *m* denotam o número de elementos dos vectores **a** e **b**, respectivamente.

```
int funcao (int a[], int n, int b[], int m) {
  int i = n-1, count = 0;

  while (i > 0) {
    for (j = 0; j < m; j++) {
      if (a[i] == b[j])
        count++;
    }
    i = i/2;
  }
  return count;
}
```

Indique a complexidade assimptótica da função em função de *n* e *m* numa análise de pior caso.


## ex04 (Análise Assimptótica)

Considere a função abaixo que recebe dois inteiros *n* e *m*.

```
int funcao (int n, int m) {
  int i = 0, count = 0;

  while (i < n*n) {
    if (i % m == 0)
      count++;
    i++;
  }
  return count;
}
```

Indique a complexidade assimptótica da função numa análise de pior caso.


## ex05 (Análise Assimptótica)

Considere a função abaixo que recebe dois inteiros *n* e *m*.

```
int funcao (int n, int m) {
  int i = 0, count = 0;

  if (n % m == 0)
    return 0;

  while (i < n) {
    if (i % m == 0)
      count++;
    i = i + 2;
  }
  return count;
}
```

Indique a complexidade assimptótica da função numa análise de pior caso e numa análise de melhor caso.
É possível estabelecer uma complexidade assimptótica apertada para esta função? Justifique.


## ex06 (SelectionSort)

Considere a aplicação do algoritmo *selectionsort* ao vector **a**:

**a** = { 20, 11, 16, 8, 21, 12, 10, 14, 17, 6 }

Supondo que em cada iteração o algoritmo identifica o menor elemento e
o coloca na posição mais à esquerda, qual o conteúdo do vector **a**
após as três primeiras iterações?

## ex07 (SelectionSort)

Resolva o exercício anterior, mas considerando uma variação do
algoritmo SelectionSort. Suponha que em cada iteração, o algoritmo
identifica o maior elemento e o coloca na posição mais à direita.
Qual o conteúdo do vector **a** após as três primeiras iterações?

## ex08 (InsertionSort)

Considere a aplicação do algoritmo *insertionsort* ao vector **a**:

**a** = { 20, 11, 16, 8, 21, 12, 10, 14, 17, 6 }

Supondo que o algoritmo vai inserindo os elementos à esquerda,
qual o conteúdo do vector **a** após as três primeiras iterações?

## ex09 (BubbleSort)

Considere a aplicação do algoritmo *bubblesort* ao vector **a**:

**a** = { 20, 11, 16, 8, 21, 12, 10, 14, 17, 6 }

Supondo que em cada iteração o algoritmo percorre o vector da esquerda para a direita, qual o
conteúdo do vector **a** após as duas primeiras iterações?

## ex10 (BubbleSort - Melhor Caso)

A complexidade assimptótica de pior caso do algoritmo *bubblesort*,
é *O(n²)*. E no melhor caso? Ilustre com um exemplo.

## ex11 (QuickSort - partition)

Considere a implementação clássica da função `int partition (Item v[], int l, int r)` usada no algoritmo quicksort tal como apresentada nas aulas teóricas. Esta função recebe o vector `v` e as posições `left` e `right` que definem, respectivamente, os índices limite esquerdo e direito do vector a considerar na função. Suponha que o procedimento partition é invocado com os seguintes argumentos: `v = <13, 6, 5, 14, 12, 4, 16, 18, 7, 9, 10>`, `left = 0`, `right = 10`.  Considerando a posição `a[r]` como pivot, indique qual o conteúdo do vector `v` após a execução da função `partition`.
