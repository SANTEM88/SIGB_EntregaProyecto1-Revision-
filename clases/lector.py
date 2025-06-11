class Lector:
    def __init__(self, id_lector,nombre,telefono,direccion,estado="NORMAL"):
        self.id_lector = id_lector
        self.nombre = nombre
        self.telefono =telefono
        self.direccion = direccion
        self.estado = estado

    @staticmethod
    def registrar():
        nuevo_lector = Lector(
            id_lector = int(input("Digite el id del lector:")),
            nombre=input("Escriba el nombre del lector:"),
            telefono=input("Escriba el telefono del lector:"),
            direccion=input("Esceiba la direccion del lector:")
        )

    @staticmethod
    def consultar(lista_lectores):
        if not lista_lectores:
            print("No hay nada que mostrar")
        else:
            for lector in lista_lectores:
                print(lector)

    @staticmethod
    def modificar(lista_lectores):
        if not lista_lectores:
            print("No hay nada que mostrar!")
        else:
            id = int(input("Inserte el id del lector a modificar:"))
            for lector in lista_lectores:
                if lector.id_lector == id:
                    print("tesis encontrada con exito!")
                    print("*************************************")
                    print("Elija la opcion que desea realizar:")
                    print("1. cambiar nombre del lector")
                    print("2. cambiar el telefono")
                    print("3. cambiar fecha la direccion")
                    print("4. cambiar estado")

                    choose = int(input("Seleccione una opcion:"))
                    match choose:
                        case 1:
                            lector.nombre = input("Ingrese el nuevo nombre:")
                        case 2:
                            lector.telefono = input("Ingrese el nuevo telefono:")
                        case 3:
                            lector.direccion = input("Ingrese la nueva direccion:")
                        case 4:
                            estado = ["NORMAL","SANCIONADO","SUSPENDIDO", "INACTIVO"]
                            opc = int(input("1. normal 2.sancionado 3.suspendido 4.inactivo"))
                            lector.estado = estado[opc - 1]
        print("Datos actualizados correctamente!")
        return   
    
    @staticmethod
    def eliminar(lista_lectores):
        id = int(input("Ingrese el id del lector a eliminar:"))
        for lector in lista_lectores:
            if lector.id_lector == id:
                lista_lectores.remove(lector)
                print("Lector eliminado correctamente!")
                break

    def __str__(self):
        return f"|id_lector::{self.id_lector}|nombre::{self.nombre}|telefono::{self.telefono}|direccion::{self.direccion}| estado::{self.estado}|"