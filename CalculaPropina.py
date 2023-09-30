
print("Bienvenido a la calculadora de propina.")

cuenta = float(input("Cual es el total de la cuenta? $"))
cantidad_propina = int(input("Cuanto % quieres dejar de propina? 10, 12 o 15? "))
personas = int(input("Entre cuantos quieres dividir la cuenta? "))

porcentaje_propina = cantidad_propina / 100
cuenta_con_propina = cuenta * porcentaje_propina + cuenta

total = cuenta_con_propina / personas
cantidad_total = round(total, 2)
cantidad_total = "{:.2f}".format(total)

print(f"Cada persona debe pagar ${cantidad_total} ")
