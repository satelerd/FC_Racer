# Feliz_Cumpleaños.py
import time
import random

# Mensaje de bienvenida
# Mensaje de bienvenida
print("Hola Bitran. Te he enviado este archivo especial porque hoy es tu cumpleaños y quiero desearte lo    .")
print("Pero no creas que te voy a regalar algo tan fácilmente. Tendrás que demostrar que eres digno de recibirlo superando un desafío.")
print("El desafío consiste en escribir sobre un tema que te apasione lo más rápido y sin errores posible. Sé que eres muy bueno en esto, así que no te lo pondré fácil.")
print("Debes alcanzar una velocidad mínima de 40 wpm y cometer como máximo 3 errores para lograr tu objetivo.")
print()

# Crear el texto a escribir con palabras aleatorias de la lista
lista = ["trobi", "bitri", "blitzcrank", "blitz", "super red del bitran", "BitriElTocino"]
texto = ""
for i in range(10):
    palabra = random.choice(lista)
    texto += palabra + " "
print(f"El texto a escribir es: {texto}")
print()

print("¿Estás listo? Presiona ENTER para comenzar.")
input()

# Iniciar el cronómetro y pedir al usuario que escriba el texto
tiempo_inicial = time.time()
texto_usuario = input("Escribe el texto aquí: ")
tiempo_final = time.time()

# Calculos de velocidad y errores
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

# Establecer un umbral mínimo de velocidad y máximo de errores para superar el desafío
velocidad_minima = 40 # wpm
errores_maximos = 5
if wpm >= velocidad_minima and errores <= errores_maximos:
    print("¡Grandeeee wnnnnnn! Has superado el desafío con éxito. Sabía que podías hacerlo.") 
    print("Tu regalo es una suscripción de 1 mes en brilliant.com.")
    print()
else:
    print("Preocupante... no has superado el desafío. Pero sé que lo puedes conseguir, inténtalo de nuevo tantas veces como quieras.") 