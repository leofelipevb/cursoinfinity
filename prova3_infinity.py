cont = 1

numero_certo = 7

numero = int(input("Digite o numero: "))

while cont <= 3:
    if numero != numero_certo:

        print("Errado, tente mais uma vez!")
        cont += 1

    elif numero == numero_certo:

        print("Acertou!")
        break