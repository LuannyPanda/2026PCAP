'''
Problema: beerowd | 1006
Data: 2026.04.30
Estudante: Luanny Cubas Ramos Silva
'''
# Objetivo: calcular a média de um aluno

# --- ANÁLISE (LIAC) ---
# Entrada: 3 valores com uma casa decimal
# Processamento: média ponderada = (A * 2 + B * 3 + C * 5)
# Saída: imprimir a mensagem "MEDIA" e a média do aluno

A = float(input())
B = float(input())
C = float(input())

media = (A * 2 + B * 3 + C * 5)/1.0

print(f"MEDIA={media:.1}")