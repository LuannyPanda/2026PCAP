# Fliperama em C++ (MeuApp v4.0)

## O que e
O Fliperama e um programa desenvolvido em C++ para cadastrar jogadores e organizar partidas.
Ele foi criado a partir de uma versao anterior em C, utilizando recursos da linguagem C++ para facilitar o desenvolvimento.

## Como compilar e rodar
g++ -Wall fliperama.cpp -o fliperama
./fliperama

## Arquivos
- fliperama.cpp : contem o codigo principal do programa, responsavel pelo cadastro e gerenciamento dos jogadores.
- jogadores.csv : arquivo utilizado para armazenar os dados dos jogadores, organizados em colunas.

## C x C++: o que mudou
|O que | No fliperama.c (linha) | No fliperama.cpp (linha) |
|---|---|---|
|guardar um jogador | strcpy(apelidos[qtd], novo) (l. ) | apelidos.push_back(novo) (l. ) |
|comparar apelidos | strcmp(...) == 0 (l. ) | == (l. ) |
|a funcao que cadastra | int cadastrar(..., int qtd) (l. ) | void cadastrar(... &apelidos, ...) (l. ) |

## O que o C++ decidiu por mim
Em C, era necessario controlar manualmente o tamanho dos vetores e utilizar funcoes especificas para manipular textos.
Em C++, a linguagem oferece recursos como vector e string, que facilitam o armazenamento e a manipulacao dos dados.


## Autoavaliacao
|Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura, compilacao e Git A
| 2. Cadastro: vectors e referencia A
| 3. Jogo e partidas A
| 4. Persistencia A
| 5. Documentacao e comparacao B