# Feliz_Cumpleaños.py
import time
import random
from termcolor import colored

# Mensaje de bienvenida´
print()
print(colored("Hola Bitran. Te he enviado este archivo especial porque hoy es tu cumpleaños y te tengo un regalo", "yellow", attrs=["bold"]))
print("Pero no creas que te voy a regalar algo tan fácilmente. Tendrás que demostrar que eres digno de recibirlo superando un desafío.")
print("El desafío consiste en escribir sobre un tema que te apasione lo más rápido y menor cantidad de errores posible.")
print("Debes alcanzar una velocidad mínima de 50 wpm y cometer como máximo 3 errores para lograr tu objetivo.")
print()

# Establecer un umbral mínimo de velocidad y máximo de errores para superar el desafío
velocidad_minima = 50 # wpm
errores_maximos = 3

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
    texto += "."

    print(f"El texto a escribir es:")
    print("-----------------------------------------------------------------")
    print(colored(texto, "green", attrs=["bold"]))
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
        print(colored("¡GRAAANNDEEEEE WNNN! Has superado el desafío con éxito.", "green", attrs=["bold"]))
        print("Tu regalo es una suscripcion por 3 meses a brilliant.com!")
        print("Avisame que completaste este desafío para enviarte el código de la suscripción.")
        print("Sale su manquehuito?")
        superado = True # Cambiar la variable a True para salir del bucle while
   
    else:
        print("Vaya, no has superado el desafío. No pasa nada, sé que lo puedes conseguir. Inténtalo de nuevo tantas veces como quieras.") 