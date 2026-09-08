import random
from random import randint
from telas import titulo, linha
from modulos import ler_opcao

def jogar_parimpar():
    titulo('PAR OU IMPAR')
    linha()
    pontos_jogador = 0
    pontos_maquina = 0

    while pontos_jogador < 2 and pontos_maquina < 2:
        escolha = input('Par ou Impar? ').strip().lower()

        numero_jogador = int(input('Escolha um numero de 0 a 5: '))
        while numero_jogador < 0 or numero_jogador > 5:
            numero_jogador = int(input('Digite um numero de 0 a 5: '))
    
        numero_maquina = random.randint(0, 5)

        soma = numero_jogador + numero_maquina

        if soma % 2 == 0:
            resultado = 'par'
        else:
            resultado = 'impar'

            print('--- RESULTADO DA RODADA ---')
            print(f'Voce jogou: {numero_jogador}')
            print(f'Maquina jogou: {numero_maquina}')
            print(f'Soma: {soma} ({resultado})')

            if escolha == resultado:
                pontos_jogador += 1
                print('Voce venceu a rodada!')
            else:
                pontos_maquina += 1
                print('A maquina venceu a rodada!')

            print('PLACAR -> Voce:', {pontos_jogador}, '| Maquina:', {pontos_maquina})
            print('-' * 30)

            if pontos_jogador == 2:
                print('PARABENS!!! Voce ganhou a melhor de 3!')
            else:
                print('O computador ganhou a melhor de 3!')
