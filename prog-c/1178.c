/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1178
* Autor      : Luanny Cubas Ramos Silva
* Data       : 2026.10.06
*/
#include <stdio.h>
int main() {
    double n[100];
    int i;

    scanf("%lf", &n[0]);

    for (i = 1; i < 100; i++) {
        n[i] = n[i - 1] / 2;
    }

    for (i = 0; i < 100; i++) {
        printf("N[%d] = %.4lf\n", i, n[i]);

    }

    return 0;
}