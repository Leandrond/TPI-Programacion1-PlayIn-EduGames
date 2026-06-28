# Juego de Geografía Mundialista 2026

def jugar_geografia():
    
    # while para permitir que el jugador vuelva a jugar si lo desea
    jugar=0
    while jugar==0:
        
        print("¡Bienvenido al juego de Geografía!")
        # Inicio del juego de geografía
        
        
        #importamos la librerias
        import random # Para mezclar la lista de países y hacer el juego más dinámico
        import unicodedata  # Para normalizar acentos y diéresis
        
        
        # Definimos constantes para el nombre del archivo y el encabezado del CSV dentro de la carpeta PlayIn EduGames
        # con el ./ para que busque en la carpeta actual y no en otra ubicación
        NOMBRE_ARCHIVO = "./ranking_geografia.csv"
        ENCABEZADO = "Nombre;puntos"
        
        # diccionario de países y sus continentes clasificados en el mundial 2026
        paises_mundial = {
            # --- AMÉRICA (CONMEBOL y CONCACAF) ---
            "Canadá": "América",
            "México": "América",
            "Estados Unidos": "América",
            "Argentina": "América",
            "Brasil": "América",
            "Colombia": "América",
            "Ecuador": "América",
            "Paraguay": "América",
            "Uruguay": "América",
            "Curazao": "América",
            "Haití": "América",
            "Panamá": "América",

            # --- EUROPA (UEFA) ---
            "Alemania": "Europa",
            "Austria": "Europa",
            "Bélgica": "Europa",
            "Bosnia": "Europa",
            "Croacia": "Europa",
            "Escocia": "Europa",
            "España": "Europa",
            "Francia": "Europa",
            "Inglaterra": "Europa",
            "Noruega": "Europa",
            "Países Bajos": "Europa",
            "Portugal": "Europa",
            "República Checa": "Europa",
            "Suecia": "Europa",
            "Suiza": "Europa",
            "Turquía": "Europa",

            # --- ASIA (AFC) ---
            "Australia": "Asia", # Compite en la confederación asiática
            "Irán": "Asia",
            "Japón": "Asia",
            "Jordania": "Asia",
            "Corea del Sur": "Asia",
            "Catar": "Asia",
            "Arabia Saudí": "Asia",
            "Uzbekistán": "Asia",
            "Irak": "Asia",

            # --- ÁFRICA (CAF) ---
            "Argelia": "África",
            "Cabo Verde": "África",
            "Costa de Marfil": "África",
            "Egipto": "África",
            "Ghana": "África",
            "Marruecos": "África",
            "Senegal": "África",
            "Sudáfrica": "África",
            "Túnez": "África",
            "Congo": "África",

            # --- OCEANÍA (OFC) ---
            "Nueva Zelanda": "Oceanía"
        }
        
        # Funcion para crear el archivo de ranking si no existe, asegurando la persistencia de datos
        def crear_ranking_si_no_existe():
            """Asegura la persistencia creando el archivo CSV [6, 7]."""
        try:
            archivo = open(NOMBRE_ARCHIVO, "x", encoding="utf-8")
            archivo.write(ENCABEZADO + "\n")
            archivo.close()
        except FileExistsError:   #Si el archivo ya existe, no hacemos nada 
            pass
        
        # Función para grabar el puntaje del jugador en el archivo CSV
        def grabar_puntaje_nuevo(nombre, puntos):
            """Graba los datos usando el separador punto y coma."""
            try:
                archivo = open(NOMBRE_ARCHIVO, "a", encoding="utf-8") # encoding para evitar problemas con acentos, lo que hace es que Python entienda que el archivo es UTF-8 y pueda manejar caracteres especiales
                linea = f"{nombre};{puntos}" # Ahora Python entiende que esto es parte de la función
                archivo.write(linea + "\n")
                archivo.close()
            except Exception as error: # Si ocurre un error al grabar, lo mostramos en pantalla
                print("Error al grabar:", error)
# Función para mostrar el top 10 del ranking, ordenando los puntajes de mayor a menor
        def mostrar_top_10():
            """Lee, ordena por burbuja y muestra los mejores puntajes."""
            ranking = []
            try:
                archivo = open(NOMBRE_ARCHIVO, "r", encoding="utf-8")
                lineas = archivo.readlines() # Hace que leamos de a líneas, lo que nos permite procesar cada línea del archivo mejor
                archivo.close()

                # Procesamos los datos saltando el encabezado
                for i in range(1, len(lineas)):
                    datos = lineas[i].strip().split(";")
                    if len(datos) == 2:
                        # Corregido: Nombre es datos y Puntos es datos
                        ranking.append({"Nombre": datos[0], "Puntos": int(datos[1])})

                # Algoritmo de Burbuja: Ordenamos de Mayor a Menor [9]
                n = len(ranking)
                for i in range(n - 1):
                    for j in range(n - 1 - i):
                        if ranking[j]["Puntos"] < ranking[j+1]["Puntos"]:
                            # Intercambio de diccionarios
                            aux = ranking[j]
                            ranking[j] = ranking[j+1]
                            ranking[j+1] = aux

                print("\n" + "="*35)
                print("🏆 TOP 10 RANKING MUNDIALISTA 🏆")
                print("="*35)
                for k in range(min(10, len(ranking))):
                    print(f"{k+1}. {ranking[k]['Nombre']} - {ranking[k]['Puntos']} aciertos")
                print("="*35)

            except FileNotFoundError:
                print("\n[!] Aún no hay puntajes registrados.")
            
         # Función principal del juego de geografía    
         def jugar_geografia():
            """Función principal que integra la lógica del juego ."""
            crear_ranking_si_no_existe()
        
        
        print("\n" + "*"*45)
        print("  BIENVENIDO AL DESAFÍO GEOGRÁFICO 2026  ")
        print("*"*45)
        
        
        # Nombre del jugador para el ranking, con validación de entrada
        nombre = input("Ingresá tu nombre para el ranking: ").strip()
        if not nombre: nombre = "Jugador Anónimo"
            
