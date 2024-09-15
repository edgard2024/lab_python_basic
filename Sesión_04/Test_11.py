"""
Requisitos:
    - Ingresar tu nombre y apellido por consola
    (cada valor tiene que estar en una varaible distinta)
    - Obtener el tamaño de tu nombre completo y mostrar en consola
    - Imprimir el resultado final todo en mayúsculas
    - Indicar mediante condicionales si el tamaño del nombre es mayor o no al del apellido ingresado
    (Ingresar solo en este caso el apellido paterno)"""
nombre = input("ingresar tu nombre: ")
apellido = input("ingresar tu apellido materno: ")
nombre_completo = nombre + " " + apellido
print("El tamaño de tu nombre es: {}".format(len(nombre_completo)))
print("El resultado final en mayusculas es: {}".format(nombre_completo.upper()))
if len(nombre) > len(apellido):
    print("El tamaño de tu nombres es mas grande que el de tu apellido")
elif len(nombre) < len(apellido):
    print("El tamaño de tu apellido es mas grande que el de tu nombre")
else:
    print("Tu nombre y apellido tienen el mismo tamaño")