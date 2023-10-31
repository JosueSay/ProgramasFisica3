from vpython import *
# Variables globales para gestionar el canvas y la escena
current_scene = None

def ajustar_valores(distancia, velocidad, radio):
    # Rangos deseados con enfoque "reloj"
    rango_distancia = [2, 15]
    rango_velocidad = [0.01, 1]
    rango_radio = [2, 20]

    # Función para simular el "reloj"
    def ajuste_reloj(valor, rango):
        if valor < rango[0]:
            diferencia = valor - rango[0]
            return rango[1] - abs(diferencia) % (rango[1] - rango[0])
        elif valor > rango[1]:
            diferencia = valor - rango[1]
            return rango[0] + abs(diferencia) % (rango[1] - rango[0])
        return valor

    # Ajuste de la distancia, velocidad y radio con enfoque "reloj"
    distancia = ajuste_reloj(distancia, rango_distancia)
    velocidad = ajuste_reloj(velocidad, rango_velocidad)
    radio = ajuste_reloj(radio, rango_radio)

    #print(distancia, "-", velocidad, "-", radio)
    return distancia, velocidad, radio

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

def iniciar_simulacion_esfera(distancia, velocidad, radio, signo_es, signo_pa):
    cerrar_canvas_actual()  # Cierra el canvas anterior si existe
    simulacionEsfera(distancia, velocidad, radio, signo_es, signo_pa)

def simulacionEsfera(distancia_c, velocidad_c, radio_c, signo_esfera, signo_particula):
    global current_scene

    n_distancia, n_velocidad, n_radio = ajustar_valores(distancia_c, velocidad_c, radio_c)

    volver = True
    # Verificar si los signos son iguales
    if signo_esfera*signo_particula > 0:
        signos = True
    else:
        signos = False
        
        
    if signo_esfera*signo_particula == 0:
        volver = False

    # Configuración de la escena
    current_scene = canvas(title='Simulación Esfera', width=1920, height=1080)

    # Crear la esfera azul de radio 5
    esfera_azul = sphere(pos=vector(0, 0, 0), radius=n_radio, color=color.blue)

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
                if n_distancia > 0:
                    while mag(particula_roja.pos - nueva_posicion) < n_distancia:
                        rate(60)
                        particula_roja.pos = particula_roja.pos + direccion * n_velocidad
                        distancia_recorrida += n_velocidad  # Actualizar la distancia recorrida
                else:
                    while mag(particula_roja.pos - nueva_posicion) > n_distancia:
                        rate(60)
                        particula_roja.pos = particula_roja.pos - direccion * velocidad_c
                        distancia_recorrida += n_velocidad  # Actualizar la distancia recorrida

                if signos == False:  # Si los signos son iguales
                    while mag(particula_roja.pos - nueva_posicion) > 0.01:  # Espera a que la partícula regrese a su posición original
                        rate(60)
                        if mag(particula_roja.pos - nueva_posicion) > 0:
                            particula_roja.pos = particula_roja.pos - direccion * n_velocidad
                        else:
                            particula_roja.pos = particula_roja.pos + direccion * n_velocidad

            else:
                print("No volvere")
                if n_distancia > 0:
                    while mag(particula_roja.pos - nueva_posicion) < 1e50:
                        rate(60)
                        particula_roja.pos = particula_roja.pos + direccion * n_velocidad
                        distancia_recorrida += n_velocidad  # Actualizar la distancia recorrida
                else:
                    while mag(particula_roja.pos - nueva_posicion) > 1e50:
                        rate(60)
                        particula_roja.pos = particula_roja.pos - direccion * n_velocidad
                        distancia_recorrida += n_velocidad  # Actualizar la distancia recorrida

                if signos == False:  # Si los signos son iguales
                    while mag(particula_roja.pos - nueva_posicion) > 0.01:  # Espera a que la partícula regrese a su posición original
                        rate(60)
                        if mag(particula_roja.pos - nueva_posicion) > 0:
                            particula_roja.pos = particula_roja.pos - direccion * n_velocidad
                        else:
                            particula_roja.pos = particula_roja.pos + direccion * n_velocidad
    # Capturar eventos de clic del mouse en la escena
    current_scene.bind('click', move_particle)