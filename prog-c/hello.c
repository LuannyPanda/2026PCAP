/* Comentario de bloco
Programa: Hello.c
Data: 2026.09.22
Autor: Luanny Cubas Ramos Silva
*/

// importa biblioteca padrao de entrada e saida 
#include <stdio.h>

// defino a funcao principal do tipo int
int main(){
    // printf == saida --> mostra na tela ; 
    // "entre aspas == texto" ; 
    // comando se encerra com ;
    printf("Hello World!\n");

    // receber 2 valores somar e mostrar o resultado
    int A=0;
    int B=0;
    printf("Digite um valor: ");
    scanf("%d", &A);
    printf("Digite outro valor: ");
    scanf("%d", &B);
    int soma = A+B;
    printf("Soma: %d\n", soma);
    
    // indica que chegou ao fim da funcao == retornando 0
    return 0;
}

/*
para compilar ==
gcc <nome-do-arquivo> -o nome-do-programa

para executar ==
./nome-do-programa
*/