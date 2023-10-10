print("Bienvenido a la montaña rusa!")
estatura = int(input("Cual es tu estatura en centimetros? "))

if estatura >= 180:
    print("Excelente, puedes subir a la montaña rusa")
    edad = int(input("Cual es tu edad? "))
    if edad < 10:
        print("Paga $50, que te diviertas!!")
    elif edad < 18:
        print("Paga $100, que te diviertas!!")
    elif edad > 60:
        print(
            "Lo siento eres muy viejo para subir a la montaña rusa, cuida tu corazón."
        )
    else:
        print("Paga $500, que te diviertas")

else:
    print("Lo siento eres muy pequeño para subir la montaña rusa.")
