print("Quais são os numeros da soma?")

soma = 0.0

while True:
    numero = float(input("Digite um numero): "))
    if numero < 0:
        break
    soma += numero
    print(f"Soma total: {soma}")