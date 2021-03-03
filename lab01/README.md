### Exercícios

1.  **Olá mundo!**:

    1. Considere o ficheiro `hello.c` seguinte:
    ```
    #include <stdio.h>
    int main() {
        printf("Olá mundo!\n");
        return 0;
    }
    ```

    2. Experimente compilar e correr, escrevendo no terminal:
    ```
    $ gcc -ansi -pedantic -Wall -Wextra -Werror hello.c
    ```
     (A utilização das opções `-ansi -pedantic -Wall -Wextra -Werror` é sempre recomendada no âmbito desta cadeira.)
     Foi criado um ficheiro executável `a.out` com o programa que escreveu.

    3. Encontre o ficheiro criado listando o directório corrente com o comando: 

    `$ ls -l`

    4.  Pode agora executar o programa criado:

    `$ ./a.out`

    5. O executável pode ser nomeado durante a compilação com a opção `-o`:
    ```
    $ gcc -ansi -pedantic -Wall -Wextra -Werror -o hello hello.c
    $ ./hello
    ```

2. **Compilação e ligação de múltiplos ficheiros**:

    1. Mude para o directório `fact/` (`cd fact`) visualize os ficheiros `main.c`, `fact.h`, `iter.c` e `recurs.c` com um editor de texto, e observe:
        - declaração da função main: argumentos e tipo de retorno
        - valores de retorno
        - função do programa
        - includes e variáveis globais

    2. Compile os módulos fonte do programa iterativo (`main.c` e `iter.c`) e faça a ligação do código objecto.
    ```
    $ gcc -ansi -pedantic -Wall -Wextra -Werror -o iter main.c iter.c
    ```

    3. Execute o programa `iter` e verifique que este imprime o factorial de 5.

    4. Repita os passos 2 e 3 utilizando a versão recursiva.

3. **Passos intermédios do processo de compilação**:

    1. Pré-processamento: fase que antecede a compilação e que executa as directivas iniciadas por #. Por exemplo, no ficheiro `main.c` serão processadas as directivas `include` e `define`.
    ```
    $ gcc -E main.c
    ```
    O resultado do pré-processamento é enviado para o terminal. (O pré processador pode ser invocado separadamente com o comando `cpp`)

    2. *Compilação*: fase que gera código final em assembly. O assembly ainda tem um formato textual, pode ser lido e modificado por um vulgar editor de texto, mas o código gerado já depende do processador, arquitectura e sistema operativo. 
    ```
    $ gcc -S iter.c
    ```
     Verifique o código assembly gerado no ficheiro `iter.s`. Compare as variantes do ficheiro `iter.s` quando utiliza o optimizador (adicionar a opção `-O`) e a informação para o debugger (adicionar a opção `-g`).

    3. *Montagem ou assemblagem*: fase que produz os códigos binários, ficheiros objecto (".o", nada tem a ver com linguagens orientada para objectos), que serão processados pelo CPU. Esta fase é independente da linguagem de alto nível utilizada: C, Pascal, Fortran, etc. 
    ```
    $ gcc -c main.c
    ```
    O ficheiro gerado `main.o` já é código máquina e já não é um ficheiro de texto.
    Verifique o tipo de ficheiro gerado, com o comando: 
    ```
    $ file main.o
    ```
    e as dimensões das secções, com o comando: 
    ```
    $ size main.o
    ```
    e a tabela de símbolos, com o comando: 
    ```
    $ nm main.o
    ```

    4. *Ligação ou Linkagem*: fase que produz o ficheiro executável final através da interligação dos vários ficheiros objectos ou de bibliotecas (conjuntos de ficheiros objecto). 
    ```
    $ gcc -o factorial main.o iter.s
    ```
     Verifique o tipo de ficheiro gerado e as dimensões das secções. Use o comando `ldd` para verificar as dependências das bibliotecas dinâmicas. Tente gerar um ficheiro executável com as variantes iterativa e recursiva, simultaneamente, 
    ```
    $ gcc main.c iter.c recurs.c
    ```
    e verifique que existem duas realizações de factorial com o mesmo nome. Por outro lado, se tentar criar um ficheiro executável apenas com o ficheiro `main.c`, 
    ```
    $ gcc main.c
    ```
     falta um ficheiro ou biblioteca que forneça uma realização de factorial.

    5. O processo completo (*executável estático vs dinâmico*): o comando `gcc` permite, como já pode observar, controlar todo o processo de compilação para a linguagem C. Contudo, pode verificar a execução das diversas fases através da opção `-v`. 
    ```
    $ gcc -v -static main.c iter.c
    ```
     Neste exemplo, geramos um executável estático, isto é, não depende na execução da existência das bibliotecas dinâmicas. Como contrapartida, o executável final fica muito maior, pois inclui no próprio ficheiro uma cópia de todas as funções utilizadas, como por exemplo o `printf`. Verifique o tipo, dimensões do ficheiro ( `ls -l`), dimensões das secções e dependências do ficheiro `a.out` gerado, face ao executável dinâmico gerado na alínea anterior. Retire a informação simbólica, com o comando `strip`, e verifique que o executável ficou mais pequeno e que já não é possível saber a posição dos símbolos (comando `nm`).

    6. Inspeccione o exemplo de ficheiro `Makefile` com um editor de texto que cria os dois executáveis através do comando *make*:
    ```
    $ make clean
    $ make
    ```
4. **A importância das declarações**

    Mude para o directório `decl/` (`cd ../decl`) e compile os dois ficheiros com o comando: 
    ```
    $ gcc -Wall -Wextra -Werror -ansi -pedantic *.c
    ```
     As opções `-Wall -Wextra` obrigam o compilador a efectuar ainda mais verificações que numa compilação normal. No entanto, como o erro se deve a uma inconsistência na declaração da função `sqr` em ambos os ficheiros, a função está realizada como double (`sqr.c`) mas utilizada como inteiro (`main.c`), o compilador não consegue relacioná-las pois compila cada ficheiro separadamente.
    ```
    $ ./a.out
    ```
    Notar que a função `sqr` está escrita para números reais em precisão dupla (`double`), logo não serve de nada declará-la como inteira (`int sqr(int);`) mesmo que seja para calcular o quadrado de um número inteiro.
    No limite, se a declarar como uma cadeia de carateres (`char *sqr();`) e ajustar a impressão em conformidade (`printf("%s\n", sqr(4));`), obtenho lixo ou até um erro de execução (`segmentation fault`).
    A função só funcionará como esperado quando for declarada corretamente (`double sqt(double);`) e usada como tal (`printf("%g\n", sqr(4));`), produzindo `16` ou seja `4 x 4`.
    Como ter de saber de antemão as declarações de todas as rotinas seria fastidioso, as declarações são agrupadas em ficheiros de declaração `.h` por quem desenvolve as rotinas e incluídas `#include` por quem as usa. Assim, vamos substituir a declaração anterior `double sqr(double);` pela inclusão do ficheiro `sqr.h` no seu lugar: `#include "sqr.h"`
    Assim, ao realizar a rotina `sqr`no ficheiro `sqr.c` também devo introduzir a sua declaração em `sqr.h` para posterior utilização.

    Podemos compilar e executar o resultado.

5. **Comparação de linguagens e algoritmos**
    Mude para o directório `fib/` (`cd ../fib`) e compile o ficheiro `fibrec.c` com o comando: 
    ```
    $ gcc -o fibrec -O3 fibrec.c
    ```
    A opção `-O3` indica que o compilador de C deve gerar código de boa qualidade,
    mesmo gastando um pouco mais de tempo, embora o resultado não possa ser depurado *debug*.
    Para comparar o desempenho das diversas linguagens vamos utilizar o comando
    `time` existente nos sistemas `unix` para determinar o tempo gasto pela
    aplicação a executar (`user time`).
    Primeiro, utilizando a versão recursiva para calcular a série de *fibonacci*
    vamos calcular o elemento 35 da série em python e em C:
    ```
    $ time python fibrec.py 35
    $ time ./fibrec 35
    ```
    Note que os tempos de execução vão diminuindo consoante a linguagem vai sendo
    menos interpretada e mais compilada.
    Caso os tempos sejam muito próximos de zero, pode utilizar termos maiores
    da série, desde que inferiores a 46.
    Para tornar a execução mais rápida é necessário dispor de um algoritmo mais eficiente.
    Neste caso, existe uma versão recursiva, significativamente mais rápida.
    Repetindo o processo para os ficheiros `fibiter` nas três linguagens,
    pode-se verificar que os tempos são significativamente melhores.
    Na realidade as outras linguagens ficam quase ao nível da versão recursiva em C,
    embora mais lentos que a mesma versão em C.
    Com uma versão tão eficiente é possível calcular termos da série superiores a
    46 (até 92) desde que os inteiros de 32-bits sejam substituídos por inteiros
    de 64-bits (long) com mais capacidade, tal como presente no ficheiro `fiblong.c`.
