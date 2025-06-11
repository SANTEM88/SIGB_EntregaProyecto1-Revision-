from datetime import datetime, timedelta, date

class Prestamo:

    def __init__(self, id_prestamo, tipo_producto,dias_prestamo,fecha_prestamo,fecha_entrega_estimada,activo = True):
        self.id_prestamo = id_prestamo
        self.tipo_producto = tipo_producto
        self.dias_prestamo = dias_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega_estimada =fecha_entrega_estimada
        self.activo = activo
        self.copia = None
        self.articulo = None
        self.tesis = None
        self.lectores = []
    
    @staticmethod
    def registrar():
        mes_devolucion = 1 #prestar solo un mes
        fecha_actual = date.today()

        #calcular fecha de entrega con devolucion un mes
        def sumar_un_mes(fecha):
            año = fecha.year
            mes = fecha.month + mes_devolucion
            día = fecha.day

            if mes > 12:
                mes = 1
                año += 1

            while True:
                try:
                    nueva_fecha = date(año, mes, día)
                    return nueva_fecha.strftime("%Y/%m/%d")  #devuelve la cadena formateada
                except ValueError:
                    día -= 1  # Reduce el día hasta que sea válido

        fecha_final = sumar_un_mes(fecha_actual)

        nuevo_prestamo = Prestamo(
            id_prestamo=int(input("Digite el id del prestamo:")),
            tipo_producto=input("Ingrese el tipo de producto:"),
            dias_prestamo=int(input("ingrese los dias de prestamo:")),
            fecha_prestamo= fecha_actual.strftime("%Y/%m/%d"),
            fecha_entrega_estimada= fecha_final
        )
        return nuevo_prestamo
    
    @staticmethod
    def consultar(lista_prestamo):
        if not lista_prestamo:
            print("No hay nada a mostrar!")
        else:
            for prestamo in lista_prestamo:
                print(prestamo)

    @staticmethod
    def modificar(lista_prestamos):
        if not lista_prestamos:
            print("No hay nada que mostrar!")
        else:
            id = int(input("Inserte el id del prestamo a modificar:"))
            for prestamo in lista_prestamos:
                if  prestamo.id_prestamo == id:
                    print("prestamo encontrado con exito!")
                    print("*************************************")
                    print("Elija la opcion que desea realizar:")
                    print("1. cambiar el tipo de producto")
                    print("2. cambiar dias prestamo")
                    print("3. cambiar fecha de prestamo")
                    print("4. cambiar fecha de entrega estimada")
                    print("5. Cambiar actividad")
                    choose = int(input("Seleccione una opcion:"))
                    match choose:
                        case 1:
                            prestamo.tipo_producto = input("Escriba el tipo de producto:")
                        case 2:
                            prestamo.dias_prestamo = int(input("Ingrese los nuevos dias prestamo:"))
                        case 3:
                            prestamo.fecha_prestamo = input("Ingrese la nueva fecha de prestamo(YYYY/MM/DD):")
                        case 4:
                            prestamo.fecha_entrega_estimada = input("Ingresa la nueva fecha de estrega estimada(YYYY/MM/DD):")
                        case 5:
                            choose = int(input("1. activo 2. Inactivo"))
                            if choose == 1:
                                prestamo.activo = True
                            else:
                                prestamo.activo = False
                           
        print("Datos actualizados correctamente!")
        return
    
    @staticmethod
    def eliminar(lista_prestamos):
        id = int(input("Ingrese el id del prestamo a eliminar:"))
        for prestamo in lista_prestamos:
            if prestamo.id_prestamo == id:
                lista_prestamos.remove(prestamo)
                print("Prestamo eliminado correctamente!")
                break

    def __str__(self):
        return f"|id_prestamo::{self.id_prestamo}|tipo_producto::{self.tipo_producto}|dias_prestamo::{self.dias_prestamo}|fecha_prestamo::{self.fecha_prestamo}|fecha_entrega_estimada::{self.fecha_entrega_estimada}|activo::{self.activo}"