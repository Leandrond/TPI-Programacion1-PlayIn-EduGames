def main():
    # 1. Inicialización el menu con una funcion

        
    #5. Importacion de juegos 
    #Esto permite una mejor comprension del codigo y una mejor organizacion de los archivos
    import juego5_geografia  # Esto conecta main.py con juego5_geografia.py
    import juego4_Simon  # Esto conecta main.py con juego4_Simon.py
    import juego3_adivinanza.py    # Esto conecta main.py con juego3_adivinanza.py
    opcion = ""
    
    # 2. Bucle principal del menú
    while opcion != "0":
        print("\n" + "*" * 50)
        print("          BIENVENIDOS A PLAY.IN EDUGAMES          ")
        print("*" * 50)
        print("1 - Juego de Lengua")
        print("2 - Juego de Ciencias")
        print("3 - Juego de Matematica")
        print("4 - Juego de Historia")
        print("5 - Juego de Geografía")
        print("0 - Salir")
        print("*" * 50)
        
        opcion = input("Ingresa tu opción: ")
        
        # 3. Seleccion de juegos 
        if opcion == "1":
            print("\n--- Entrando al Juego 1 ---")
            # juego_lengua() # Llamamos a la función del juego
            input("Presiona Enter para volver al menú...")
            
        elif opcion == "2":
            print("\n--- Entrando al Juego 2 ---")
            # juego_matematica()
            input("Presiona Enter para volver al menú...")
            
        elif opcion == "3":
            print("\n--- Entrando al Juego 3 ---")
            juego3_adivinanza.juego_matematicas()
            input("Presiona Enter para volver al menú...")
            
        elif opcion == "4":
            print("\n--- Entrando al Juego 4 ---")
            juego4_Simon.jugar_simon()
            input("Presiona Enter para volver al menú...")
            
        elif opcion == "5":
            print("\n--- Entrando al Juego 5 ---")
            juego5_geografia.jugar_geografia() 
            input("Presiona Enter para volver al menú...")
            
        elif opcion == "0":
            print("\nSaliendo del sistema... ¡Gracias por jugar!")
            
        else:
            # 4. Validación de entradas no válidas
            print("\n[!] Opción no válida. Por favor, ingresa un número del 0 a 5.")
                  
# entrada principal del programa
if __name__ == "__main__": # Verifica si el script se está ejecutando directamente
    main()
