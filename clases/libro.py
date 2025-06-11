class Libro:
    def __init__(self, isbn,titulo,edicion,year,editorial,genero,idioma,n_copias,activo=True):
        self.isbn = isbn
        self.titulo = titulo
        self.edicion = edicion
        self.year = year
        self.editorial = editorial
        self.genero = genero
        self.idioma = idioma
        self.n_copias = n_copias
        self.activo = activo
        self.categoria = [] #relacion uno a muchos, donde libro contiene a categoria

    @staticmethod
    def registrar():
        nuevo_libro = Libro(
            isbn = input("Ingrese el ISBN del libro:"),
            titulo = input("Ingrese el titulo del libro:"),
            edicion = int(input("Digite la edicion del libro:")),
            year = int(input("Digite el año de creacion del libro:")),
            editorial = input("Escriba la editorial del libro:"),
            genero = input("Escriba el genero del libro:"),
            idioma = input("Escriba el idioma del libro:"),
            n_copias = int(input("Digite el numero de copias:"))
        )
        return nuevo_libro
    
    @staticmethod
    def consultar(lista_libros):
        if not lista_libros:
            print("No hay libros a mostrar")
        else:
            for libro in lista_libros:
                print(libro)
        return
    
    @staticmethod
    def modificar(lista_libros):
        if not lista_libros:
            print("No hay libros a modificar!")
            return
        else: 
            isbn = input("Ingrese el isbn del libro que desea modificar:")
            for libro in lista_libros:
                if libro.isbn == isbn:
                    print("--------------------------------------------")
                    print("Su libro fue encontrado con exito!")
                    print("***************************************************")
                    print("A continuacion se muestra el menu de modificacion para el libro:")
                    print("1. Modificar el titulo")
                    print("2. Modificar la edicion")
                    print("3. Modificar el año de creacion")
                    print("4. Modificar la editorial")
                    print("5. Modificar el genero")
                    print("6. Modificar el idioma")
                    print("7. Modificar el numero de copias")
                    choose = input("Ingrese una opcion a realizar:")
                    match choose:
                        case 1:
                            libro.isbn = input("Escriba el nuevo ISBN:")
                        case 2:
                            libro.edicion = input("Digite la nueva edicion:")
                            
                        case 3:
                            libro.year = input("Digite el nuevo año de creacion:")
                            
                        case 4:
                            libro.editorial = input("Escriba la nueva editorial del libro:")
                            
                        case 5:
                            libro.genero = input("Escriba el nuevo genero:")
                            
                        case 6:
                            libro.idioma = input("Escriba el nueva idioma:")
                            
                        case 7:
                            libro.n_copias = input("Digite el numero nuevo de copias:")

        print("Cambios realizados con exito!")                    
        return
    

    @staticmethod
    def eliminar(lista_libros):
        isbn = input("Escribe el ISBN del libro que deseas eliminar: ")
        for libro in lista_libros:
            if libro.isbn == isbn:
                lista_libros.remove(libro)
                print("Libro eliminado correctamente!")
                break

    @staticmethod
    def asignar_categoria(lista_categorias, lista_libros):
        isbn = input("Ingrese el ISBN de la tesis al que desea asignar categoria:")
        id = int(input("Ingrese el id de la categoria a asignar:"))

        if not lista_libros or not lista_categorias:
            print("No existe aun tesis o no existen aun categorias, cree una tesis antes")
            return
        
        for libro in lista_libros:
            if libro.isbn == isbn:
                for categoria in lista_categorias:
                    if categoria.id_categoria == id:
                        libro.categoria.append(categoria)
                        print("Categoria agregada con exito!")
                        break


    def __str__(self):
        return f"|ISBN::{self.isbn}|titulo::{self.titulo}|edicion::{self.edicion}|año::{self.year}|editorial::{self.editorial}|genero::{self.genero}|idioma::{self.idioma}|numero de copias::{self.n_copias}|activo={self.activo}"

