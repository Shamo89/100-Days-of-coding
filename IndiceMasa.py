# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

a = float(height) 
b = int(weight)

bmi = b / a ** 2

resultado = int(bmi)

print(resultado)

# En este codigo la operación calcula el indice de masa corporal, combinamos un integer con un float
# El resultado que obtenemos es un float, que es modificado para que aparezca como un integer