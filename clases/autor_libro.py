class Autor_libro:
    def __init__(self, id_autor_libro):
        self.id_autor_libro = id_autor_libro
        self.isbn = []
        self.id_autor = []
    
    @staticmethod
    def registrar():
        nueva_relacion = Autor_libro(
            id_autor_libro = int(input("Inserte el id de la relacion autor_libro:"))
        )
        return nueva_relacion
    
    def __str__(self):
        return f"|id_autor_libro::{self.id_autor_libro}|"
