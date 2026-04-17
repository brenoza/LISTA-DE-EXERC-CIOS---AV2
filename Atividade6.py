temperaturas = []

dias = 7
for i in range(dias):
    temp = float(input(f"Digite a temperatura do dia {i+1}: "))
    temperaturas.append(temp)

soma = sum(temperaturas) 
media = soma / dias
print(f"A média da semana foi {media:.2f} °C")