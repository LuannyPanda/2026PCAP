'''
Problema: beecrowd | 1037
Data: 2026.05.14
Estudantes: Luanny Cubas Ramos Silva
'''
# Objetivo: Ler um valor float e indicar em qual intervalo se encontra

# --- ANÁLISE (LIAC) ---
# Entrada: um número de ponyo flutuante qualquer
# Processamento: verificar em qual dos intervalos o valor se enquadra
# [0,25] - 0 <= valor <= 25
# (25,50] - 25 < valor <= 50
# (50,75] - 50 < valor <= 75
# (75,100] - 75 < valor <= 100
# fora - qualquer outro valor
# Saída: mensagem com o intervalo correspondente ou "Fora de intervalo"

valor = float(input())

if 0 <= valor <= 25:
    print("Intervalo [0,25]")
elif 25 < valor <= 50:
    print("Intervalo (25,50]")
elif 50 < valor <= 75:
    print("Intervalo (50,75]")
elif 75 < valor <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")