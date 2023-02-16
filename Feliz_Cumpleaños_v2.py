# Feliz_Cumpleaños.py
import time
import random

# Mensaje de bienvenida
print("Hola Bitran. Te he enviado este archivo especial porque hoy es tu cumpleaños y quiero desearte lo    .")
print("Pero no creas que te voy a regalar algo tan fácilmente. Tendrás que demostrar que eres digno de recibirlo superando un desafío.")
print("El desafío consiste en escribir sobre un tema que te apasione lo más rápido y sin errores posible. Sé que eres muy bueno en esto, así que no te lo pondré fácil.")
print("Debes alcanzar una velocidad mínima de 40 wpm y cometer como máximo 3 errores para lograr tu objetivo.")
print()
# Establecer un umbral mínimo de velocidad y máximo de errores para superar el desafío
velocidad_minima = 40 # wpm
errores_maximos = 3

# Crear una variable para controlar si el usuario ha superado el desafío o no
superado = False

# Crear un bucle while que se repita hasta que el usuario supere el desafío
while not superado:

    # Crear el texto a escribir con palabras aleatorias de la lista
    lista = ["bitri", "blitzcrank", "super red del bitran", "bitri el tocino", "du hast", "ecuestre", "aviso!", "la rueda nunca deja de girar", "chachis gaming chile"]
    texto = ""
    for i in range(5):
        palabra = random.choice(lista)
        texto += palabra + " "
    print(f"El texto a escribir es: {texto}")

    print("¿Estás listo? Presiona ENTER para comenzar o CTRL+C para salir.")
    input()

    # Iniciar el cronómetro y pedir al usuario que escriba el texto
    tiempo_inicial = time.time()
    texto_usuario = input("Escribe el texto aquí: ")
    tiempo_final = time.time()

    # Cálculos de velocidad y errores
    duracion = tiempo_final - tiempo_inicial
    palabras = len(texto_usuario.split())
    wpm = palabras / (duracion / 60)
    errores = 0
    for i in range(min(len(texto), len(texto_usuario))):
        if texto[i] != texto_usuario[i]:
            errores += 1
    errores += abs(len(texto) - len(texto_usuario))

    # Mostrar los resultados al usuario
    print(f"Has escrito {palabras} palabras en {duracion:.2f} segundos.")
    print(f"Tu velocidad ha sido de {wpm:.2f} palabras por minuto.")
    print(f"Has cometido {errores} errores.")
    print()

    
   
    # Comprobar si el usuario ha superado el desafío o no
   
    if wpm >= velocidad_minima and errores <= errores_maximos:
       print("¡Bravo! Has superado el desafío con éxito. Sabía que podías hacerlo. Tu regalo es una suscripción de 1 mes en brilliant.com, la mejor plataforma para aprender ciencia y matemáticas. Sé que te encantará.")
       superado = True # Cambiar la variable a True para salir del bucle while
   
    else:
       print("Vaya, no has superado el desafío. No pasa nada, sé que lo puedes conseguir. Inténtalo de nuevo tantas veces como quieras.") 