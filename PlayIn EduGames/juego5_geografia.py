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
            
