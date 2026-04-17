def festa_amigos():
    print("escreva o nome de um amigo que esta na festa")
    amigos = []

    while True:
        nome = input("escreva: ")
        if nome == "":
            break
        amigos.append(nome)

    quantidade = len(amigos)
    print(f"\nVocê tem {quantidade} amigos na festa.")

    if quantidade % 2 == 0:
        print("Esse número é PAR.")
    else:
        print("Esse número é ÍMPAR.")


festa_amigos()
