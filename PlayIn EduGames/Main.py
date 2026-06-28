#En este archivo creamos un meno para poden ingresar a los demas juego e ir navegando 
def main():
    # Aquí irá el código del menú principal
     
    opcion = ""
    
    # 2. Estructura Repetitiva: El bucle principal
    while opcion != "0":
        # Mostramos el menú con un formato claro (valorado en el punto 7 del TPI)
        print("\n" + "*" * 50)
        print("          BIENVENIDOS A PLAY.IN EDUGAMES          ")
        print("*" * 50)
        print("1 - Juego de Lengua")
        print("2 - Juego de Matemática")
        print("3 - Juego de Ciencias")
        print("4 - Juego de Historia")
        print("5 - Juego de Geografía")
        print("0 - Salir")
        print("*" * 50)
        
        opcion = input("Ingresa tu opción: ")
    
    # if para cada opción, llamamos a la función correspondiente del juego
    if opcion == "1":
        print("Entrando al juego 1...")
        # Aquí llamarías a la función de ese juego
    elif opcion == "2":
        print("Entrando al juego 2...")
        # Aquí llamarías a la función de ese juego
    elif opcion == "3":
        print("Entrando al juego 3...")
        # Aquí llamarías a la función de ese juego
    elif opcion == "4":
        print("Entrando al juego 4...")
        # Aquí llamarías a la función de ese juego
    elif opcion == "5":
        print("Entrando al juego 5...")
        # Aquí llamarías a la función de ese juego
    elif opcion == "0":
        print("Saliendo del sistema...")
    else:
        print("Opción no válida, intentá de nuevo.") # Para evitar errores, si el usuario ingresa una opción no válida, se le pedirá que intente de nuevo. 

