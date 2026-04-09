'''
Problema: beecrowd / 1001
Data: 2026.04.07
Estudante: Luanny Cubas Ramos Silva
'''
# Objetivo: Ler dois números inteiros nas variáveis A e B, calcular a soma em X e exibir o resultado

# ---ANÁLISE (LIAC) ---
# Entrada: dois números inteiros, cada um em uma linha separada
# Processamentos: somar A + B e armazenar em X
# Saída: exibir no formato exato "X = valor" (espaços ao redor do =, sem mensagens extras)

# int() - converte o texto lido para um número inteiro
# input() - lê o valor fornecido (digitado ou pelo Beecrowd)
# int(input()) - lê e converte em uma única instrução
A = int(input())
B = int(input())

# O enunciado específica explicitamente as variáveis A, B e X - seguir à risca
X = A + B

# f-string: insere o valor de X dentro do texto com {}
# Atenção: espaço antes e depois do = é obrigatório conforme o enunciado
print(f"X = {X}")