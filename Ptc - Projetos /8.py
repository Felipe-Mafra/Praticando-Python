def calculadora(text, n1, n2):
    match text:
        case '+':
            return n1 + n2
        case '-':
            return n1 - n2
        case '*':
            return n1 * n2
        case '/':
            if n2 == 0:
                print("Erro: Divisão por zero não é permitida.")
            return n1 / n2
        
try:
    n1 = float(input("Digite o primeiro numero: "))
    sinal = input("Digite um sinal de operacao (+, -, *, /) :  ")
    n2 = float(input("Digite o segundo numero: "))

    resultado = calculadora(sinal, n1, n2)
    print(resultado)

except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")
except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
