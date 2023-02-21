# coding=utf-8
"""
Feliz_Cumpleaños.py
Creado en colaboracion entre Sat + BingAI.
"""

import time
import random

# Mensaje de bienvenida
print()
print("Hola Bitran. Te he enviado este archivo especial porque hoy es tu cumpleaños y te tengo un regalo")
time.sleep(2)
print("Pero no creas que te voy a regalar algo tan fácilmente. Tendrás que demostrar que eres digno de recibirlo superando un desafío.")
time.sleep(2)
print("El desafío consiste en un TypeRacer personalizado. Tienes que escribir lo mismo que te va a salir en pantalla lo más rápido posible y sin errores.")
time.sleep(2)
print("Debes alcanzar una velocidad mínima de 40 wpm y la menora cantidad de errores para lograr tu objetivo.")
print()
time.sleep(2)

# Establecer un umbral mínimo de velocidad y máximo de errores para superar el desafío
velocidad_minima = 40 # wpm
errores_maximos = 10

# Crear un bucle while que se repita hasta que el usuario supere el desafío
superado = False
primero = True
while not superado:
    if not primero:
        input("Presiona ENTER para volver a intentarlo.")
        print()
        print()
        print()
    primero = False

    # Crear el texto a escribir con palabras aleatorias de la lista
    lista = ["bitri", "blitzcrank", "super red del bitran", "bitri el tocino", "du hast", "ecuestre", "aviso!", "la rueda nunca deja de girar", "chachis gaming chile"]
    random.shuffle(lista)
    texto = ""
    for i in lista:
        texto += i + " "

    print(f"El texto a escribir es:")
    print("-----------------------------------------------------------------")
    print(texto)
    print("-----------------------------------------------------------------")
    print()
    print("Debes escribirlo tal cual aparece y finalizas aprentando ENTER.")
    print("¿Estás listo? Presiona ENTER para comenzar (o CTRL+C para salir).")
    input()

    # Iniciar el cronómetro y pedir al usuario que escriba el texto
    tiempo_inicial = time.time()
    print("¡Empieza a escribir!")
    print()
    print("-----------------------------------------------------------------")
    texto_usuario = input()
    print("-----------------------------------------------------------------")
    print()
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
        print("¡GRAAANNDEEEEE WNNN! Has superado el desafío con éxito.")
        print("Tu regalo es una suscripcion por 3 meses a brilliant.com!")
        print("Avisame que completaste este desafío para enviarte el código de la suscripción.")
        print("¡Feliz cumpleaños! :D")
        print("Sale su manquehuito?")
        print()
        superado = True # Cambiar la variable a True para salir del bucle while
   
    else:
        print("Vaya, no has superado el desafío. No pasa nada, sé que lo puedes conseguir. Inténtalo de nuevo tantas veces como quieras.") 