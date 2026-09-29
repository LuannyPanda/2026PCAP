/*
Problema 1043 beecrowd
2026.09.29
Luanny Cubas Ramos Silva
*/

#include <stdio.h>

int main() {
    float a, b, c;

    scanf("%f %f %f", &a, &b, &c);

    if (a < b + c && b < a + c && c < a + b) {
        float pe = a + b + c;
        printf("Perimetro = %.1f\n", pe);
    }else {
        float ar = (a + b) * c / 2;
        printf("Area = %.1f\n", ar);
    }

    return 0;
}