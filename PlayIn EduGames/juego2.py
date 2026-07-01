import os
import random

PUNTAJES_FILE = "puntajes_animales.txt"

ANIMALES = {
    "gato": [
        "Tiene bigotes",
        "Ronronea",
        "Le gusta cazar",
        "Suele dormir muchas horas",
    ],
    "perro": [
        "Ladra",
        "Tiene cuatro patas",
        "Le gusta jugar",
        "Es muy fiel a su dueño",
    ],
    "gallina": [
        "Pone huevo",
        "Tiene plumas",
        "Le gusta comer maíz",
        "Hace \"cloc cloc\"",
    ],
    "vaca": [
        "Da leche",
        "Es grande",
        "Tiene manchas",
        "Tiene cuernos",
    ],
    "elefante": [
        "Es muy grande",
        "Tiene trompa",
        "Es herbívoro",
        "Tiene orejas enormes",
    ],
    "jirafa": [
        "Tiene el cuello muy largo",
        "Come hojas de los árboles",
        "Es la más alta de los animales terrestres",
        "Tiene manchas",
    ],
    "cebra": [
        "Tiene rayas blancas y negras",
        "Es un caballo salvaje",
        "Vive en la sabana",
        "Es herbívoro",
    ],
    "delfín": [
        "Nada rápido",
        "Vive en el agua",
        "Es muy inteligente",
        "Hace sonidos con el agua",
    ],
}


def cargar_puntajes():
    if not os.path.exists(PUNTAJES_FILE):
        return []

    puntajes = []
    with open(PUNTAJES_FILE, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if ":" not in linea:
                continue
            nombre, valor = linea.split(":", 1)
            try:
                puntaje = int(valor.strip())
            except ValueError:
                continue
            puntajes.append((nombre.strip(), puntaje))

    return sorted(puntajes, key=lambda item: item[1], reverse=True)


def guardar_puntaje(nombre, puntaje):
    with open(PUNTAJES_FILE, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre}: {puntaje}\n")


def mostrar_ranking(maximo=5):
    puntajes = cargar_puntajes()
    print("\n--- Ranking de puntajes ---")
    if not puntajes:
        print("Todavía no hay puntajes guardados.")
        return

    for indice, (nombre, puntaje) in enumerate(puntajes[:maximo], start=1):
        print(f"{indice}. {nombre} - {puntaje} puntos")

    if len(puntajes) > maximo:
        print(f"...y {len(puntajes) - maximo} puntajes más guardados.")


def pedir_nombre():
    while True:
        nombre = input("Ingresa tu nombre para guardar tu puntaje: ").strip()
        if nombre:
            return nombre
        print("El nombre no puede estar vacío. Probá de nuevo.")


def elegir_dificultad():
    while True:
        print("\nElige una dificultad:")
        print("1. Fácil (4 pistas)")
        print("2. Medio (3 pistas)")
        print("3. Difícil (2 pistas)")
        opcion = input("Seleccioná 1, 2 o 3: ").strip().lower()

        if opcion in {"1", "f", "fácil", "facil"}:
            return 4, 10, 2
        if opcion in {"2", "m", "medio"}:
            return 3, 15, 5
        if opcion in {"3", "d", "difícil", "dificil"}:
            return 2, 20, 10

        print("Opción inválida. Por favor ingresá 1, 2 o 3.")


def jugar():
    animal_secreto = random.choice(list(ANIMALES.keys()))
    pistas = ANIMALES[animal_secreto]
    intentos_maximos, puntaje_maximo, penalizacion = elegir_dificultad()
    pistas_aleatorias = random.sample(pistas, intentos_maximos)

    errores = 0
    puntaje = 0
    print("\nAdivina el animal oculto. Recibirás pistas según la dificultad elegida.")

    for intento, pista in enumerate(pistas_aleatorias, start=1):
        print(f"\nPista {intento} de {intentos_maximos}: {pista}")

        while True:
            respuesta = input("¿Qué animal crees que es?: ").strip().lower()
            if respuesta:
                break
            print("No ingresaste ninguna respuesta. Intenta otra vez.")

        if respuesta == animal_secreto:
            puntaje = puntaje_maximo - errores * penalizacion
            if puntaje < 0:
                puntaje = 0
            print(f"¡Muy bien! Adivinaste el animal. Era {animal_secreto}.")
            print(f"Puntos obtenidos: {puntaje} (Máximo {puntaje_maximo}, errores {errores})")
            break

        errores += 1
        print("No es ese animal.")

    else:
        print(f"\nPerdiste... No adivinaste. El animal era: {animal_secreto}.")
        print(f"Puntos obtenidos: 0")

    nombre = pedir_nombre()
    guardar_puntaje(nombre, puntaje)
    print(f"¡Tu puntaje fue guardado con éxito! Puntos: {puntaje}")
    mostrar_ranking()


def mostrar_menu():
    print("\n--- Menú principal ---")
    print("1. Jugar")
    print("2. Ver tabla de puntajes")
    print("3. Salir")

    return input("Elegí una opción: ").strip().lower()


if __name__ == "__main__":
    print("¡Bienvenido al juego de adivinanza de animales!")

    while True:
        opcion = mostrar_menu()

        if opcion in {"1", "jugar"}:
            jugar()
        elif opcion in {"2", "tabla", "puntajes"}:
            mostrar_ranking()
        elif opcion in {"3", "salir", "q", "quit"}:
            print("Gracias por jugar. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Elegí 1, 2 o 3.")
