
vendas = [120, 55, 78, 101, 200, 33, 42]
soma = 0
for valor in vendas:
    if valor % 2 == 0:  
        soma += valor

print("soma dos valores pares:", soma)
