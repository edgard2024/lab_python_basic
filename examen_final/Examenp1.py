class Persona:

    def __init__(self):
        self.__nombre = ""
        self.edad = 0
        self.ciudad = ""

    def solicitar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))
        self.ciudad = input("Ingrese su ciudad: ")
        print(f"Hola {self.nombre} tu edad es {self.edad} y tu ciudad es {self.ciudad}")


class Empleado(Persona):
    def __init__(self):
        super().__init__()

    def Agregar_sueldo(self):
        self.sueldo = 0
        self.sueldo = int(input("Ingrese su sueldo: "))

    def Pagar_impuesto(self):
        if self.sueldo > 5500:
            impuesto = self.sueldo * 0.09
            print(f"El impuesto a pagar es de {impuesto}")
        else:
            impuesto = 0
            print(f"Tu sueldo es menor a 5500 por lo cual no corresponde a pagar impuestos")
        return impuesto

    def ManejoDiccionario(self):
        Datos = {"nombre" : self.nombre, "edad" : self.edad, "ciudad" : self.ciudad, "sueldo" : self.sueldo, "impuesto" : self.Pagar_impuesto()}
        print(Datos)

colaborador1 = Empleado()
colaborador1.solicitar_datos()
colaborador1.Agregar_sueldo()
colaborador1.Pagar_impuesto()
colaborador1.ManejoDiccionario()