from vpython import *

scene = canvas(title='Prueba', width=1920, height=1080)

# Crear la esfera azul de radio 5
esfera_azul = sphere(pos=vector(0, 0, 0), radius=5, color=color.blue)

regresar = True  # Cambiado a False inicialmente para evitar el retorno inmediato

distancia = 5

def move_particle(evt):
    global particula_roja, distancia, regresar
    if evt.event == 'click':
        # Obtener la posición donde se hizo clic
        click_pos = evt.pos
        # Calcular la dirección y distancia desde el centro de la esfera hasta la posición del clic
        direccion = norm(click_pos - esfera_azul.pos)
        nueva_posicion = esfera_azul.pos + esfera_azul.radius * direccion
        
        # Crear la partícula roja en la posición del clic
        particula_roja = sphere(pos=nueva_posicion, radius=0.1, color=color.red)
        
        while mag(particula_roja.pos - nueva_posicion) < distancia:
            rate(60)
            particula_roja.pos = particula_roja.pos + direccion * 0.1
            
        if regresar:  # Verifica si se debe mover de regreso a la esfera
            while mag(particula_roja.pos - esfera_azul.pos) > esfera_azul.radius:  # Mover de regreso a la esfera
                rate(60)
                direccion_regreso = norm(esfera_azul.pos - particula_roja.pos)
                particula_roja.pos = particula_roja.pos + direccion_regreso * 0.1

scene.bind('click', move_particle)
