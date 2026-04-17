def calcular_preco_final():
    print("koja Online")
    valor = float(input("digite o valor da compra (R$): "))

    if valor > 450:
        desconto = 0.20
    elif valor >= 155:
        desconto = 0.10
    else:
        desconto = 0.0

    preco_final = valor - (valor * desconto)

    print(f"\nValor original: R${valor:.2f}")
    print(f"Desconto aplicado: {desconto*100:.0f}%")
    print(f"Preço final: R${preco_final:.2f}")

calcular_preco_final()

