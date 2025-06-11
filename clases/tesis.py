class Tesis:
    def __init__(self, id_tesis,nombre,institucion,fecha_investigacion,fecha_presentacion, campo_estudio, N_paginas, estado="DISPONIBLE"):
        self.id_tesis = id_tesis
        self.nombre = nombre
        self.institucion = institucion
        self.fecha_investigacion = fecha_investigacion
        self.fecha_presentacion = fecha_presentacion
        self.campo_estudio = campo_estudio
        self.N_paginas = N_paginas
        self.estado = estado
        self.categoria = [] #relacion uno a muchos con categoria, donde Tesis contiene a categoria

    @staticmethod
    def registrar():
        nueva_tesis = Tesis(
            id_tesis = int(input("Ingrese la id de la tesis:")),
            nombre = input("Escriba el nombre de la tesis:").upper(),
            institucion= input("Escriba el nombre de la institucion:").upper(),
            fecha_investigacion=input("Escriba la fecha de investigacion(YYYY/MM/DD): ").upper(),
            fecha_presentacion=input("Escriba la fecha de presentacion(YYYY/MM/DD): ").upper(),
            campo_estudio=input("Escriba el campo de estudio:").upper(),
            N_paginas=input("Digite el numero de paginas: ")
        )
        return nueva_tesis
    
    @staticmethod
    def consultar(lista_tesis):
        if not lista_tesis:
            print("No hay nada que mostrar!")
        else:
            for tesis in lista_tesis:
                print(tesis)

    
    @staticmethod
    def modificar(lista_tesis):
        if not lista_tesis:
            print("No hay nada que mostrar!")
        else:
            id = int(input("Inserte el id de la tesis a modificar:"))
            for tesis in lista_tesis:
                if tesis.id_tesis == id:
                    print("tesis encontrada con exito!")
                    print("*************************************")
                    print("Elija la opcion que desea realizar:")
                    print("1. cambiar nombre de la tesis")
                    print("2. cambiar la institucion")
                    print("3. cambiar fecha de investigacion")
                    print("4. cambiar fecha de presentacion")
                    print("5. Cambiar campo de estudio")
                    print("6. Cambiar numero de paginas")
                    choose = int(input("Seleccione una opcion:"))
                    match choose:
                        case 1:
                            tesis.nombre = input("Ingrese el nuevo nombre:")
                        case 2:
                            tesis.institucion = input("Ingrese el nuevo nombre de la institucion:")
                        case 3:
                            tesis.fecha_investigacion = input("Ingrese la nueva fecha de investigacion(YYYY/MM/DD):")
                        case 4:
                            tesis.fecha_presentacion = input("Ingresa la nueva fecha de presentacion(YYYY/MM/DD):")
                        case 5:
                            tesis.campo_estudio = input("Escriba el campo de estudio")
                        case 6:
                           tesis.n_paginas = input("Digite el numero de paginas")
                           
        print("Datos actualizados correctamente!")
        return
    
    @staticmethod
    def eliminar(lista_tesis):
        id = int(input("Escriba la id de la tesis a eliminar:"))
        for tesis in lista_tesis:
            if tesis.id_tesis == id:
                lista_tesis.remove(tesis)
                print("Tesis eliminada correctamente!")
                break
    
    @staticmethod
    def asignar_categoria(lista_categorias, lista_tesis):
        id1 = int(input("Ingrese el id de la tesis al que desea asignar categoria:"))
        id = int(input("Ingrese el id de la categoria a asignar:"))

        if not lista_tesis or not lista_categorias:
            print("No existe aun tesis o no existen aun categorias, cree una tesis antes")
            return
        
        for tesis in lista_tesis:
            if tesis.id_tesis == id1:
                for categoria in lista_categorias:
                    if categoria.id_categoria == id:
                        tesis.categoria.append(categoria)
                        print("Categoria agregada con exito!")
                        break

    def __str__(self):
        return f"|id_tesis::{self.id_tesis} | nombre::{self.nombre}| institucion::{self.institucion}| fecha investigacion::{self.fecha_investigacion}| fecha presentacion::{self.fecha_presentacion}| campo de estudio::{self.campo_estudio}| numero de paginas::{self.N_paginas}| estado::{self.estado}"