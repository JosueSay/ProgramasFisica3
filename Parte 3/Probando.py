from vpython import *

def simulacion(longitud_c, diametro_c):
    longitud = longitud_c
    radio_cilindro = diametro_c / 2
    centro_cilindro = longitud / 2
    msj = 'Corriente ->'

    # Configuración de la escena
    espacio = canvas(title='Simulación', width=1920, height=1080)

    # Crear cilindro azul horizontal vacío en el centro de la escena
    cable = cylinder(pos=vector(-centro_cilindro, 0, 0), axis=vector(longitud, 0, 0), radius=radio_cilindro, color=color.blue, opacity=0.5)

    # Calcular la posición del texto
    # Ubicación x del centro del cilindro
    centro_x = cable.pos.x + cable.axis.x / 2
    # La altura del texto se establece en 1, centrado a lo largo del radio del cilindro
    centro_y = radio_cilindro
    # Ubicación z del texto
    centro_z = 0

    # Crear texto centrado en el cilindro
    texto = text(text=msj, pos=vector(centro_x, centro_y, centro_z), depth=0.1, height=1, color=color.green)

simulacion(20, 10)
