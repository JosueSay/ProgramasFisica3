from vpython import *
from Posiciones import damePosiciones  # Obtener posiciones y & z para la creacion de electrones

longitud = 10
radio_cilindro = 2
cant_esferas = 20
radio_electron = 0.1
velocidad_electron= 0.01

# Función para actualizar la velocidad de los electrones
def cambiarVelocidad(new_vel):
    for electron in electrones:
        electron.direccion = vector(new_vel, 0, 0)
        electron.velocidad = new_vel

# Configuración de la escena
espacio = canvas(title='Simulación', width=1920, height=1080)

# Calcular la mitad de la longitud para posicionar en el centro
centro_cilindro = longitud / 2

# Crear cilindro azul horizontal vacío en el centro de la escena
cable = cylinder(pos=vector(-centro_cilindro, 0, 0), axis=vector(longitud, 0, 0), radius=radio_cilindro, color=color.blue, opacity=0.5)

# Lista para almacenar los electrones y sus direcciones de movimiento
electrones = []

# Crea electrones en posiciones aleatorias dentro del rango definido
for i in range(cant_esferas):
    pY, pZ = damePosiciones(-centro_cilindro, radio_cilindro, radio_electron)
    # Crear posición
    posicion = vector(-centro_cilindro, pY, pZ)
    # Crear esfera (electrón)
    electron = sphere(pos=posicion, radius=radio_electron, color=color.red)
    electron.direccion = vector(velocidad_electron, 0, 0)  # Establecer dirección inicial de movimiento
    electron.velocidad_electron = velocidad_electron  # Establecer velocidad

    electrones.append(electron)  # Agregar electrón a la lista

# Movimiento de los electrones
while True:
    rate(100)  # Controla la velocidad de la animación
    for electron in electrones:
        electron.pos += electron.direccion
        # Si el electrón sale del cable, reinicia su posición al inicio del cable
        if electron.pos.x > centro_cilindro:
            electron.pos.x = -centro_cilindro
            
# Cambiar la velocidad en cualquier momento
#nueva_velocidad = 0.2
#cambiarVelocidad(nueva_velocidad)
