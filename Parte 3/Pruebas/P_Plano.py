from vpython import *

# Variables globales para gestionar el canvas y la escena
current_scene = None

# Nueva función para cerrar la simulación
def cerrar_simulacion_grafica():
    global current_scene
    if current_scene:
        current_scene.delete()
        current_scene = None

def cerrar_canvas_actual():
    """Cierra el canvas actual si existe."""
    global current_scene
    if current_scene:
        current_scene.delete()

def iniciar_simulacion(distancia, velocidad, signo_pl, signo_pa):
    cerrar_canvas_actual()  # Cierra el canvas anterior si existe
    simulacionPlano(distancia, velocidad, signo_pl, signo_pa)

def simulacionPlano(distancia_c, velocidad_c, signo_pl, signo_pa):
    global current_scene
    
    signos = False
    
    signo_plano = signo_pl
    signo_particula = signo_pa

    # Verificar si los signos son iguales
    if signo_plano * signo_particula > 0:
        signos = True
    else:
        signos = False

    # Configuración de la escena
    current_scene = canvas(title='Simulación Plano', width=1920, height=1080)

    # Definir el tamaño del plano
    width = 10  # Ancho del plano
    length = 50  # Longitud del plano

    # Crear el plano (utilizando un objeto box muy delgado)
    plane = box(pos=vector(0, 0, 0), size=vector(width, 0.1, length), color=color.blue)

    # Crear una partícula (esfera) en el plano
    particle = sphere(pos=vector(0, 0, 0), radius=0.1, color=color.red)
    initial_position = particle.pos.y  # Guarda la posición inicial de la partícula

    distancia_recorrida = 0  # Variable para almacenar la distancia recorrida

    def clic(event):
        nonlocal particle, distancia_recorrida
        pos_click = event.pos
        particle.pos = vector(pos_click.x, 0, pos_click.z)

        if distancia_c > 0:
            while particle.pos.y < distancia_c:
                rate(30)  # Controla la velocidad de la animación
                particle.pos.y += velocidad_c
                distancia_recorrida += velocidad_c  # Actualizar la distancia recorrida
        else:
            while particle.pos.y > distancia_c:
                rate(30)  # Controla la velocidad de la animación
                particle.pos.y -= velocidad_c
                distancia_recorrida += velocidad_c  # Actualizar la distancia recorrida

        if signos == False:  # Si los signos son iguales
            while abs(particle.pos.y - initial_position) > 0.01:  # Espera a que la partícula regrese a su posición original
                rate(30)
                if particle.pos.y > initial_position:
                    particle.pos.y -= velocidad_c
                else:
                    particle.pos.y += velocidad_c

    # Capturar eventos de clic del mouse en la escena
    current_scene.bind("click", clic)
