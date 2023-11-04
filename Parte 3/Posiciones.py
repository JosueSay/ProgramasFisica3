import math
import random

def damePosiciones(centro_inicio_cilindro, radio_cilindro, radio_electron):
    x_0 = centro_inicio_cilindro

    # Hacemos una lista de todas las posibles combinaciones de y y z dentro del radio r
    posibilidades = [(y, z) for y in range(-radio_cilindro, radio_cilindro + 1) for z in range(-radio_cilindro, radio_cilindro + 1)]

    # Mezclamos aleatoriamente las posibilidades
    random.shuffle(posibilidades)

    # Iteramos sobre las combinaciones para encontrar la primera válida
    for y, z in posibilidades:
        if (x_0 - centro_inicio_cilindro) ** 2 + (y - 0) ** 2 + (z - 0) ** 2 <= radio_cilindro ** 2:
            if(abs(y) == radio_cilindro):
                #print("hubo cambio de y = ", y)
                y = radio_cilindro-radio_electron
                #print("ahoa es y = ", y)
            if(abs(z) == radio_cilindro):
                #print("hubo cambio de y = ", z)
                z = radio_cilindro-radio_electron
                #print("ahoa es y = ", z)
            return y, z

    return None

# Caso de prueba damePosiciones
#x = 0
#r = 2
#r2 = 0.1
#y, z =  damePosiciones(x, r, r2)
#print("las posiciones son: y = ", y, ", z = ", z)