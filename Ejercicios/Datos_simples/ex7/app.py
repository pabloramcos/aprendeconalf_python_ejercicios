peso = float(input("indique su peso(kg): "))
altura = float(input("Y su altura(m): "))

imc = peso / altura**2

print(f"Tu índice de masa corporal es {round(imc, 2)}")