"""Aplicacion
Requisitos:
    - Ingresar por teclado el sueldo de un empleado
    - Si el sueldo es mayor a 3500, imprimir "Su sueldo no tiene bonificación"
    - Caso contrario: "Su sueldo tiene bonificación este año y será de: sueldo_final", sueldo_final= sueldo + 20% sueldo"""
sueldo = int(input("ingrese su sueldo mensual: "))
sueldo_final = sueldo + (sueldo * 0.2)
if sueldo > 3500:
  print("Su sueldo no tiene bonificación")
else:
  print("Su sueldo tiene bonificación este año y sera de : {sueldo_final}")