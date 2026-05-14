'''
Problema: beecrowd | 1052
Data: 2026.05.14
Estudante: Luanny Cubas Ramos Silva
'''
# Objetivo: ler um valor entre 1 e 12, e apresentar como resposta o mês por extenso

# --- ANÁLISE (LIAC) ---
# Entrada: um número inteiro representando o mês
# Processamento: comparar o número lido com cada código da tabela
# Saída: mês correspondente

MES = int(input())

if MES == 1:
    print("January")
elif MES == 2:
    print("February")
elif MES == 3:
    print("March")
elif MES == 4:
    print("April")
elif MES == 5:
    print("May")
elif MES == 6:
    print("June")
elif MES == 7:
    print("July")
elif MES == 8:
    print("August")
elif MES == 9:
    print("September")
elif MES == 10:
    print("October")
elif MES == 11:
    print("November")
elif MES == 12:
    print("December")