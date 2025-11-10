cantidad_payasos = int(input("Número de payasos en el último pedido: "))
cantidad_munhecas = int(input("Número de muñecas en el último pedido: "))

peso_payaso = 112/1000
peso_munheca = 75/1000

print(f"El peso total de los payasos y muñecas en el último pedido fue de {peso_payaso*cantidad_payasos + peso_munheca*cantidad_munhecas} Kg")