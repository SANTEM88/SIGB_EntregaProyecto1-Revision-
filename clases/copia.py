class Copia:
    def __init__(self, id_copia, estado = "DISPONIBLE"):
        self.id_copia = id_copia
        self.estado = estado
        self.libros = []

    @staticmethod
    def registrar():
        nueva_copia = Copia(
            id_copia = int(input("Digite el id de la copia:"))
        )
        return nueva_copia
    @staticmethod
    def consultar(lista_copias):
        if not lista_copias:
            print("No hay nada que mostrar!")
        else:
            for copia in lista_copias:
                print(copia)
    
    @staticmethod
    def modificar(lista_copias):
        estado = ["DISPONIBLE","PRESTADA","CON RETRASO","EN REPARACION"]
        if not lista_copias:
            print("No hay nada que mostrar!")
        else:
            id = int(input("Inserte el id de la copia a modificar:"))
            for copia in lista_copias:
                if copia.id_copia == id:
                    print("copia encontrada con exito!")
                    print("*************************************")
                    print("Elija la opcion que desea realizar:")
                    print("1. cambiar estado")

                    choose = int(input("Seleccione una opcion:"))
                    match choose:
                        case 1:
                            print("Seleccione el estado:")
                            print("1.Disponible\n2.prestada\n3.con retraso\n4.en reparacion")
                            estado_opc = int("Seleccione una opcion:")
                            copia.estado = estado[estado_opc - 1]
        print("Datos actualizados correctamente!")
        return
    
    @staticmethod
    def eliminar(lista_copias):
        id = int(input("Ingrese el id de la copia a eliminar:"))
        for copia in lista_copias:
            if copia.id_copia == id:
                lista_copias.remove(copia)
                print("Copia eliminada correctamente!")
                break

    def __str__(self):
        return f"|id copia::{self.id_copia}|"

