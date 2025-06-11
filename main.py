"""
    *
    * Universidad Tecnologica de Pereira
    *
    * Proyecto: gestion de una biblioteca
    * Revision del proyecto biblioteca VER(1.1)
    * Cambios:
    *   -Uso de correcto de metodos usando clases
    *   -Cambio correcto de paradigma a POO
    * Proyecto creado por:
    *   Nombre: Santiago Enriquez Martinez
    *   Codigo: 1010105344
"""

from clases.articulo import Articulo
from clases.categoria import Categoria
from clases.autor_articulo import Autor_articulo
from clases.autor_tesis import Autor_tesis
from clases.autor import Autor 
from clases.tesis import Tesis
from clases.libro import Libro
from clases.autor_libro import Autor_libro
from clases.copia import Copia
from clases.prestamo import Prestamo
from clases.lector import Lector
from clases.multa import Multa

#este es el menu principal del programa
def MenuPrincipal():
    articulos_registrados = [] #aqui es donde se guardan los articulos registrados

    categorias_registradas = [] #aqui es donde se guardan las categorias

    autores_registrados = [] #aqui es donde se guardan los autores

    autor_articulo_registrado = [] #aqui es donde se guarda la relacion autor_articulo

    tesis_registradas = [] #aqui es donde se guardan las tesis registradas

    autor_tesis_registradas = [] #aqui se guarda la relacion autor y tesis

    libros_registrados = [] #aqui se guardan libros registrados

    autor_libro_registrados = [] #aqui se guarda la relacion autor_libro

    copias_registradas = [] #aqui se guardan las copias registradas

    prestamos_registrados = [] #aqui se guardan los prestamos registrados

    lectores_registrados = [] #aqui se guardan los autores registrados

    multas_registradas = [] #aqui se guardan las multas registradas

    #preguntar si el usuario es super usuario o usuario comun
    def definirUsuario():
        contra = int(input("Si usted es usuario comun presione digite 456, si usted es super usuario, inserte aqui la contraseña de super usuario:"))
        super_usuario_contra = 123
        if super_usuario_contra == contra:
            print("BIENVENIDO SUPER USUARIO!")
            eleccion = 0
            while(eleccion != 6):
                print("******************************************************")
                print("Bienvenido al sistema de gestion de la Biblioteca\n")
                print("De las opciones de usuario y administrador:")
                print("     1. Todo sobre registrar")
                print("     2. Todo sobre consultar")
                print("Uso exclusivo del administrador:")
                print("     3. Todo sobre modificar")
                print("     4. Todo sobre eliminar")
                print("Otros usos de usuario:")
                print("     5. Otras opciones")
                print("     6. Salir")
                eleccion = int(input("Digite la opcion que quiere realizar: "))
                print("*****************************************************")

                match eleccion:
                    case 1:
                        print("*****************************")
                        MenuRegistrar(
                            articulos_registrados, 
                            categorias_registradas, 
                            autores_registrados, 
                            autor_articulo_registrado, 
                            autor_tesis_registradas, 
                            tesis_registradas,
                            libros_registrados,
                            autor_libro_registrados,
                            copias_registradas,
                            prestamos_registrados,
                            lectores_registrados,
                            multas_registradas
                        )
                    case 2:
                        print("*****************************")
                        MenuConsultar(
                            articulos_registrados, 
                            categorias_registradas, 
                            autores_registrados, 
                            tesis_registradas,
                            libros_registrados,
                            copias_registradas,
                            prestamos_registrados,
                            lectores_registrados,
                            multas_registradas
                        )
                    case 3:
                        print("******************************")
                        MenuModificar(
                            articulos_registrados, 
                            categorias_registradas, 
                            autores_registrados, 
                            tesis_registradas,
                            libros_registrados,
                            copias_registradas,
                            prestamos_registrados,
                            lectores_registrados,
                            multas_registradas
                        )
                    case 4:
                        print("*******************************")
                        MenuEliminar(
                            articulos_registrados, 
                            categorias_registradas, 
                            autores_registrados, 
                            tesis_registradas,
                            libros_registrados,
                            copias_registradas,
                            prestamos_registrados,
                            lectores_registrados,
                            multas_registradas
                        )
                    case 5:
                        print("******************************")
                        MenuOtrasOpciones(
                            articulos_registrados, 
                            categorias_registradas, 
                            autores_registrados, 
                            tesis_registradas,
                            libros_registrados,
                            copias_registradas,
                            prestamos_registrados,
                            lectores_registrados,
                            multas_registradas
                        )

                    case 6:
                        print("Saliendo del sistema...")
                    case _:
                        print("Digito un numero incorrecto, vuelva a intentarlo")
        elif contra == 456:
            print("BIENVENIDO USUARIO!")
            eleccion = 0
            while(eleccion != 6):
                print("******************************************************")
                print("Bienvenido al sistema de gestion de la Biblioteca\n")
                print("De las opciones de usuario y administrador:")
                print("     1. Todo sobre registrar")
                print("     2. Todo sobre consultar")
                print("Uso exclusivo del administrador:")
                print("     3. Todo sobre modificar")
                print("     4. Todo sobre eliminar")
                print("Otros usos de usuario:")
                print("     5. Otras opciones")
                print("     6. Salir")
                eleccion = int(input("Digite la opcion que quiere realizar: "))
                print("*****************************************************")

                match eleccion:
                    case 1:
                        print("*****************************")
                        MenuRegistrar(
                            articulos_registrados, 
                            categorias_registradas, 
                            autores_registrados, 
                            autor_articulo_registrado, 
                            autor_tesis_registradas, 
                            tesis_registradas,
                            libros_registrados,
                            autor_libro_registrados,
                            copias_registradas,
                            prestamos_registrados,
                            lectores_registrados,
                            multas_registradas
                        )
                    case 2:
                        print("*****************************")
                        MenuConsultar(
                            articulos_registrados, 
                            categorias_registradas, 
                            autores_registrados, 
                            tesis_registradas,
                            libros_registrados,
                            copias_registradas,
                            prestamos_registrados,
                            lectores_registrados,
                            multas_registradas
                        )
                    case 3:
                        print("Usted es usuario comun no puede acceder a esta funcion!")
                        """
                        print("******************************")
                        MenuModificar(
                            articulos_registrados, 
                            categorias_registradas, 
                            autores_registrados, 
                            tesis_registradas,
                            libros_registrados,
                            copias_registradas,
                            prestamos_registrados,
                            lectores_registrados,
                            multas_registradas
                        )
                        """
                    case 4:
                        print("Usted es usuario comun no puede acceder a esta funcion!")
                        """
                        print("*******************************")
                        MenuEliminar(
                            articulos_registrados, 
                            categorias_registradas, 
                            autores_registrados, 
                            tesis_registradas,
                            libros_registrados,
                            copias_registradas,
                            prestamos_registrados,
                            lectores_registrados,
                            multas_registradas
                        )
                        """
                    case 5:
                        print("******************************")
                        MenuOtrasOpciones(
                            articulos_registrados, 
                            categorias_registradas, 
                            autores_registrados, 
                            tesis_registradas,
                            libros_registrados,
                            copias_registradas,
                            prestamos_registrados,
                            lectores_registrados,
                            multas_registradas
                        )
                    case 6:
                        print("Saliendo del sistema...")
                    case _:
                        print("Digito un numero incorrecto, vuelva a intentarlo")
        else:
            print("Digito una opcion erronea, saliendo del sistema!")

    definirUsuario()
#menu que tiene que ver con todo sobre registros
def MenuRegistrar(
    articulos_registrados, 
    categorias_registradas, 
    autores_registrados, 
    autor_articulo_registrado, 
    autor_tesis_registradas, 
    tesis_registradas,
    libros_registrados,
    autor_libro_registrados,
    copias_registradas,
    prestamos_registrados,
    lectores_registrados,
    multas_registradas
):
    eleccion = 0
    while(eleccion != 10):
        print("*****************************************************************************")
        print("Este es el submenu referente a registrar, elija que documento desea registrar:")
        print("     1. Registrar articulo cientifico")#funcionando
        print("     2. Registrar libro")#funcionando
        print("     3. Registrar autor")#funcionando
        print("     4. Registrar tesis")#funcionando
        print("     5. Registrar categoria")#funcionando
        print("     6. Registrar Copia")#funcionando
        print("     7. Registrar Prestamo")#funcionando
        print("     8. Registrar lector")#funcionando
        print("     9. Registrar multa")
        print("     10. Salir")

        eleccion = int(input("Ingrese la opcion que desea realizar: "))
        print("*****************************************************************************")
        match eleccion:
            case 1:
                nuevo_articulo = Articulo.registrar() #registrar nuevo_articulo
                categorias_registradas.append(nuevo_articulo.categoria)
                articulos_registrados.append(nuevo_articulo)
                #relacion autor con articulo
                if not autores_registrados:
                    print("Aun no hay autores registrados")
                    print("Se creara un autor")
                    nuevo_autor = Autor.registrar()
                    autores_registrados.append(nuevo_autor)#registra el autor
                    relacion_autor_articulo = Autor_articulo.registrar()
                    relacion_autor_articulo.id_autor.append(nuevo_autor)
                    relacion_autor_articulo.id_articulo.append(nuevo_articulo)
                    #guardar relacion
                    autor_articulo_registrado.append(relacion_autor_articulo)
                else:
                    print("Hay autores registrados, desea crear uno nuevo o enlazar con uno existente\nCrear nuevo(1) Elegir existente(2)")
                    elegir = int(input("Digite su eleccion"))

                    if elegir == 1:
                        nuevo_autor = Autor.registrar()
                        autores_registrados.append(nuevo_autor)#registra el autor
                        relacion_autor_articulo = Autor_articulo.registrar()
                        relacion_autor_articulo.id_autor.append(nuevo_autor)
                        relacion_autor_articulo.id_articulo.append(nuevo_articulo)

                        autor_articulo_registrado.append(relacion_autor_articulo)
                    else:
                        id = int(input("Seleccione el id del autor"))

                        for autor in autores_registrados: #buscar entre autores registrados
                            if id == autor.id_autor:
                                relacion_autor_articulo = Autor_articulo.registrar()
                                relacion_autor_articulo.id_autor.append(autor)
                                relacion_autor_articulo.id_articulo.append(nuevo_articulo)
                                autor_articulo_registrado.append(relacion_autor_articulo)

                print("Articulo registrado con exito!")
                eleccion = 10 #salir

            case 2:
                #confirmacion
                nuevo_libro = Libro.registrar()
                libros_registrados.append(nuevo_libro)
                if not autores_registrados:
                    nuevo_autor = Autor.registrar()
                    autores_registrados.append(nuevo_autor)
                    nuevo_autor_libro = Autor_libro.registrar()
                    nuevo_autor_libro.isbn.append(nuevo_libro.isbn)
                    nuevo_autor_libro.id_autor.append(nuevo_autor.id_autor)
                    autor_libro_registrados.append(nuevo_autor_libro)#guarda la relacion entre autor y libro
                else:
                    id = int(input("Ingrese el id del autor del libro:"))
                    for autor in autores_registrados:
                        if autor.id_autor == id:
                            nuevo_autor_libro = Autor_libro.registrar()
                            nuevo_autor_libro.isbn.append(nuevo_libro.isbn)
                            nuevo_autor_libro.id_autor.append(autor.id_autor)
                            autor_libro_registrados.append(nuevo_autor_libro)#guarda la relacion entre autor y libro
                            break
                
                if not categorias_registradas:
                    nueva_categoria = Categoria.registrar()
                    nuevo_libro.categoria.append(nueva_categoria)
                    categorias_registradas.append(nueva_categoria)
                else:
                    print("Las siguientes son las categorias que se han registrado:")
                    for categoria in categorias_registradas:
                        print(categoria)
                    id = int(input("Digite la id de la categoria a ser agregada en el libro:"))
                    for categoria in categorias_registradas:
                        if id == categoria.id_categoria:
                            nuevo_libro.categoria.append(categoria.id_categoria)
                            break

                eleccion = 10#salir

            case 3:
                nuevo_autor = Autor.registrar()
                imprime = False
                #verificar si ya existe un autor
                for autor in autores_registrados:
                   if autor.id_autor == nuevo_autor.id_autor:
                       imprime = True
                       break  
                
                if(imprime):
                    print("Ese autor ya existe")
                else:
                    print("El autor no existe, revise si creo un documento anteriormente!")

                eleccion = 10 #salir

            case 4:
                #verificacion de tesis
                nueva_tesis = Tesis.registrar()
                tesis_registradas.append(nueva_tesis)  
                #si no encuentra autores              
                if not autores_registrados:
                    print("No hay autores registrados, se creara un nuevo autor")
                    nuevo_autor = Autor.registrar()
                    autores_registrados.append(nuevo_autor)
                    relacion_autor_tesis = Autor_tesis.registrar()
                    relacion_autor_tesis.id_autor.append(nuevo_autor.id_autor)
                    relacion_autor_tesis.id_tesis.append(nueva_tesis.id_tesis)
                    autor_tesis_registradas.append(relacion_autor_tesis)
                else:
                    print("Ya hay autores registrados")
                    print("Desea crear uno nuevo o enlazar con uno existente\nCrear uno nuevo(1) Enlazar con existente(2)")
                    elegir = int(input("Eliga la opcion que desea realizar:"))
                    if elegir == 1:
                        nuevo_autor = Autor.registrar()
                        autores_registrados.append(nuevo_autor)
                        relacion_autor_tesis = Autor_tesis.registrar()
                        relacion_autor_tesis.id_autor.append(nuevo_autor.id_autor)
                        relacion_autor_tesis.id_tesis.append(nueva_tesis.id_tesis)
                        autor_tesis_registradas.append(relacion_autor_tesis)   
                    else:
                        for autor in autores_registrados:
                            if autor.id_autor == id:
                                relacion_autor_tesis = Autor_tesis.registrar()
                                relacion_autor_tesis.id_autor.append(nuevo_autor.id_autor)
                                relacion_autor_tesis.id_tesis.append(nueva_tesis.id_tesis)
                                autor_tesis_registradas.append(relacion_autor_tesis)
                #Si no encuentra categorias
                if not categorias_registradas:
                    print("No hay categorias, creando una categoria: ")
                    nuevo_categoria = Categoria.registrar()
                    categorias_registradas.append(nuevo_categoria)
                    nueva_tesis.categoria.append(nuevo_categoria)
                else:
                    print("Hay categorias registradas, desea crear una nueva categoria o enlazar una nueva categoria\nnueva categoria Si(1) enlazar(2)")
                    elegir = int(input("Digite la opcion que desea realizar:"))
                    if elegir == 1:
                        nuevo_categoria = Categoria.registrar()
                        categorias_registradas.append(nuevo_categoria)
                        nueva_tesis.categoria.append(nuevo_categoria)
                    else:
                        buscar_categoria = int(input("Ingrese el id de la categoria:"))
                        for categoria in categorias_registradas:
                            if categoria.id_categoria == buscar_categoria:
                                nueva_tesis.categoria.append(categoria)
                print("Registro exitoso!")
                eleccion = 10

            case 5:
                nueva_categoria = Categoria.registrar()
                categorias_registradas.append(nueva_categoria)
                print("Categoria agregada satisfactoriamente!")
                eleccion = 10

            case 6:
                nueva_copia = Copia.registrar()
                copias_registradas.append(nueva_copia)
                if not libros_registrados:
                    print("No hay libros creados, creando uno nuevo:")
                    nuevo_libro = Libro.registrar()
                    nueva_copia.libros.append(nuevo_libro)
                else:
                    isbn = input("Escriba el isbn del libro registrado:")
                    for libro in libros_registrados:
                        if libro.isnb == isbn:
                            nueva_copia.libros.append(libro.isbn)
                print("Copia creada con exito!")

                eleccion = 10#salir
            case 7: 
                nuevo_prestamo = Prestamo.registrar()
                print("Elija el tipo de prestamo que desea realizar:")
                print("     1. Prestar copia de un libro")
                print("     2. Prestar un articulo cientifico")
                print("     3. Prestar una tesis")
                elec = int(input("Digite la opcion que desea realizar:"))
                match elec:
                    case 1:
                        if not copias_registradas:
                            print("Aun no hay copias registradas!")
                            return 
                        
                        id = int(input("Digite la id de la copia de libro a ser prestada:"))
                        for copia in copias_registradas:
                            if copia.id_copia == id:
                                nuevo_prestamo.copia = copia.id_copia
                                nuevo_prestamo.activo = False #al prestar el libro ya no esta activo
                                break

                    case 2:

                        if not articulos_registrados:
                            print("Aun no hay articulos registrados!")
                            return 
                        
                        doi = input("Ingrese el doi del articulo a ser registrado:")
                        for articulo in articulos_registrados:
                            if articulo.doi == doi:
                                nuevo_prestamo = articulo.doi
                                nuevo_prestamo.activo = False #al prestar el libro ya no esta activo
                                break  
              
                    case 3:

                        if not copias_registradas:
                            print("Aun no hay tesis registradas!")
                            return 
                        
                        id = int(input("Digite la id de la tesis registrada:"))
                        for tesis in tesis_registradas:
                            if tesis.id_tesis == id:
                                nuevo_prestamo.tesis = tesis.id_tesis
                                nuevo_prestamo.activo = False #al prestar el libro ya no esta activo
                                break

                    case _:
                        print("No es una opcion correcta, regresando al menu principal")
                        return

                if not lectores_registrados:
                    print("Aun no hay lectores creados, creando nuevo lector:")
                    nuevo_lector = Lector.registrar()
                    lectores_registrados.append(nuevo_lector)
                    nuevo_prestamo.lectores.append(nuevo_lector)
                    prestamos_registrados.append(nuevo_prestamo) #guardar prestamo
                else:
                    id = int(input("Ingrese el id del lector que hara el prestamo:"))
                    for lector in lectores_registrados:
                        if lector.id_lector == id:
                            nuevo_prestamo.lectores.append(lector.id_lector)
                            prestamos_registrados.append(nuevo_prestamo) #guardar prestamo
                            break

                eleccion = 10#salir

            case 8:
                nuevo_lector = Lector.registrar()
                lectores_registrados.append(nuevo_lector)
                print("Creado con exito!")
                eleccion = 10#salir del menu
            case 9:
                if not prestamos_registrados:
                    print("No hay prestamos registrados, cree un prestamo antes!")
                    eleccion = 10#salir
                else:
                    id = input("Ingrese el id del prestamo a registrar:")
                    for prestamo in prestamos_registrados:
                        if prestamo.id_prestamo == id:
                            fecha_real_entrega = input("Ingrese la fecha de entrega del documento(YYYY/MM/DD):")
                            nueva_multa = Multa.generar_multa(prestamo,prestamo.fecha_entrega_estimada, fecha_real_entrega)
                            multas_registradas.append(nueva_multa)
                            print("Exito al crear!")
                            eleccion = 10#salir del menu
            case _:
                print("El numero que digitaste es incorrecto, selecciona una opcio'n correcta!")
#menu que tiene que ver con todo sobre consultas
def MenuConsultar(
    articulos_registrados, 
    categorias_registradas, 
    autores_registrados, 
    tesis_registradas,
    libros_registrados,
    copias_registradas,
    prestamos_registrados,
    lectores_registrados,
    multas_registradas
):
    eleccion = 0
    while(eleccion != 10):
        print("*****************************************************************************")
        print("Este es el submenu referente a consultar, elija que documento desea consultar:")
        print("1. Consultar articulo cientifico")#funcionando
        print("2. Consultar libro")#funcionando
        print("3. Consultar autor")#funcionando
        print("4. Consultar tesis")#funcionando
        print("5. Consultar categoria")#funcionando
        print("6. Consultar Copia")#funciona
        print("7. Consultar Prestamo")#funciona
        print("8. Consultar lector")#funciona
        print("9. Consultar multa")#funciona
        print("10. Salir")

        eleccion = int(input("Ingrese la opcion que desea realizar: "))
        print("*****************************************************************************")
        match eleccion:
            case 1:
                Articulo.consultar(articulos_registrados)
                return
            case 2:
                Libro.consultar(libros_registrados)
                return
            case 3:
                Autor.consultar(autores_registrados)
                return
            case 4:
                Tesis.consultar(tesis_registradas)
                return
            case 5:
                Categoria.consultar(categorias_registradas)
                return
            case 6:
                Copia.consultar(copias_registradas)
                return
            case 7:
                Prestamo.consultar(prestamos_registrados)
                return
            case 8:
                Lector.consultar(lectores_registrados)
                return
            case 9:
                Multa.consultar(multas_registradas)
                return
            case _:
                print("El numero que digitaste es incorrecto, selecciona una opcio'n correcta!")
#menu que tiene que ver con todo sobre modificaciones               
def MenuModificar(
    articulos_registrados, 
    categorias_registradas, 
    autores_registrados, 
    tesis_registradas,
    libros_registrados,
    copias_registradas,
    prestamos_registrados,
    lectores_registrados,
    multas_registradas
):
    salir = 10
    eleccion = 0
    while(eleccion != salir):
        print("*****************************************************************************")
        print("Este es el submenu referente a modificar, elija que documento desea modificar:")
        print("     1. modificar articulo cientifico")
        print("     2. modificar libro")
        print("     3. modificar autor")
        print("     4. modificar tesis")
        print("     5. modificar categoria")
        print("     6. modificar Copia")
        print("     7. modificar Prestamo")
        print("     8. modificar lector")
        print("     9. modificar multa")
        print("     10. Salir")

        eleccion = int(input("Ingrese la opcion que desea realizar: "))
        print("*****************************************************************************")
        match eleccion:
            case 1:
                Articulo.modificar(articulos_registrados)
                return
            case 2:
                Libro.modificar(libros_registrados)
                return
            case 3:
                Autor.modificar(autores_registrados)
                return
            case 4:
                Tesis.modificar(tesis_registradas)
                return
            case 5:
                Categoria.modificar(categorias_registradas)
                return
            case 6:
                Copia.modificar(copias_registradas)
                return
            case 7: 
                Prestamo.modificar(prestamos_registrados)
                return
            case 8:
                Lector.modificar(lectores_registrados)
                return
            case 9:
                Multa.modificar(multas_registradas)
                return
            case 10:
                eleccion = salir
            case _:
                print("El numero que digitaste es incorrecto, selecciona una opcio'n correcta!")
#menu que tiene que ver con todo sobre modificaciones
def MenuEliminar(
    articulos_registrados, 
    categorias_registradas, 
    autores_registrados, 
    tesis_registradas,
    libros_registrados,
    copias_registradas,
    prestamos_registrados,
    lectores_registrados,
    multas_registradas
):
    salir = 10
    eleccion = 0
    while(eleccion != salir):
        print("*****************************************************************************")
        print("Este es el submenu referente a eliminar, elija el documento que desea eliminar:")
        print("1. eliminar articulo cientifico")
        print("2. eliminar libro")
        print("3. eliminar autor")
        print("4. eliminar tesis")
        print("5. eliminar categoria")
        print("6. eliminar Copia")
        print("7. eliminar Prestamo")
        print("8. eliminar lector")
        print("9. eliminar multa")
        print("10. Salir")

        eleccion = int(input("Ingrese la opcion que desea realizar: "))
        print("*****************************************************************************")
        match eleccion:
            case 1:
                Articulo.eliminar(articulos_registrados)
                return
            case 2:
                Libro.eliminar(libros_registrados)
                return
            case 3:
                Autor.eliminar(autores_registrados)
                return
            case 4:
                Tesis.eliminar(tesis_registradas)
                return
            case 5:
                Categoria.eliminar(categorias_registradas)
                return
            case 6:
                Copia.eliminar(copias_registradas)
                return
            case 7: 
                Prestamo.eliminar(prestamos_registrados)
                return
            case 8:
                Lector.eliminar(lectores_registrados)
                return
            case 9:
                Multa.eliminar(multas_registradas)
                return
            case 10:
                eleccion = salir
            case _:
                print("El numero que digitaste es incorrecto, selecciona una opcio'n correcta!")

def MenuOtrasOpciones(
        #si se necesitan en el futuro se dejan todas las listas
        articulos_registrados, 
        categorias_registradas, 
        autores_registrados, 
        tesis_registradas,
        libros_registrados,
        copias_registradas,
        prestamos_registrados,
        lectores_registrados,
        multas_registradas
):
    print("Bienvenido al menu de otras opciones")
    print("A continuacion se mostraran las opciones que puede realizar:")
    print("Asignaciones de categorias:")
    print("     1.asignar categoria a una tesis")
    print("     2.asignar categoria a un articulo cientifico")#funcionando
    print("     3.Asignar categoria a un libro")
    choose = int(input("Selecciona la opcion a realizar:"))

    match choose:
        case 1:
            Tesis.asignar_categoria(
                tesis_registradas,
                categorias_registradas
            )
        case 2:
            Articulo.asignar_categoria(
                categorias_registradas,
                articulos_registrados
            )
        case 3:
            Libro.asignar_categoria(
                categorias_registradas,
                libros_registrados
            )
        case _:
            print("Opcion incorrecta!")

    return



if __name__ == "__main__":
    MenuPrincipal()