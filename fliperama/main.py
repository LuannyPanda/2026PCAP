# ======================================
# Arquivo:    main.py
# Disciplina: 2026-PCAP
# Aula:       20
# Autor:      Luanny Cubas Ramos Silva
# Data:       2026.08.04
# Conceitos: 
# ======================================

# Importar funcoes de arquivos
from telas import titulo, linha
from adivinhe import jogar_adivinhe
from modulos import ler_opcao
from ppt import jogar_ppt
from parimpar import jogar_parimpar
from continhalegal import jogar_continhalegal
from placar import salvar_placar
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores


NOME_DOS_JOGOS = ['Adivinhe o Numero', 'Pedra-Papel-Tesoura', 'Par ou Impar', 'Continha Legal']
vezes_jogado = [0, 0, 0, 0]
jogadores = carregar_jogadores()
NOME_DO_DONO = 'LUANNY.PANDA'
OPCOES = ['0', '1', '2', '3', '4', '5']

def mostrar_placar():
    titulo('PLACAR')
    for i in range(3):
        print(NOME_DOS_JOGOS[i] + ': ' + str(vezes_jogado[i]) + 'x')

while True:
    titulo('FLIPERAMA DA ' + NOME_DO_DONO)
    print('[1] - Jogo Adivinhe o numero')
    print('[2] - Jogo Pedra-Papel-Tesoura')
    print('[3] - Jogo Par ou Impar')
    print('[4] - Jogar Continha Legal')
    print('[5] - Jogadores')
    print('[0] - Sair do Fliperama')
    linha()
    opcao = ler_opcao('Escolha uma opcao', OPCOES)

    if opcao == '0':
        mostrar_placar()
        salvar_placar(vezes_jogado)
        salvar_jogadores(jogadores)
        print('Ate a proxima!')
        break
 
    if opcao == '5':
        menu_jogadores(jogadores)
    else:
        indice = int(opcao) - 1
        if 0 <= indice < len(vezes_jogado):
            vezes_jogado[indice] = vezes_jogado[indice] + 1

        if opcao == '1':
            jogar_adivinhe()
        elif opcao == '2':
            jogar_ppt()
        elif opcao == '3':
            jogar_parimpar()
        elif opcao == '4':
            jogar_continhalegal()
        else:
            print('Opcao invalida!')
    

    input('Pressione Enter para voltar ao menu... ')