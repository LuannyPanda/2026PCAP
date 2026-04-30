'''
Problema: beecrowd | 1005
Data: 2026.04.30
Estudante: Luanny Cubas Ramos Silva
'''
# Objetivo: Ler duas notas com pesos diferentes e calcular a média ponderada

# --- ANÁLISE (LIAC) ---
# Entrada: duas notas de ponto flutuante A e B (cada uma em uma linha)
# Processamento: média ponderada = (A * 3.5 + B * 7.5) / 11
# Saída: exibir no formato exato "MEDIA = valor" com 5 casas decimais

A = float(input())
B = float(input())

media = (A * 3.5 + B * 7.5) / 11

print(f"MEDIA = {media:.5f}")