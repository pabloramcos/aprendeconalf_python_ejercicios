cant_invertir = float(input("Cantidad a invertir: "))
inter_anual = float(input("Interés anual: "))
num_anhos = float(input("Número de años: "))

print(f"El capital obtenido es igual a {round(cant_invertir * (inter_anual / 100 + 1) ** num_anhos, 2)}")