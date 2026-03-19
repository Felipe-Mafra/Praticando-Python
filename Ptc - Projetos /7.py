import random

numero = random.randint(1, 100)
print(numero)

acertou = False
tentativas = 0

while not acertou:

    escolha = input("Tente adivinhar o numero entre 1-100: ")

    while not escolha.isdigit():
        print("ERRO: Digite um numero valido.")
        escolha = input("Tente adivinhar o numero entre 1-100: ")

    escolha = int(escolha)

    while escolha > 100 or escolha < 1:
        print("ERRO: Digite um numero entre 1 e 100.")
        escolha = int(input("Tente adivinhar novamente: "))

    tentativas += 1

    if escolha > numero:
        print("O numero é menor!")
    elif escolha < numero:
        print("O numero é maior!")
    else:
        print(f"Parabéns! Você acertou o número {numero} com {tentativas} tentativas.")
        acertou = True