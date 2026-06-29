def jugar_simon():
    
    import subprocess   #libreria para borrar la pantalla
    import time # libreria para pausar antes de borrar (time.sleep)
    import random # libreria para tomar valores aleatorios y q cada secuencia sea diferente
    
    # 1. Funcion para limpiar la pantalla.
    def limpiar_pantalla():
        subprocess.run("cls", shell=True)
    
    # 2. guardar el puntaje de cada juagador
    def guardar_puntaje(nombre, ronda):
        # "a" abre el archivo para agregar texto sin borrar lo anterior
        with open("rankingSimon.txt", "a") as archivo:
            archivo.write(f"{nombre} - Ronda: {ronda}\n")
        print("¡Puntaje guardado con éxito!")
    
    # 3. Función para mostrar el ranking
    def ver_ranking():
        limpiar_pantalla()
        print("=== TABLA DE POSICIONES ===")
        try:
            with open("rankingSimon.txt", "r") as archivo:
                contenido = archivo.read()
                if contenido == "":
                    print("Aún no se han registrado puntajes.")
                else:
                    print(contenido)
        except FileNotFoundError:
            print("Aún no se han registrado puntajes.")
        
        input("\nPresiona Enter para volver al menú...")

# 4. Función principal "el juego"
def jugar():
    limpiar_pantalla()
    nombre = input("Ingresa tu nombre: ")
    
    opciones = ['A', 'B', 'C', 'D'] # Lista con las opciones para la secuencia
    secuencia = []
    jugando = True
    ronda = 1
    
    while jugando:
        limpiar_pantalla()
        print(f"--- RONDA {ronda} ---")
        time.sleep(1)
        
        
        secuencia.append(random.choice(opciones)) # Agrega un la letra random a la lista
        
        # Muestra la secuencia en pantalla
        print("Simón dice: ", end="") #el end es para que no haga salto de línea
        for elemento in secuencia:
            print(elemento, end=" ")
        print() # Salto de línea
        
        # Espera 2 segundos y borra la pantalla para que el usuario no copie
        time.sleep(2)
        limpiar_pantalla()
        
        # Turno del jugador
        print("¡Tu turno! Ingresa la secuencia separada por espacios (Ej: A B C):")
        entrada_usuario = input("> ").upper() # .upper() pasa todo a mayúsculas
        secuencia_usuario = entrada_usuario.split() # Convierte el texto en una lista
        
        # condicion para ver si el usuario acertó o no
        if secuencia_usuario == secuencia:
            print("\n¡Correcto! Prepárate para la siguiente ronda.")
            ronda += 1
            time.sleep(1.5)
        else:
            print(f"\nX ¡MAL! La secuencia correcta era: {secuencia}")
            print(f"Al menos llegaste hasta la ronda {ronda}.")
            guardar_puntaje(nombre, ronda)
            
            # opciones para cuando perdes
            while True:
                print("\n¿Qué deseas hacer?")
                print("1. Intentarlo otra vez (Jugar de nuevo)")
                print("2. Volver al menú principal")
                print("3. Salir del programa")
                
                rta = input("Selecciona una opción: ")
                
                if rta == "1":
                    # Reset del juego y volvemos a empezar desde la ronda 1
                    secuencia = []
                    ronda = 1
                    limpiar_pantalla()
                    print("¡Arrancamos de nuevo! Suerte...")
                    time.sleep(1.5)
                    break 
                    
                elif rta == "2":
                    
                    print("Volviendo al menú principal de la arcada...")
                    jugando = False 
                    break 
                    
                elif rta == "3": # por si ya no quiere juhar y cierra todo
                    
                    print("¡Gracias por jugar! Adiós.")
                    exit()
                    
                else:
                    print("Opción inválida. Por favor, elige 1, 2 o 3.")
                    time.sleep(1.5)
                    limpiar_pantalla()

# 5. Menú Principal del programa
def menu():
    while True:
        limpiar_pantalla()
        print("===============================")
        print("     BIENVENIDO A SIMÓN DICE   ")
        print("===============================")
        print("1. Jugar")
        print("2. Ver Ranking (Manejo de Archivos)")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            jugar()
        elif opcion == "2":
            ver_ranking()
        elif opcion == "3":
            print("¡Gracias por jugar! Adiós.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
            time.sleep(1.5)


def iniciar_juego(): # funcion para que corra el juego desde otro archivo
        menu()

if __name__ == "__main__":     # funcion para que corra el juego desde este archivo

    menu()

