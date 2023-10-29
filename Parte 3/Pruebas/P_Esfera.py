from vpython import *


radio_e = 1
distancia_p = 2.5
aviso = False

# Crear la escena
scene = canvas(title='Simulación Esfera', width=1920, height=1080)
# Crear una esfera azul
esfera = sphere(pos=vector(0, 0, 0), radius=radio_e, color=color.blue)

# Crear una partícula roja
particula = sphere(pos=esfera.pos, radius=0.1, color=color.red)

# Distancia que la partícula se moverá
distancia = distancia_p

def al_hacer_click(evt):
    # Obtener la posición del clic
    local = evt.pos
    if mag(local - esfera.pos) <= esfera.radius:
        # Dirección desde la superficie de la esfera hasta el punto de destino
        direccion = norm(local - esfera.pos)
        # Mover la partícula
        particula.pos = local + direccion * distancia
        
        # Cambiar el color de la esfera si la distancia es mayor a 2
        if aviso:
            esfera.color = color.white

# Asignar la función al evento del clic
scene.bind('click', al_hacer_click)
