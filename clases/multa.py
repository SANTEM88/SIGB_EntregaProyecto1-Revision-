from datetime import datetime, timedelta, date

class Multa:
    def __init__(self, id_multa,lector,fecha_entrega,dias_retraso,dias_multa,fecha_inicio_multa,fecha_fin_multa,activa=True):
        self.id_multa = id_multa
        self.lector=lector
        self.fecha_entrega=fecha_entrega
        self.dias_retraso=dias_retraso
        self.dias_multa=dias_multa
        self.fecha_inicio_multa=fecha_inicio_multa
        self.fecha_fin_multa=fecha_fin_multa
        self.activa = activa
        self.prestamo = None

    @staticmethod
    def generar_multa(_,fecha_entrega_estimada,fecha_entrega_real):
        
        def dias_transcurridos(fecha_entrega_estimada: str, fecha_entrega_real: str) -> int:
            # Convertimos las cadenas de fecha al objeto datetime
            formato = "%Y/%m/%d"
            fecha1 = datetime.strptime(fecha_entrega_estimada, formato)
            fecha2 = datetime.strptime(fecha_entrega_real, formato)
            
            # Calculamos la diferencia en días
            diferencia = fecha2 - fecha1
            return diferencia.days
        
        def nueva_fecha(fecha_fin_multa_str, dias):
            # Convertimos la cadena a un objeto datetime.date
            fecha_obj = datetime.strptime(fecha_fin_multa_str, "%Y/%m/%d").date()
            
            # Sumamos los días usando timedelta
            nueva_fecha = fecha_obj + timedelta(days=dias)
            
            # Nueva fecha
            return nueva_fecha.strftime("%Y/%m/%d")
        
        dias_retraso = dias_transcurridos(fecha_entrega_estimada,fecha_entrega_real)

        fecha_inicio_multa = date.today()

        fecha_fin_multa = nueva_fecha(fecha_entrega_real, dias_retraso * 3)

        nueva_multa = Multa(
            id_multa=int(input("Ingrese el id de la multa:")),
            lector = input("Ingrese el nombre del lector:"),
            fecha_entrega= fecha_entrega_real,
            dias_retraso= dias_retraso,
            dias_multa= dias_retraso * 3,
            fecha_inicio_multa= fecha_inicio_multa.strftime("%Y/%m/%d"),
            fecha_fin_multa = fecha_fin_multa
        )
    
    @staticmethod
    def consultar(lista_multas):
        if not lista_multas:
            print("No hay nada que mostrar!")
        else:
            for multa in lista_multas:
                print(multa)

    @staticmethod
    def modificar(lista_multas):
        if not lista_multas:
            print("No hay nada que mostrar!")
        else:
            id = int(input("Inserte el id de la multa a modificar:"))
            for multa in lista_multas:
                if multa.id_tesis == id:
                    print("tesis encontrada con exito!")
                    print("*************************************")
                    print("Elija la opcion que desea realizar:")
                    print("1. cambiar lector")
                    print("2. cambiar fecha de entrega")
                    print("3. cambiar dias retraso")
                    print("4. cambiar dias de multa")
                    print("5. Cambiar fecha de inicio")
                    print("6. Cambiar fecha de fin de la multa")
                    print("7. cambiar actividad")
                    choose = int(input("Seleccione una opcion:"))
                    match choose:
                        case 1:
                            multa.lector = input("Ingrese el nuevo nombre del lector:")
                        case 2:
                            multa.fecha_entrega = input("Ingrese la fecha de entrega(YYYY/MM/DD):")
                        case 3:
                            multa.dias_retraso = input("Ingrese los dias de retraso:")
                        case 4:
                            multa.dias_multa = int(input("Ingresa los dias de multa:"))
                        case 5:
                            multa.fecha_inicio_multa = input("Escriba la fecha de inicio de la multa(YYYY/MM/DD):")
                        case 6:
                           multa.fecha_fin_multa = input("Escriba la fecha del fin de la multa(YYYY/MM/DD)")
                        case 7:
                            print("Elija el estado de la multa")
                            actividad = int(input("1. activa 2. inactiva"))
                            if actividad == 1:
                                multa.activa = True
                            else:
                                multa.activa = False
                           
        print("Datos actualizados correctamente!")
        return
    
    @staticmethod
    def eliminar(lista_multas):
        id = int(input("Ingrese el id de la multa a eliminar:"))
        for multa in lista_multas:
            if multa.id_multa == id:
                lista_multas.remove(multa)
                print("Multa eliminada correctamente!")
                break
            
    def __str__(self):
        return f"|id_multa::{self.id_multa}|lector::{self.lector}|fecha_entrega::{self.fecha_entrega}|dias_retraso::{self.dias_retraso}|dias_multa::{self.dias_multa}|fecha_inicio_multa::{self.fecha_inicio_multa}|fecha_fin_multa::{self.fecha_fin_multa}|activa::{self.activa}|"