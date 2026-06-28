

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
        import datetime # Necesario para la fecha del reporte 
        
        
        """
        Normaliza el texto, elimina acentos y convierte a minúsculas para una comparación robusta.
        Recibe: cadena de texto (str).
        Retorna: cadena de texto normalizada (str).
        """
        
        
        NOMBRE_ARCHIVO = "./ranking_geografia.csv"
        ENCABEZADO = "Nombre;puntos"
        NOMBRE_REPORTE = "reporte_ganadores.txt"
        
        
        
        
    
        
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
           
            """Asegura la persistencia creando el archivo CSV ."""
        try:
            
            archivo = open(NOMBRE_ARCHIVO, "x", encoding="utf-8")
            archivo.write(ENCABEZADO + "\n")
            archivo.close()
            
        except FileExistsError:   #Si el archivo ya existe, no hacemos nada 
            pass
        
        
        
        
        
        # Función para grabar el puntaje del jugador en el archivo CSV
        
        def grabar_puntaje_nuevo(nombre, puntos):
            
            """
            Agrega una nueva línea al archivo CSV con el nombre del jugador y su puntaje obtenido [5].
            Recibe: nombre (str) y puntos (int).
            """
            
            try:
                
                archivo = open(NOMBRE_ARCHIVO, "a", encoding="utf-8") # encoding para evitar problemas con acentos, lo que hace es que Python entienda que el archivo es UTF-8 y pueda manejar caracteres especiales
                linea = f"{nombre};{puntos}" # Ahora Python entiende que esto es parte de la función
                archivo.write(linea + "\n")
                archivo.close()
                
            except Exception as error: # Si ocurre un error al grabar, lo mostramos en pantalla
                print("Error al grabar:", error)
        
        
        
        
        
        # Función para mostrar el top 10 del ranking, ordenando los puntajes de mayor a menor
        
        def mostrar_top_10():
            
            """
            Lee el archivo de ranking, procesa los datos y utiliza el método de burbuja 
            para ordenar y mostrar los 10 mejores puntajes .
            """
            
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

                
                # Algoritmo de Burbuja: Ordenamos de Mayor a Menor 
                
                n = len(ranking)
                
                for i in range(n - 1):
                    
                    for j in range(n - 1 - i):
                        
                        if ranking[j]["Puntos"] < ranking[j+1]["Puntos"]:
                            
                            # Intercambio de diccionarios
                            aux = ranking[j]
                            ranking[j] = ranking[j+1]
                            ranking[j+1] = aux
                
                
                #exportamos el top 10 del ranking a .txt
                
                exportar_reporte_txt(ranking) 
                
                print("\n" + "="*35)
               
                print("🏆 TOP 10 RANKING MUNDIALISTA 🏆")
                
                print("="*35)
              
                for k in range(min(10, len(ranking))):
                   
                    print(f"{k+1}. {ranking[k]['Nombre']} - {ranking[k]['Puntos']} aciertos")
                
                print("="*35)

            except FileNotFoundError:
                print("\n[!] Aún no hay puntajes registrados.")
        
        
        
        # Función para exportar el podio de ganadores a un archivo de texto
       
        def exportar_reporte_txt(ranking_ordenado):
           
            """
            Genera un archivo de texto con el podio de los ganadores y la fecha actual.
            Recibe: lista de diccionarios (ranking) ya ordenada.
            """
            
            try:
                
                # Obtenemos la fecha y hora actual como en el ejemplo del profe [2]
                fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                
                archivo = open(NOMBRE_REPORTE, "w", encoding="utf-8")
                
                # Diseño "lindo" del reporte
                archivo.write("==========================================\n")
                archivo.write("      REPORTE DE GANADORES - MUNDIAL 2026\n")
                archivo.write("==========================================\n")
                archivo.write(f"Emisión: {fecha}\n\n")
                archivo.write("🏆 EL PODIO DE LOS CAMPEONES 🏆\n")
                archivo.write("------------------------------------------\n")
                
                # Limitamos al Top 3 para el podio o mostramos lo que haya
                for i in range(min(3, len(ranking_ordenado))):
                    puesto = i + 1
                    nombre = ranking_ordenado[i]["Nombre"]
                    puntos = ranking_ordenado[i]["Puntos"]
                    archivo.write(f"Puesto {puesto}: {nombre} con {puntos} aciertos\n")
                
                archivo.write("------------------------------------------\n")
                archivo.write("\n¡Felicitaciones a los mejores geógrafos!\n")
                archivo.write("Plataforma Play.In EduGames\n")
                
                archivo.close()
                print(f"\n✅ Reporte exportado con éxito como '{NOMBRE_REPORTE}'")
                
            except Exception as e:
                print(f"Error al generar el reporte: {e}")
            
        
        
        
        # Función principal del juego de geografía    
        
        def jugar_geografia():
            """
            Función principal de la actividad de Geografía. Controla el flujo del juego, 
            la validación de respuestas y la actualización del ranking.
            """
            crear_ranking_si_no_existe()
        
        
        print("\n" + "*"*50)
        print(" ⚽ BIENVENIDO AL DESAFÍO MUNDIALISTA 2026 ⚽ ")
        print("*"*50)
        
        
        # Nombre del jugador para el ranking, con validación de entrada
        nombre = input("Ingresá tu nombre para el ranking: ").strip()
        if not nombre: nombre = "Jugador Anónimo"
        
        
        # Acentos y mayúsculas no afectarán la comparación de respuestas, gracias a la función limpiar_texto()
        aciertos = 0
        paises = list(paises_mundial.keys())
        random.shuffle(paises) # Mezclamos para que cada partida sea distinta
        
        
        
        
        # Función para limpiar y normalizar el texto ingresado por el usuario
        def limpiar_texto(texto):
            
            """Normaliza, quita acentos y pasa a minúsculas."""
            # 1. Normalizamos (separa la letra del acento)
            texto_descompuesto = unicodedata.normalize('NFD', texto)
            # 2. Filtramos: mantenemos solo los caracteres que NO sean acentos (categoría 'Mn')
            texto_sin_acentos = "".join(c for c in texto_descompuesto if unicodedata.category(c) != 'Mn')
            # 3. Pasamos a minúsculas y quitamos espacios extra para máxima robustez 
            return texto_sin_acentos.strip().lower()

        
        # Bucle de preguntas: el jugador debe adivinar el continente de cada país
        
        for pais in paises:
            
            print(f"\nPaís: {pais}")
            continente_usuario = input("¿A qué continente pertenece? ")
            continente_correcto = paises_mundial[pais]

            
            # COMPARA USANDO LA FUNCIÓN DE LIMPIEZA
            
            if limpiar_texto(continente_usuario) == limpiar_texto(continente_correcto):
                
                aciertos += 1
                print(f"✅ ¡Correcto! Llevás {aciertos} aciertos.")
            else:
                
                print(f"❌ ¡Incorrecto! {pais} pertenece a {paises_mundial[pais]}.")
                break
        
        # Grabamos el puntaje del jugador en el ranking
        grabar_puntaje_nuevo(nombre, aciertos)
        
            

    
        # Fin del juego y agradecimiento al jugador
        
        
        # Mostrar el ranking actualizado
        mostrar_top_10()
        
        
        #preguntamos si quiere volver a jugar o salir
        jugar = input("\n¿Querés volver a jugar? (s/n): ").strip().lower()
        
        if jugar != "s":
            
            print("\n¡Gracias por jugar! ¡Hasta la próxima!")
            break
        else:
            
            print("\n¡Genial! Reiniciando el juego...\n")
            jugar = 0  # Reiniciamos la variable para continuar el bucle
            
