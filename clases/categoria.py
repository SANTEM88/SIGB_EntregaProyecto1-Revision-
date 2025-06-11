class Categoria:
    def __init__(self, id_categoria, nombre, descripcion):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.descripcion = descripcion
        self.subcategoria = []
    
    #crear un nuevo articulo
    @staticmethod
    def registrar():
        nueva_categoria = Categoria(
            id_categoria = int(input("Inserte el id de la nueva categoria: ")),
            nombre = input("Inserte el nombre de la categoria: ").upper(),
            descripcion = input("Inserte la descripcion de la categoria: ").upper(),
        )
        if not nueva_categoria.subcategoria: #esta vacia?
            print("Aun no se ha creado una subcategoria, cree subcategorias")
            cantidad = int(input("Escriba el numero de subcategorias que quiere anyadir: "))
            i = 0
            while i != cantidad:
                subcategoria = input("Escriba la subcategoria: ")
                nueva_categoria.subcategoria.append(subcategoria)
                i = i + 1

        return nueva_categoria
    
    #consultar categorias
    @staticmethod
    def consultar(lista_categorias):
        id = int(input("Inserte el id de la categoria que desea consultar: "))
        for categoria in lista_categorias:
            if id == categoria.id_categoria:
                print(categoria)
                return
        print("Categoria no encontrada")

    #modificar categorias
    @staticmethod
    def modificar(lista_categorias):
        id = int(input("Inserta el id de la categoria a eliminar: "))
        for categoria in lista_categorias:
            if id == categoria.id_categoria:
                eleccion = int(input("Estas seguro de modificar la categoria? Si(1) No(2): "))
                if eleccion == 1:
                    print("***************************")
                    print("Elija la opcion de acuerdo a lo que desea modificar:")
                    print("1. Modificar el nombre de la categoria")
                    print("2. Modificar la descripcion de la categoria")
                    choose = int(input("Elija la opcion a modificar: "))
                    match choose:
                        case 1:
                            categoria.nombre = input("Ingrese el nuevo nombre: ")
                            print("Exito!")
                            return
                        case 2:
                            categoria.descripcion = input("Ingrese la nueva descripcion: ")
                            print("Exito!")
                            return
                        case _:
                            print("Opcion incorrecta regresando al menu principal...")
        print("No se realizaron cambios!")

        return
    # "eliminar" categoria
    @staticmethod
    def eliminar(lista_categorias):
        id = int(input("Ingrese la id de la categoria a ser eliminada: "))
        for categoria in lista_categorias:
            if categoria.id_categoria == id:
                lista_categorias.remove(categoria)
                print("Eliminada con exito!")
                return
        print("No existe la categoria ingresada")
        return

    def __str__(self):
        return f"| id categoria: {self.id_categoria}| nombre: {self.nombre}| descripcion: {self.descripcion}|"