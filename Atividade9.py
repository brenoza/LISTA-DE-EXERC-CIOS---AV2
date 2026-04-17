def contar_notas():
    print("notas")
    notas = [6.5, 7.0, 8.2, 9.5, 5.8, 7.3, 10]

    acima_de_sete = 0
    for nota in notas:
        if nota > 7:
            acima_de_sete += 1

    print("notas:", notas)
    print(f"Quantidade de notas acima de 7: {acima_de_sete}")


contar_notas()
