from vpython import *

# Variables globales para gestionar el canvas y la escena
current_scene = None

def ajustar_valores(distancia, velocidad):
    # Rangos deseados con enfoque "reloj"
    rango_distancia = [2, 30]
    rango_velocidad = [0.01, 1]

    # Función para simular el "reloj"
    def ajuste_reloj(valor, rango):
        if valor < rango[0]:
            diferencia = valor - rango[0]
            return rango[1] - abs(diferencia) % (rango[1] - rango[0])
        elif valor > rango[1]:
            diferencia = valor - rango[1]
            return rango[0] + abs(diferencia) % (rango[1] - rango[0])
        return valor

    # Ajuste de la distancia y velocidad con enfoque "reloj"
    distancia = ajuste_reloj(distancia, rango_distancia)
    velocidad = ajuste_reloj(velocidad, rango_velocidad)

    print(distancia, "-", velocidad)
    return distancia, velocidad

def cerrar_simulacion_plano():
    global current_scene
    if current_scene:
        current_scene.delete()
        current_scene = None

def cerrar_canvas_actual():
    """Cierra el canvas actual si existe."""
    global current_scene
    if current_scene:
        current_scene.delete()

def iniciar_simulacion_plano(distancia, velocidad, signo_pl, signo_pa):
    cerrar_canvas_actual()  # Cierra el canvas anterior si existe
    simulacionPlano(distancia, velocidad, signo_pl, signo_pa)

def simulacionPlano(distancia_c, velocidad_c, signo_pl, signo_pa):
    global current_scene

    n_distancia, n_velocidad = ajustar_valores(distancia_c, velocidad_c)
    
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

    distancia_recorrida = 0  # Variable para almacenar la distancia recorrida

    def clic(event):
        nonlocal distancia_recorrida
        pos_click = event.pos
        new_particle = sphere(pos=vector(pos_click.x, 0, pos_click.z), radius=0.1, color=color.red)
        initial_position = new_particle.pos.y  # Guarda la posición inicial de la nueva partícula

        if n_distancia > 0:
            while new_particle.pos.y < n_distancia:
                rate(30)  # Controla la velocidad de la animación
                new_particle.pos.y += n_velocidad
                distancia_recorrida += n_velocidad  # Actualizar la distancia recorrida
        else:
            while new_particle.pos.y > n_distancia:
                rate(30)  # Controla la velocidad de la animación
                new_particle.pos.y -= n_velocidad
                distancia_recorrida += n_velocidad  # Actualizar la distancia recorrida

        if signos == False:  # Si los signos son iguales
            while abs(new_particle.pos.y - initial_position) > 0.01:  # Espera a que la partícula regrese a su posición original
                rate(30)
                if new_particle.pos.y > initial_position:
                    new_particle.pos.y -= n_velocidad
                else:
                    new_particle.pos.y += n_velocidad

    # Capturar eventos de clic del mouse en la escena
    current_scene.bind("click", clic)