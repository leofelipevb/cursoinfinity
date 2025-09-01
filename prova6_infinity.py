usuario_correto = "leo"
senha_correta = "123"

for i in range(3):
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Bem-vindo!")
        break
    else:
        tentativas_restantes = 2 - i
        if tentativas_restantes > 0:
            print(f"Credenciais incorretas. Você ainda tem {tentativas_restantes} tentativa(s).")
        else:
            print("Número máximo de tentativas atingido. Acesso negado.")
