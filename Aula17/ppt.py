# =============================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Pedra-Papel-Tesoura"
# Arquivo    : ppt.py
# Autor      : Luanny Cubas Ramos Silva
# Data       : 2026.06.16
# =============================================

import random

def resultado(jogador, maquina):
    if jogador == maquina:
        return "empate"
    if jogador == "pe" and maquina == "te":
        return "jogador"
    if jogador == "pa" and maquina == "pe":
        return "jogador"
    if jogador == "te" and maquina == "pa":
        return "jogador"
    return "maquina"

opcoes = ["pe", "pa", "te"]

pontos_jogador = 0
pontos_maquina = 0
sequencia_vitoria = 0

for rodada in range(1, 6):
    print("--- Rodada", rodada, "---")
    jogada_maquina = random.choice(opcoes)
    entrada = input("Sua jogada(pedra, papel, tesoura): ")
    jogada_jogador = entrada.lower().strip()


    if jogada_jogador not in opcoes:
        print("❌ Inválida! Você perde a rodada.")
        pontos_jogador = pontos_jogador + 1
    else:
        quem = resultado(jogada_jogador, jogada_maquina)
        if quem == "empate":
            print("🤝 Empate!")
        elif quem == "jogador":
            print("🎉 Você ganhou a rodada!")
            pontos_jogador = pontos_jogador + 1
            sequencia_vitoria = sequencia_vitoria + 1
        else:
            print("💀 A máquina venceu! Ela jogou", jogada_maquina)
            pontos_maquina = pontos_maquina + 1
            sequencia_vitoria = sequencia_vitoria
    

print("Placar final -> Você:", pontos_jogador, "| Máquina:", pontos_maquina, "| Sequência de vitórias:", sequencia_vitoria)