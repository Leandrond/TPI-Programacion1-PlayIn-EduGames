
import random

ARCHIVO = "puntajes.txt"

# ── Lista de diccionarios: cada adivinanza tiene enunciado, 2 pistas y respuesta ──
# Se usa lista de diccionarios porque cada adivinanza tiene varios datos relacionados.
ADIVINANZAS = [
    {
        "enunciado": "Tengo el doble de dedos que una mano, más 3. ¿Cuánto soy?",
        "pistas": ["Soy mayor que 10.", "Soy impar y estoy entre 12 y 14."],
        "respuesta": 13
    },
    {
        "enunciado": "Si me multiplicás por 3 y le restás 6, obtenés 12. ¿Quién soy?",
        "pistas": ["Soy un número par.", "Soy mayor que 4 y menor que 8."],
        "respuesta": 6
    },
    {
        "enunciado": "Soy el número que está justo en el medio entre 14 y 20. ¿Quién soy?",
        "pistas": ["Soy impar.", "Soy mayor que 16 y menor que 18."],
        "respuesta": 17
    },
    {
        "enunciado": "Hay 5 filas de sillas con 7 sillas cada una. ¿Cuántas sillas hay en total?",
        "pistas": ["Es una multiplicación.", "El resultado está entre 30 y 40."],
        "respuesta": 35
    },
    {
        "enunciado": "Una araña tiene 8 patas. ¿Cuántas patas tienen 4 arañas?",
        "pistas": ["Multiplicá la cantidad de patas por la cantidad de arañas.", "El resultado está entre 30 y 35."],
        "respuesta": 32
    },
    {
        "enunciado": "Soy un número par. Si me dividís por 2 obtenés 7. ¿Quién soy?",
        "pistas": ["Soy mayor que 10.", "Tengo un 4 en la cifra de las unidades."],
        "respuesta": 14
    },
    {
        "enunciado": "Hay 30 alumnos en clase. Se van 8 y llegan 5 nuevos. ¿Cuántos hay ahora?",
        "pistas": ["Primero restá, después sumá.", "El resultado está entre 25 y 30."],
        "respuesta": 27
    },
    {
        "enunciado": "Un cuadrado tiene 4 lados iguales. Si su perímetro es 20, ¿cuánto mide cada lado?",
        "pistas": ["Tenés que dividir el perímetro entre la cantidad de lados.", "El resultado es menor que 10."],
        "respuesta": 5
    },
    {
        "enunciado": "Si sumás todos los números del 1 al 4, ¿qué número obtenés?",
        "pistas": ["Son solo 4 sumas sencillas.", "El resultado termina en cero."],
        "respuesta": 10
    },
    {
        "enunciado": "Si a un número le sumás 8 obtenés 20. ¿Quién soy?",
        "pistas": ["Soy mayor que 10.", "Soy par y estoy entre 11 y 13."],
        "respuesta": 12
    }
]


# ── Función 1: guarda el puntaje en el archivo ──
def guardar_puntaje(nombre, puntaje):
    f = open(ARCHIVO, "a", encoding="utf-8")
    f.write(nombre + "," + str(puntaje) + "\n")
    f.close()


# ── Función 2: lee el archivo y muestra los puntajes ──
def mostrar_ranking():
    try:
        f = open(ARCHIVO, "r", encoding="utf-8")
        lineas = f.readlines()
        f.close()
    except FileNotFoundError:
        print("  Todavía no hay puntajes guardados.")
        return

    print("\n   RANKING — OLIMPIADAS MATEMÁTICAS")
    print("  " + "-" * 35)
    for linea in lineas:
        partes = linea.strip().split(",")
        print(f"  {partes[0]} — {partes[1]} pts")
    print("  " + "-" * 35)


# ── Función 3: lógica de una partida completa ──
def jugar_ronda(nombre):
    puntaje_total = 0

    # Elige 5 adivinanzas al azar sin repetir
    seleccion = random.sample(ADIVINANZAS, 5)

    print(f"\n  ¡Buena suerte, {nombre}!")
    print("  Sin pistas: 20 pts  |  1 pista: 15 pts  |  2 pistas: 10 pts\n")

    for i, adiv in enumerate(seleccion, 1):
        puntos = 20
        pistas_usadas = 0

        print("  " + "-" * 40)
        print(f"  Adivinanza {i}/5:")
        print(f"  {adiv['enunciado']}\n")

        while True:
            print(f"  Puntos disponibles: {puntos}")
            print("  1 - Responder")
            if pistas_usadas < 2:
                print(f"  2 - Pedir pista {pistas_usadas + 1}  (-5 pts)")

            opcion = input("\n  Tu opción: ")

            if opcion == "1":
                try:
                    intento = int(input("  Tu respuesta: "))
                except ValueError:
                    print("    Ingresá un número.")
                    continue

                if intento == adiv["respuesta"]:
                    print(f"   ¡Correcto! +{puntos} puntos")
                    puntaje_total += puntos
                else:
                    print(f"   Era {adiv['respuesta']}. +0 puntos")
                break

            elif opcion == "2" and pistas_usadas < 2:
                pistas_usadas += 1
                puntos -= 5
                print(f"\n   Pista {pistas_usadas}: {adiv['pistas'][pistas_usadas - 1]}\n")

            else:
                print("    Opción no válida.")

    print("\n  " + "=" * 40)
    print(f"  Puntaje final de {nombre}: {puntaje_total}/100")

    if puntaje_total == 100:
        print("   ¡PERFECTO! ¡Sos un campeón olímpico!")
    elif puntaje_total >= 70:
        print("   ¡Muy bien! ¡Medalla de plata!")
    elif puntaje_total >= 40:
        print("   ¡Buen intento! ¡Medalla de bronce!")
    else:
        print("   ¡Seguí practicando!")

    print("  " + "=" * 40)
    return puntaje_total


# ── Función 4: menú del juego ──
def juego_matematicas():
    while True:
        print("\n" + "=" * 45)
        print("     OLIMPIADAS MATEMÁTICAS  ")
        print("=" * 45)
        print("  1 - Jugar")
        print("  2 - Ver Ranking")
        print("  3 - Volver al menú principal")
        print("=" * 45)

        opcion = input("  Tu opción: ")

        if opcion == "1":
            nombre = input("\n  ¿Cómo te llamás? ").strip()
            if nombre == "":
                print("    Ingresá tu nombre.")
                continue
            puntaje = jugar_ronda(nombre)
            guardar_puntaje(nombre, puntaje)
            print("  ¡Puntaje guardado!")

        elif opcion == "2":
            mostrar_ranking()

        elif opcion == "3":
            break

        else:
            print("    Opción no válida.")
