# ===================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Adivinhe o Número"
# Arquivo    : adivinhe.py
# Autor      : Luanny Cubas Ramos Silva
# Data:      : 2026.05.28
# ===================================================

import random

numero_secreto = random.randint(1, 10)
palpite = int(input("Digite um número de 1 a 10:"))

print("Você chutou:", palpite)
print("O número secreto era:", numero_secreto)