from vpython import *
import random
from Posiciones import damePosiciones # Obtener posiciones y & z para la creacion de electrones

longitud = 10
radio_cilindro = 2
cant_esferas = 20
radio_electron = 0.1

# Configuración de la escena
espacio = canvas(title='Simulación', width=1920, height=1080)

# Calcular la mitad de la longitud para posicionar en el centro
centro_cilindro = longitud / 2

# Crear cilindro azul horizontal vacío en el centro de la escena
cable = cylinder(pos=vector(-centro_cilindro, 0, 0), axis=vector(longitud, 0, 0), radius=radio_cilindro, color=color.blue, opacity=0.5)

# Crea cinco esferas en posiciones aleatorias dentro del rango definido
for i in range(cant_esferas):
    pY, pZ = damePosiciones(-centro_cilindro, radio_cilindro, radio_electron)
    # Crear posición
    posicion = vector(-centro_cilindro, pY, pZ)
    # Crear esfera (electrón)
    electron = sphere(pos=posicion, radius=radio_electron, color=color.red)
