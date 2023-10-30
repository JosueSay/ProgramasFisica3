from vpython import *
# Variables globales para gestionar el canvas y la escena
current_scene = None

def cerrar_simulacion_esfera():
    global current_scene
    if current_scene:
        current_scene.delete()
        current_scene = None

def cerrar_canvas_actual():
    """Cierra el canvas actual si existe."""
    global current_scene
    if current_scene:
        current_scene.delete()

def iniciar_simulacion_esfera(distancia, velocidad, signo_es, signo_pa):
    cerrar_canvas_actual()  # Cierra el canvas anterior si existe
    simulacionEsfera(distancia, velocidad, signo_es, signo_pa)

def simulacionEsfera(distancia_c, velocidad_c, signo_es, signo_pa):
    global current_scene

    signos = False
    signo_esfera = signo_es
    signo_particula = signo_pa
    volver = True


    # Verificar si los signos son iguales
    if signo_esfera*signo_particula > 0:
        signos = True
    if signo_esfera*signo_particula == 0:
        volver = False
    else:
        signos = False

    # Configuración de la escena
    current_scene = canvas(title='Simulación Esfera', width=1920, height=1080)

    # Crear la esfera azul de radio 5
    esfera_azul = sphere(pos=vector(0, 0, 0), radius=5, color=color.blue)

    distancia_recorrida = 0  # Variable para almacenar la distancia recorrida

    def move_particle(evt):
        nonlocal distancia_recorrida
        if evt.event == 'click':
            # Obtener la posición donde se hizo clic
            click_pos = evt.pos
            # Calcular la dirección y distancia desde el centro de la esfera hasta la posición del clic
            direccion = norm(click_pos - esfera_azul.pos)
            nueva_posicion = esfera_azul.pos + esfera_azul.radius * direccion

            # Crear la partícula roja en la posición del clic
            particula_roja = sphere(pos=nueva_posicion, radius=0.1, color=color.red)
            
            if volver:
                if distancia_c > 0:
                    while mag(particula_roja.pos - nueva_posicion) < distancia_c:
                        rate(60)
                        particula_roja.pos = particula_roja.pos + direccion * velocidad_c
                        distancia_recorrida += velocidad_c  # Actualizar la distancia recorrida
                else:
                    while mag(particula_roja.pos - nueva_posicion) > distancia_c:
                        rate(60)
                        particula_roja.pos = particula_roja.pos - direccion * velocidad_c
                        distancia_recorrida += velocidad_c  # Actualizar la distancia recorrida

                if signos == False:  # Si los signos son iguales
                    while mag(particula_roja.pos - nueva_posicion) > 0.01:  # Espera a que la partícula regrese a su posición original
                        rate(60)
                        if mag(particula_roja.pos - nueva_posicion) > 0:
                            particula_roja.pos = particula_roja.pos - direccion * velocidad_c
                        else:
                            particula_roja.pos = particula_roja.pos + direccion * velocidad_c

            else:
                print("No volvere")
                if distancia_c > 0:
                    while mag(particula_roja.pos - nueva_posicion) < 1e50:
                        rate(60)
                        particula_roja.pos = particula_roja.pos + direccion * velocidad_c
                        distancia_recorrida += velocidad_c  # Actualizar la distancia recorrida
                else:
                    while mag(particula_roja.pos - nueva_posicion) > 1e50:
                        rate(60)
                        particula_roja.pos = particula_roja.pos - direccion * velocidad_c
                        distancia_recorrida += velocidad_c  # Actualizar la distancia recorrida

                if signos == False:  # Si los signos son iguales
                    while mag(particula_roja.pos - nueva_posicion) > 0.01:  # Espera a que la partícula regrese a su posición original
                        rate(60)
                        if mag(particula_roja.pos - nueva_posicion) > 0:
                            particula_roja.pos = particula_roja.pos - direccion * velocidad_c
                        else:
                            particula_roja.pos = particula_roja.pos + direccion * velocidad_c
    # Capturar eventos de clic del mouse en la escena
    current_scene.bind('click', move_particle)