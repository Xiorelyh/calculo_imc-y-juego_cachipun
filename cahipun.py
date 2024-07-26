#Se pide crear el programa cachipun.py, donde el usuario entregará como
#argumento: piedra, papel o tijera. Para que el computador pueda jugar escogerá un
# argumento al azar


#Esta libreria permite escoger una opcion aleatoria dentro de las determinadas anteriormente.
import random

computadora = (random.choice(["piedra", "papel", "tijera"]))


#Jugadores
usuario = (input("Escribe tu opción: "))
if usuario == "piedra" or usuario == "papel" or usuario == "tijera" :
    print("Empieza el juego")
    print("Computadora eligió:" , computadora)

# Opciones de resultado
    if usuario == computadora:
        print("Empate")
    elif usuario == "piedra" and computadora == "tijera":
        print("Ganaste!")
    elif usuario == "tijera" and computadora == "papel":
        print("Ganaste!")
    elif usuario == "papel" and computadora == "piedra":
        print("Ganaste!")
    else:
        print("Perdiste")    

# Error por opcion invalida
else:
    print("Debe escribir una de las opciones: piedra-papel-tijera")