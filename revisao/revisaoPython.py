# Fundamentos de Programação

# 1. Variáveis e tipos de dados == armazena um dado dependendo da forma que vai ser usado
nome = str("João") # str - a variável "nome" está armazenando o valor em formato de texto
idade = int(12) # int - a variável "idade" está armazenando o valor como número inteiro
horário = float(12.30) # float - armazena um dado em ponto flutuante
maiorIdade = True # bool - determina se o valor é verdadeiro ou falso

# 2. Operadores == operam um cálculo matemático dentro do código: +, -, ==, =!, *, %, **, //, /, <, >, <=, >=
2 + 2 # + - soma os valores
20 - 3 # -  subtrai os valores
0 == 0 # == - deixa os valores igualados
30 * 2 # * - multiplica os valores
120 / 8 # / - divide os valores
200 // 4 # // - divisão inteira
30 % 3 # % - divide o resto
2 ** 3 # ** - eleva um valor a potencia
67 < 68 # < - diz se um valor é menor que outro e <= diz se um valor é menor ou igual
34 > 33 # > - diz se um valor é maior que outro e >= diz se um valor é maior ou igual
33 != 3 # != - diz que um valor é diferente de outro

# 3. Entrada == é quando você manda um comando para o computador
input()

# 4. Saída == é quando o computador transmite uma mensagem
print("Olá! Tudo bom?")
nome = str("Panda")
print(f"Olá {nome}, Tudo bom?")

# 5. Estrutura de Condição == coloca uma condição para que o progama execute
numero = int(input("Qual número você quer?"))
if numero < 10:
    print("O número é menor que 10!")
else numero > 10
    print("O número é maior que 10!")

# 6. Estrutura de repetição == permite que um bloco de código seja executado várias vezes
batata = 0
while batata < 10:
    print("Compre batatas!")
    b = int(input("Vai levar quantas batatas hoje?"))
    batata = batata + b

for agua in range(1,4):
    print("Águinha H2O!")
    agua = agua + 1