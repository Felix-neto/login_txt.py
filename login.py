def app():
    print("os dados serão salvos em um arquivo .txt,\nentão melhor se registar primeiro")
    op = input("(1) logar \n(2) registrar \nEscolha:")

    if op == "1":
        usuario = input("Seu nome de usuario: ")
        senha = input("senha: ")
        with open("dados.txt","r") as dados:
            linhas = dados.readlines()
            usuario_salvo = linhas[0].strip()
            senha_salva = linhas[1].strip()

        if usuario_salvo == usuario and senha == linhas[1].strip():
            print(usuario_salvo, "logado")
        else:
            print("usuario não logado")
            tentar = input("gostaria de tentar novamente?\n (1)sim (2)não")
            if tentar == "1":
                app()
            elif tentar == "2":
                print("Até a proxima")
    elif op == "2":
        usuario_novo = input("Seu nome de usuario: ")
        senha_novo = input("senha: ")
        with open("dados.txt","w") as dados:
            dados.write(usuario_novo + "\n" + senha_novo)
        print("Ola", usuario_novo,", seu usuario foi criado, execute o app novamente e tente logar!")

app()