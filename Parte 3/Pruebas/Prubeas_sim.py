from vpython import *

scene = canvas(title='Prueba', width=1920, height=1080)
distancia = 2
velocidad = 0.1
signo_plano = -1
signo_particula = 1

signos = False

# Verificar si los signos son iguales
if signo_plano * signo_particula > 0:
    signos = True
else:
    signos = False

scene.background = color.black
width = 10
length = 50

plane = box(pos=vector(0, 0, 0), size=vector(width, 0.1, length), color=color.blue)
particle = sphere(pos=vector(0, 0, 0), radius=0.1, color=color.red)
initial_position = particle.pos.y  # Guarda la posición inicial de la partícula

def clic(event):
    global distancia, velocidad
    pos_click = event.pos
    particle.pos = vector(pos_click.x, 0, pos_click.z)

    if distancia > 0:
        while particle.pos.y < distancia:
            rate(30)
            particle.pos.y += velocidad
    else:
        while particle.pos.y > distancia:
            rate(30)
            particle.pos.y -= velocidad
    
    if signos == False:  # Si los signos son iguales
        while abs(particle.pos.y - initial_position) > 0.01:  # Espera a que la partícula regrese a su posición original
            rate(30)
            if particle.pos.y > initial_position:
                particle.pos.y -= velocidad
            else:
                particle.pos.y += velocidad

scene.bind('click', clic)
