lista = []

while True:
    print("1. Adicionar tarefa")
    print("2. Visualizar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

    escolha = int(input("Escolha uma opcao: "))
    match escolha:
        case 1:
            tarefa = input("Digite a tarefa que deseja adicionar: ")
            lista.append(tarefa)
        case 2:
            if not lista:
                print("Lista vazia!")
            else:
                for i,itens in enumerate(lista):
                    print(i, itens)
        case 3:
            if not lista:
                print("Lista vazia!")
            else:
                for i, item in enumerate(lista):
                    print(f"{i} - {item}")

                try:
                    indice = int(input("Digite o indice: "))
                    lista.pop(indice)
                    print("Tarefa removida!")
                except:
                    print("Indice invalido!")
        case 4:
            print("Encerrando...")
            break

        case _:
            print("Opcao invalida!")