from clases.categoria import Categoria

class Articulo:
    def __init__(self, doi, titulo, editor, fecha_publicacion, revista, periodicidad, n_volumen, campo_interes, estado="DISPONIBLE"):
        self.doi = doi
        self.titulo = titulo
        self.editor = editor
        self.fecha_publicacion = fecha_publicacion
        self.revista = revista
        self.periodicidad = periodicidad
        self.n_volumen = n_volumen
        self.campo_interes = campo_interes
        self.estado = estado
        self.categoria = []
    
    #crear un nuevo articulo
    @staticmethod
    def registrar():
        nuevo_articulo = Articulo(
            doi=input("Inserte el doi del nuevo articulo: ").upper(),
            titulo=input("Inserte el titulo del articulo: ").upper(),
            editor=input("Inserte el editor del articulo: ").upper(),
            fecha_publicacion=input("Inserte la fecha de publicacion del articulo (YYYY/MM/DD): ").upper(),
            revista=input("Ingrese la revista a la que pertenece: ").upper(),
            periodicidad=input("Ingrese la periodicidad del articulo: ").upper(),
            n_volumen=input("Ingrese el numero del volumen del articulo: ").upper(),
            campo_interes=input("Escriba el campo de interes del articulo: ").upper()
        )
        if not nuevo_articulo.categoria: #esta vacia?
            print("Aun no se ha creado una categoria, cree la categoria para este articulo cientifico")
            nueva_categoria = Categoria.registrar()
            nuevo_articulo.categoria = nueva_categoria
            
        return nuevo_articulo
    
    #Consultar un articulo a partir de su doi
    @staticmethod
    def consultar(lista_articulos):
        imprimir = False
        doi = input("Escriba el doi del articulo a consultar: ")#consulta el articulo por doi
        for articulo in lista_articulos:
            if articulo.doi == doi:
                imprimir = True
                print(articulo)

        if imprimir:
            print("Mostrados con exito!")
        else:
            print("Articulo no encontrado!")

    @staticmethod
    def modificar(lista_articulos):
        cerrar_menu = 9
        doi = input("Escriba el doi del articulo a modificar: ")#consulta el articulo por doi
        for articulo in lista_articulos:
            if articulo.doi == doi:
                eleccion = int(input("Esta seguro que desea modificar este articulo?\n(Si:1 No:2)"))
                if eleccion == 1:
                    choose = 0
                    while choose != cerrar_menu:
                        #mini-menu para modificar
                        print("*********************************************************")
                        print("Qu'e desea modificar?: ")
                        print("1. Modificar el titulo")
                        print("2. Modificar el editor")
                        print("3. Modificar la fecha de publicacion")
                        print("4. Modificar la revista")
                        print("5. Modificar la periodicidad")
                        print("6. Modificar el n'umero del volumen")
                        print("7. Modificar el campo de inter'es")
                        print("8. Modificar el estado")
                        print("9. Salir")
                        choose = int(input("Eliga la opcion que quiera realizar: "))
                        print("*********************************************************")
                        match choose:
                            case 1:
                                articulo.titulo = input("Escriba el nuevo nombre o el nombre corregido del articulo cientifico")
                            case 2:
                                articulo.editor = input("Escriba el nuevo editor o el editor corregido del articulo cientifico")
                            case 3:
                                articulo.fecha_publicacion = input("Escriba la nueva fecha de publicaci'on")
                            case 4:
                                articulo.revista = input("Escriba el nuevo nombre para la revista")
                            case 5:
                                articulo.periodicidad = input("Escriba la nueva periodicidad del articulo cientifico")
                            case 6:
                                articulo.n_volumen = input("Escriba el nuevo volumen del articulo cientifico")
                            case 7:
                                articulo.campo_interes = input("Escriba el nuevo nombre del campo de interes del articulo cientifico")
                            case 8:
                                """
                                    USO EXCLUSIVO DEL PROGRAMADOR, NO INGRESE SI ES USUARIO
                                    CONTRASEÑA: 1323
                                """
                                contrasenya = 1323 #reservado usuario programador
                                contra = int(input("Solo personal autorizado, no entrar,inserte la contrasenya si lo es: "))
                                if contrasenya == contra:
                                    estado = ["DISPONIBLE", "PRESTADO", "EN REVISI'ON", "EN REPARACION", "NO DISPONIBLE"]
                                    print("De los siguientes estados eliga un tipo de estado")
                                    print("1:DISPONIBLE\n2:PRESTADO\n3:EN REVISION\n4:EN REPARACION\n5:NO DISPONIBLE")
                                    tipo_estado = int(input("Escriba la opcion que desea realizar: "))
                                    if tipo_estado <= 0:
                                        choose = 0 #repetir el men'u
                                    else:
                                        articulo.estado = estado[tipo_estado - 1]
                                        print("Estado modificado con exito!")
                                else:
                                    print("Usuario no autorizado para realizar esta opcion, regresando al menu principal!")
                                    choose = cerrar_menu
                            case 9:
                                choose = cerrar_menu
                            case _:
                                print("Vuelva a intentarlo, opcion incorrecta")
                else:
                    choose == cerrar_menu
        return
    
    @staticmethod
    def eliminar(lista_articulos):
        doi = input("Ingrese el doi del articulo cientifico a inhabilitar: ")
        for articulo in lista_articulos:
            if articulo.doi == doi :
                eleccion = int(input("Esta seguro de inhabilitar este articulo Si(1) No(2): "))
                if eleccion == 1:
                    articulo.estado = "NO DISPONIBLE"
                    #Articulo eliminado
                    print("Articulo Eliminado con Exito!")
                    break
                else:
                    break
        return
    
    @staticmethod
    def asignar_categoria(lista_categorias, lista_articulos):
        doi = input("Ingrese el doi del articulo al que desea asignar categoria:")
        id = input("Ingrese el id de la categoria a asignar:")

        if not lista_articulos or not lista_categorias:
            print("No existe el doi o no existen aun categorias, cree un articulo antes")
            return
        
        for articulo in lista_articulos:
            if articulo.doi == doi:
                for categoriar in lista_categorias:
                    if categoriar.id_categoria == id:
                        articulo.categoria.append(categoriar)
                        break

    def __str__(self):
        return f"| DOI: {self.doi}| Titulo: {self.titulo}| Editor: {self.editor}| Fecha: {self.fecha_publicacion}| Revista: {self.revista}| Volumen: {self.n_volumen}| Campo de interés: {self.campo_interes}| Estado: {self.estado} |"
