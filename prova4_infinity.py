numero_1 = int(input("Digite o número de início: "))
numero_2 = int(input("Digite o número de fim: "))

soma = 0

for i in range(numero_1, numero_2 + 1):
    if i % 2 == 0:
        soma += i
else:
    if soma > 0:
        print(f"A soma dos números pares é {soma}")
    else:
        print("Não há números pares no intervalo.")
