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
    
