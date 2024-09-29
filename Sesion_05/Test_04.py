"""Practica"""
Var2 = 20
    def operaciones():
    a = input("ingrese valor para a:")
    b = input("ingrese valor para b:")
    try:
        a = float(a)
        b = float(b)
        suma = a + b
        suma = a / b
        print("datos ingresados son validos.")
    except TypeError:
        print("No es posible operar un string con un dato int")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    else:
        print(resultado)