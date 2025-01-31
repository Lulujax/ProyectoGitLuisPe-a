class Archivo:
    def __init__(self, nombre, contenido):
        # Inicializa nombre y contenido del archivo
        self.nombre = nombre
        self.contenido = contenido

    def leer(self):
        # Retorna el contenido del archivo
        return self.contenido

    def escribir(self, nuevo_contenido):
        # Actualiza el contenido del archivo
        self.contenido = nuevo_contenido
