import random
from random import randint
from telas import titulo, linha
from modulos import ler_opcao

def jogar_continhalegal():
    titulo('CONTINHA LEGAL')
    linha()
    
    print('Selecione uma operacao')
    print('[1] - Adicao')
    print('[2] - Subtracao')

    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    resultado = 0

    operacao = ler_opcao('Operacao escolhida: ', ['1', '2'])
    if operacao == '1':
        soma = n1 + n2
        print('Resolva a conta:')
        print(f'{n1} + {n2}')
        resultado = int(input('Resultado: '))
        if resultado == soma:
            print('Acertou!')
        else:
            print('Errou!')

    if operacao == '2':
        subtracao = n1 - n2
        print('Resolva a conta:')
        print(f'{n1} - {n2}')
        resultado = int(input('Resultado: '))
        if resultado == subtracao:
            print('Acertou!')
        else:
            print('Errou!')




    
        


