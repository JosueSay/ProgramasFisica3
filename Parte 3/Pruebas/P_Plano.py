from vpython import *

# Variables globales para gestionar el canvas y la escena
current_scene = None

def cerrar_canvas_actual():
    """Cierra el canvas actual si existe."""
    global current_scene
    if current_scene:
        current_scene.delete()

def iniciar_simulacion(distancia, velocidad):
    cerrar_canvas_actual()  # Cierra el canvas anterior si existe
    simulacionPlano(distancia, velocidad)

def simulacionPlano(distancia_c, velocidad_c):
    global current_scene
    # Configuración de la escena
    current_scene = canvas(title='Simulación Plano', width=1920, height=1080)

    # Definir el tamaño del plano
    width = 10  # Ancho del plano
    length = 50  # Longitud del plano

    # Crear el plano (utilizando un objeto box muy delgado)
    plane = box(pos=vector(0, 0, 0), size=vector(width, 0.1, length), color=color.blue)

    # Crear una partícula (esfera) en el plano
    particle = sphere(pos=vector(0, 0.1, 0), radius=0.1, color=color.red)

    distancia_recorrida = 0  # Variable para almacenar la distancia recorrida

    def clic(event):
        nonlocal particle, distancia_recorrida
        pos_click = event.pos
        # Mover la partícula a la posición donde se hizo clic
        particle.pos = vector(pos_click.x, 0.1, pos_click.z)

        # Determinar la dirección del movimiento en función del clic
        if pos_click.y > 0:
            # Mover la partícula a lo largo del eje Y hacia arriba desde la posición de clic
            while particle.pos.y < distancia_c:
                rate(30)  # Controla la velocidad de la animación
                particle.pos.y += velocidad_c
                distancia_recorrida += velocidad_c  # Actualizar la distancia recorrida
        else:
            # Mover la partícula a lo largo del eje Y hacia abajo desde la posición de clic
            while particle.pos.y > -distancia_c:
                rate(30)  # Controla la velocidad de la animación
                particle.pos.y -= velocidad_c
                distancia_recorrida += velocidad_c  # Actualizar la distancia recorrida

    # Capturar eventos de clic del mouse en la escena
    current_scene.bind("click", clic)

# Ejemplo de uso:
iniciar_simulacion(5, 0.1)
