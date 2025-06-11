class Autor_tesis:
    def __init__(self, id_autor_tesis):
        self.id_autor_tesis = id_autor_tesis
        self.id_autor = []
        self.id_tesis = []
    
    @staticmethod
    def registrar():
        nuevo_autor_tesis = Autor_tesis(
            id_autor_tesis = int(input("Registrar autor_tesis id:"))
        )
        return nuevo_autor_tesis

    def __str__(self):
        return f"|id_autor_tesis::{self.id_autor_tesis}|"