from commit import Commit
from rama import Rama
from archivo import Archivo

class Repositorio:
    def __init__(self):
        # Inicializa repositorio con rama 'main' y commit inicial
        archivo_lectura = Archivo("README.md", "Contenido inicial")
        commit_inicial = Commit([archivo_lectura], "Initial commit")
        self.ramas = {'main': Rama('main', commit_inicial)}
        self.rama_actual = self.ramas['main']
        self.archivos = {archivo_lectura.nombre: archivo_lectura}

    def hacer_commit(self, mensaje):
        # Crea nuevo commit en la rama actual
        archivos = list(self.archivos.values())
        nuevo_commit = Commit(archivos, mensaje, self.rama_actual.commit_actual)
        self.rama_actual.commit_actual = nuevo_commit

    def crear_rama(self, nombre):
        # Crea nueva rama con el commit actual
        nueva_rama = Rama(nombre, self.rama_actual.commit_actual)
        self.ramas[nombre] = nueva_rama

    def cambiar_rama(self, nombre):
        # Cambia a una rama existente por nombre
        if nombre in self.ramas:
            self.rama_actual = self.ramas[nombre]
        else:
            print("La rama no existe")

    def merge(self, nombre_rama):
        # Fusiona rama especificada en la rama actual
        if nombre_rama in self.ramas:
            commit_fusion = Commit(self.rama_actual.commit_actual.archivos, f"Merge branch {nombre_rama}", self.rama_actual.commit_actual)
            self.rama_actual.commit_actual = commit_fusion
        else:
            print("La rama no existe")

    def mostrar_historial(self):
        # Muestra historial de commits de la rama actual
        commit = self.rama_actual.commit_actual
        while commit is not None:
            print(f"Commit ID: {commit.id}, Mensaje: {commit.mensaje}, Timestamp: {commit.timestamp}")
            commit = commit.commit_anterior

    def agregar_archivo(self, nombre, contenido):
        # Agrega nuevo archivo al repositorio
        nuevo_archivo = Archivo(nombre, contenido)
        self.archivos[nombre] = nuevo_archivo
