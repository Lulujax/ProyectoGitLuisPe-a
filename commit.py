import datetime

class Commit:
    _id_counter = 0

    def __init__(self, archivos, mensaje, commit_anterior=None):
        # Inicializa commit con ID, archivos, mensaje y commit anterior
        self.id = Commit._id_counter
        Commit._id_counter += 1
        self.archivos = archivos
        self.mensaje = mensaje
        self.commit_anterior = commit_anterior
        self.timestamp = datetime.datetime.now()
