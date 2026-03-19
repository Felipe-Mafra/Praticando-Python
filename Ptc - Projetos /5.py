import random
import string

senha = ''
numeros = '123456789'
letras = 'abcdefghijklmnopqrstuvwxyz'
especiais = '`˜!@#$%ˆ&*()_+=[]{;?/><'

for i in range(4):
    senha += random.choice(numeros)

for i in range(4):
    senha += random.choice(letras.lower())

for i in range(4):
    senha += random.choice(letras.upper())

for i in range(4):
    senha += random.choice(especiais)

senha = list(senha)
random.shuffle(senha)
senha = ''.join(senha)

print(f"senha: {senha}")