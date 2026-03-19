import random

def resultado(escolha, escolha_robo):

    escolha = escolha.lower()
    escolha_robo = escolha_robo.lower()

    if escolha == escolha_robo:
        print("Empate!")

    elif escolha == 'pedra' and escolha_robo == 'papel':
        print("O robo escolheu papel e venceu")

    elif escolha == 'pedra' and escolha_robo == 'tesoura':
        print("Voce venceu pois o robo escolheu tesoura")

    elif escolha == 'papel' and escolha_robo == 'pedra':
        print("Voce venceu pois o robo escolheu pedra")

    elif escolha == 'papel' and escolha_robo == 'tesoura':
        print("Voce perdeu pois o robo escolheu tesoura")

    elif escolha == 'tesoura' and escolha_robo == 'papel':
        print("Voce ganhou!")

    elif escolha == 'tesoura' and escolha_robo == 'pedra':
        print("Voce perdeu")

escolha = input("Escolha entre pedra papel ou tesoura: ")

while escolha.lower() not in ['pedra','papel','tesoura']:
    print('Escolha invalida!')
    escolha = input("Escolha entre pedra papel ou tesoura: ")

jogadas = ['pedra', 'papel', 'tesoura']
escolha_robo = random.choice(jogadas)

print(f"O robo escolheu {escolha_robo}.")

resultado(escolha, escolha_robo)