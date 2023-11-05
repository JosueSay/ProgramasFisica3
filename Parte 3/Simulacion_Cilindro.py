from vpython import *
from Posiciones import damePosiciones  # Obtener posiciones y & z para la creación de electrones

# Variables globales para gestionar el canvas y la escena
espacio = None

def crearElectrones(cant_electrones, centro_cilindro, radio_cilindro, radio_electron, velocidad_electron):
    electrones = []

    for i in range(cant_electrones):
        pY, pZ = damePosiciones(-centro_cilindro, radio_cilindro, radio_electron)
        # Crear posición
        posicion = vector(-centro_cilindro, pY, pZ)
        # Crear esfera (electrón)
        electron = sphere(pos=posicion, radius=radio_electron, color=color.red)
        electron.direccion = vector(velocidad_electron, 0, 0)  # Establecer dirección inicial de movimiento
        electron.velocidad_electron = velocidad_electron  # Establecer velocidad

        electrones.append(electron)  # Agregar electrón a la lista

    return electrones

def cerrarSimulacionCilindro():
    global espacio
    if espacio:
        espacio.delete()
        espacio = None
        
def cerrarSimulacionActual():
    """Cierra el canvas actual si existe."""
    global espacio
    if espacio:
        espacio.delete()

def iniciarSimulacionCilindro(diametro_c, longitud_c, densidad_e, velocidad_e):
    cerrarSimulacionActual()  # Cierra el canvas anterior si existe
    simulacionCilindro(diametro_c, longitud_c, densidad_e, velocidad_e)

def simulacionCilindro(diametro_c, longitud_c, densidad_e, velocidad_e):
    longitud = int(longitud_c)
    radio_cilindro = int(diametro_c/2)
    cant_electrones = 50
    radio_electron = int((radio_cilindro / 20) * 0.1) if radio_cilindro >= 20 else 0.1
    velocidad_electron = 0.1

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

    # Llama a la función crearElectrones para generar los electrones
    electrones = crearElectrones(cant_electrones, centro_cilindro, radio_cilindro, radio_electron, velocidad_electron)

    # Movimiento de los electrones
    while True:
        rate(100)  # Controla la velocidad de la animación
        for electron in electrones:
            electron.pos += electron.direccion
            # Si el electrón sale del cable, reinicia su posición al inicio del cable
            if electron.pos.x > centro_cilindro:
                electron.pos.x = -centro_cilindro
            
iniciarSimulacionCilindro(20, 10, 5, 2)