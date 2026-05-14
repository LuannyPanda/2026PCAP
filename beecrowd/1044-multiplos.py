'''
Problema: beecrowd | 1044
Data: 2026.05.14
Estudante: Luanny Cubas Ramos Silva
'''
# Objetivo: Verificar se dois inteiros são múltiplos entre si

# --- ANÁLISE (LIAC) ---
# Entrada: dois inteiros A e B na mesma linha separados por espaço
# Processamento: identificar maior e menor, verificar se maior % menor == 0
# Saída: "Sao Multiplos" ou "Nao sao Multiplos"

A, B = input().split()
A = int(A)
B = int(B)

if A > B:
    maior = A
    menor = B
else:
    maior = B
    menor = A

if maior % menor == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")