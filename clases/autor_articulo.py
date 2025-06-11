class Autor_articulo:
    def __init__(self, id_autor_articulo):
        self.id_autor_articulo = id_autor_articulo
        self.id_autor = []
        self.id_articulo = []
    
    @staticmethod
    def registrar():
        nuevo_registrar = Autor_articulo(
            id_autor_articulo = int(input("Elija el id de la relacion de autor y articulo")),
        )
        return nuevo_registrar

    def __str__(self):
        return f"|id articulo_autor::{self.id_autor_articulo}|"