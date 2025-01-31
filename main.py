from repositorio import Repositorio
def main():
    # Inicializar el repositorio
    repo = Repositorio()

    # Agregar archivos y hacer commits
    repo.hacer_commit("Initial commit")

    # Crear una nueva rama y trabajar en ella
    repo.crear_rama("develop")
    repo.cambiar_rama("develop")
    repo.agregar_archivo("nuevo_archivo.txt", "Contenido del nuevo archivo")
    repo.hacer_commit("Added new feature")

    # Cambiar a la rama principal y hacer un merge
    repo.cambiar_rama("main")
    repo.merge("develop")

    # Mostrar el historial de commits
    repo.mostrar_historial()
main()