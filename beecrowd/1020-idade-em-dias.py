'''
Problema: becrowd | 1020
Data: 2026.04.30
Estudante: Luanny Cubas Ramos Silva
'''
# Objetivo: Ler um valor inteiro correspondente à idade de uma pessoa em dias e informar em anos, meses e dias

# --- ANÁLISE (LIAC) ---
# Entrada: um número inteiro N representando a idade
# Processamento: extrair em ano, mês e dias restantes por divisãp inteira e módulo
# Saída: em a:m:d(sem zeros à esquerda)

N = int(input())

a = N // 365
N = N % 365

m = N // 30
N = N % 30

print(f"{a} ano(s)")
print(f"{m} mes(es)")
print(f"{N} dia(s)")