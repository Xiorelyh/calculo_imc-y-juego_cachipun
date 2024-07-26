#Se pide crear el programa cachipun.py, donde el usuario entregará como
#argumento: piedra, papel o tijera. Para que el computador pueda jugar escogerá un
# argumento al azar

import random

computadora = (random.choice(["piedra", "papel", "tijera"]))


#Jugadores
jugador = (input("Escribe tu opción: "))
if jugador == "piedra" or jugador == "papel" or jugador == "tijera" :
    print("Empieza el juego")
    print("Computadora eligió:" , computadora)

# Opciones de resultado
    if jugador == computadora:
        print("Empate")
    elif jugador == "piedra" and computadora == "tijera":
        print("Ganaste!")
    elif jugador == "tijera" and computadora == "papel":
        print("Ganaste!")
    elif jugador == "papel" and computadora == "piedra":
        print("Ganaste!")
    else:
        print("Perdiste")    

# Error por opcion invalida
else:
    print("Debe escribir una de las opciones: piedra-papel-tijera")