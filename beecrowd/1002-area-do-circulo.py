'''
Problema: beecrowd | 1002
Data: 2026.04.23
Estudante: Luanny Cubas Ramos Silva
'''
# Objetivo: calcular a área do cículo, elevando o valor de raio ao quadrado e multiplicando por pi

# --- ANALISE (LIAC) ---
# Entrada:contém um valor de ponto flutuante, variável raio
# Processamento: aplicar a fórmula da área no círculo
# Saída: exibir no formato "A = algum valor" com 4 casas decimais

# Leitura do raio como número decimal
R = float(input())

# Defina pi conforme o enunciado indica
pi = 3.14159

# Qual é a fórmula da área do círculo?
AREA = pi * R **2

# Saída - observe o formato exato e o número de casas decimais no enunciado
print(f"A={AREA:.4f}")