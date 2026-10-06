/*
 * Disciplina : 2026-PCAP
 * Problema   : beecrowd 1175
 * Autor      : Luanny Cubas Ramos Silva
 * Data       : 2026.10.06
*/
#include <stdio.h>

int main() {
    int n[20], i;

    for (i = 0; i < 20; i++) {
        scanf("%d", &n[i]);
    }

    for (i = 0; i < 20; i++) {
        printf("N[%d] = %d\n", i, n[19 - i]);

    }

    return 0;
}