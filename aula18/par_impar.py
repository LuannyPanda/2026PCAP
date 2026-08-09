# ================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Par ou Ímpar"
# Arquivo    : par_impar.py
# Autor      : Luanny Cubas Ramos Silva
# Data       : 2026.06.25
# ================================================

import random
def quem_venceu(soma, jogada):
    if soma % 2 == 0:
        paridade = "par"
    else:
        paridade = "impar"
    
    if paridade == numero:
        return jogada
    else:
        return "maquina"

pontos_jogador = 0
pontos_maquina = 0
opcoes = ["par", "ímpar"]
rodada = 1

while pontos_jogador < 3 and pontos_maquina < 3 and rodada <= 5:
    maquina = random.randint(0, 5)
    numero = int(input("Número de(0 a 5): "))

    jogador = input("Sua escolha (par ou ímpar?): ")
    jogada = jogador.lower().strip()

    soma = numero + maquina



    if jogada not in opcoes:
        print("Jogada Inválida!")
    else:
        quem = quem_venceu(soma, jogada)
        if quem == "empate":
            print("empate")
        elif quem == "jogada":
            print("🎉 Você venceu")
            pontos_jogador = pontos_jogador + 1
        else:
            print("💀 A máquina venceu")
            pontos_maquina = pontos_maquina + 1

print("Placar -> Você:", pontos_jogador, "| Máquina:", pontos_maquina)
rodada = rodada + 1