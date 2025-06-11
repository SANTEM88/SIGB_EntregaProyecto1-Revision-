class Autor:
    def __init__(self, id_autor, nombre, nacionalidad, fecha_nacimiento):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
    
    @staticmethod
    def registrar():
        nuevo_registrar = Autor(
            id_autor = int(input("Digite el id del autor: ")),
            nombre = input("Escriba el nombre del autor: ").upper(),
            nacionalidad = input("Escriba la nacionalidad del autor: ").upper(),
            fecha_nacimiento = input("Escriba la fecha de nacimiento(YYYY/MM/DD):")
        )
        return nuevo_registrar
    
    @staticmethod
    def consultar(lista_autores):
        if not lista_autores:
            print("No hay autores por mostrar!")
        else:
            for autor in lista_autores:
                print(autor)
    @staticmethod
    def modificar(lista_autores):
        if not lista_autores:
            print("No hay autores a modificar!")
            return
        else: 
            id = int(input("Ingrese el id del autor que desea modificar:"))
            for autor in lista_autores:
                if autor.id_autor == id:
                    print("--------------------------------------------")
                    print("El autor fue encontrado con exito!")
                    print("***************************************************")
                    print("A continuacion se muestra el menu de modificacion para el libro:")
                    print("1. Modificar el nombre")
                    print("2. Modificar la nacionalidad")
                    print("3. Modificar la fecha de nacimiento")
                    choose = input("Ingrese una opcion a realizar:")
                    match choose:
                        case 1:
                            autor.nombre = input("Escriba el nuevo nombre:")
                        case 2:
                            autor.nacionalidad = input("Escriba la nueva nacionalidad:")
                        case 3:
                            autor.fecha_nacimiento = input("Escriba la nueva fecha de nacimiento:")
        print("Cambios realizados con exito!")                    
        return
    
    @staticmethod
    def eliminar(lista_autores):
        id = input("Ingrese el id del autor a eliminar: ")
        for autor in lista_autores:
            if autor.id_autor == id:
                lista_autores.remove(autor)
                print("Autor eliminado correctamente!")
                break
        
    def __str__(self):
        return f"|id_autor::{self.id_autor}| nombre::{self.nombre}|nacionalidad::{self.nacionalidad}|fecha_nacimiento::{self.fecha_nacimiento}|"