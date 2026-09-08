# Continha Legal
Jogo autoral do meu fliperama. Abre pela opcao [4] do menu.
Autor: Luanny Cubas Ramos Silva
## A regra
O jogo gera 2 operacoes matematicas basicas (adicao e subtracao) para o jogado resolver. O jogador digita o resultado da conta e o programa valida se a resposta esta correta.
## Como jogar
1. Dentro da pasta fliperama, rode python3 main.py.
2. Escolha a opcao [4] do menu.
3. Escolha qual operacao deseja resolver (adicao ou subtracao).
4. Digite a resposta que acredita estar correta e pressione Enter.

## O que eu reusei do projeto, e onde
A peça titulo() vinda do modulo telas.py é usada no meu jogo na linha 3 para desenhar a testeira do jogo.
A contagem da partida vinda do modulo placar.py é usada em main.py na linha 54 para somar 1 em vezes_jogado a cada partida realizada.

## O que ainda não funciona
Se o jogador digitar uma letra em vez de um numero na hora de dar a resposta, o jogo quebra com erro.
A pontuacao do jogador é zerada toda vez que a partida termina, sem salvar o progresso individual de quem jogou.

## Autoavaliacao

Conceito que eu acho que a minha entrega vale: [A ou B]

### Mapa do projeto: onde esta cada coisa

| O que | Arquivo | Funcao |
|---|---|---|
| Adivinhe o Numero | `adivinhe.py` | `jogar_adivinhe` |
| Pedra-Papel-Tesoura | `ppt.py` | `jogar_ppt` |
| Par ou Impar | `parimpar.py` | `jogar_parimpar` |
| [NOME DO MEU JOGO] | `continhalegal.py` | `jogar_continhalegal` |
| Cadastro de jogadores | `jogadores.py` | `menu_jogadores` |
| Ranking Top 10 | `jogadores.py` | `listar` |
| Placar que sobrevive | `placar.py` | `salvar_placar`, `carregar_placar` |

### Criterio por criterio: o nivel e a prova

| Criterio | Nivel | Onde esta a prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura e registro | [A/B/C] | [arquivo, linha] |
| 2. As quatro operacoes | [A/B/C] | [arquivo, linha] |
| 3. Busca e indice | [A/B/C] | [arquivo, linha] |
| 4. Persistencia e primeira execucao | [A/B/C] | [arquivo, linha] |
| 5. Documentacao e autoavaliacao | [A/B/C] | [arquivo, linha] |
| 6. Jogo autoral e reuso | [A/B/C] | [arquivo, linha] |

### Usei IA?

Usei IA para resolver alguns problemas do Par ou Impar pois nao sabia como resolver sem a ajuda do pofessor.