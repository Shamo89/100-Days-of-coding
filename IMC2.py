altura = float(input("Digite sua altura en metros: "))
peso = int(input("Digite su peso en kilogramos: "))

imc = peso / altura ** 2

resultado = round(imc, 2)

total = str(resultado)

if resultado <= 18.50:
  print (f"Tu IMC es " + (total) + " y estás bajo de peso según la ciencia.")
elif resultado <= 25 : 
   print(f"Tu IMC es " + (total) + " y estás en tu peso adecuado según la ciencia.")
elif resultado <= 30 :
  print(f"Tu IMC es " +  (total) + " y estás un poco pasado de peso según la ciencia")
elif resultado <= 35 :
  print(f"Tu IMC es " + (total) + " y eres obeso según la ciencia.")
elif resultado > 35 :
  print(f"Tu IMC es " + (total) + " y eres clínicamente obeso según la ciencia.")