# from random import choice

# jugador= input("ingresa tu opción piedra, papel o tijera: ")
# opcion = choice ["piedra", "papel", "tijeras"]
# print (opcion)

import random

computador = ["piedra", "papel", "tijera"]

jugador = input("ingrese su elección piedra, papel o tijera: ")
if jugador == "piedra" or jugador == "papel" or jugador == "tijera":
    computadora = random.choice(computador)  # Seleccionar la elección aleatoria del computador
    print("El computador jugó: " + computadora)
    
    if jugador == "tijera" and computadora == "papel":
        print("¡Ganaste!")
    elif jugador == "tijera" and computadora == "tijera":
        print("Empate")
    elif jugador == "tijera" and computadora == "piedra":
        print("perdiste")
        
    if jugador == "piedra" and computadora == "tijera":
        print("¡Ganaste!")
    elif jugador == "piedra" and computadora == "piedra":
        print("Empate")
    elif jugador == "piedra" and computadora == "papel":
        print("perdiste") 
        
    if jugador == "papel" and computadora == "piedra":
        print("¡Ganaste!")
    elif jugador == "papel" and computadora == "papel":
        print("Empate")
    elif jugador == "papel" and computadora == "tijera":
        print("perdiste")       
else:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
