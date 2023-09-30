# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

edad_int = int(age)

años_restantes = 90 - edad_int
dias_restantes = años_restantes * 365
semanas_restantes = años_restantes * 52
meses_restantes = años_restantes * 12



mensaje = f"Tienes {dias_restantes} dias, {semanas_restantes} semanas, y {meses_restantes} meses restantes"

print(mensaje)