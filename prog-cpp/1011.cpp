/*
Disciplina : 2026-PCAP
Problema   : 1011
Autor      : Luanny Cubas
Data       : 2026.11.03
*/

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int r;
    double volume;

    cin >> r;
    volume = (4 / 3.0) * 3.14159 * r * r * r;
    cout << fixed << setprecision(3);
    cout << "VOLUME = " << volume << endl;

    return 0;
}