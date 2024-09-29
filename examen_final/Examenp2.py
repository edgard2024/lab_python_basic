import random

def numero_aleatorio():
    return random.randint(1, 100)
def solicitar_numero():
    while True:
        try:
            numero = int(input("Ingreso un numero del 1 al 100: "))
            if 0 < numero <= 100:
                return numero
            else:
                print("Ingresa un numero valido")
        except ValueError:
            print("El ingresado no es un numero")

def adivina():
    numero1 = numero_aleatorio()

    print("intenta adivinar en numero del 1 al 100")
    while True:
        numerosolicitado = solicitar_numero()
        if numerosolicitado < numero1:
            print("El numero ingresado es menor al numero secreto")
        elif numerosolicitado > numero1:
            print("El numero ingresado es mayor al numero secreto")
        else:
            print("Felicidades acertaste el numero")
            print(f"El numero secreto era {numero1}")
            break

adivina()