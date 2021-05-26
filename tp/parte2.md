# Perguntas Teste Prático - IAED 2020/2021

- Deverá submeter a resposta a ambas as perguntas ao Fenix como um .zip em __teste prático (2ªparte)__.
- __Cada aluno deverá utilizar um identificador na sessão Zoom no seguinte formato `identificadorMooshak:Nome`, eg, `al123456:José Almeida`.__
- __Deverá submeter dentro do prazo a solução que tiver, mesmo que incompleta. Serão consideradas soluções parciais ou não completamente funcionais das perguntas.__

## Projecto 1 (17h50-18h30)

Responda a ambas as peguntas.

__1.__ Altere os limites do nome das tarefas, do nome das actividades e do nome dos utilizadores para um máximo de 100 caracteres. Os limites definidos no enunciado original eram 50, 20 e 20, respectivamente.

__2.__ Um __grupo__ é um conjunto de até __10__ utilizadores já existentes no sistema.
Do ponto de vista do sistema, um grupo comporta-se como um utilizador, ou seja, se a tarefa é realizada por um grupo, o utilizador da tarefa é o grupo.

Crie o comando `g` por forma a que este permita definir grupos de utilizadores. O nome do grupo de utilizadores
está limimtado a 100 caracteres e poderá ser utilizado nas outras opções como um utilizador normal,
incluindo na listagem de utilizadores.

_Não se esqueça de adicionar a opção `g` ao `switch` dos comandos_.

O novo comando deverá funcionar como se descreve abaixo:

- __g__ - Adiciona um grupo de utilizadores.
  - Formato de entrada: `g grupo <utilizador> <utilizador> ... <utilizador>`
  - Formato de saída: NADA (excepto erro).
  - Erros:
    * `user already exists` no caso de já existir um utilizador (ou grupo) com o nome do grupo que se pretende definir.
    * `too many users` no caso de o novo utilizador, a ser criado, exceder o limite de utilizadores.
    * `no such user` no caso de ser indicado um utilizador para o grupo que não existe.
    * `repeated user` no caso de ser indicado o mesmo utilizador duas ou mais vezes para o grupo.
