from vpython import *

# --- Función para calcular la distancia de alejamiento ---
def distancia_alejamiento(datos):
    epsilon_0 = 8.854e-12
    densidad_superficial = datos[1]
    carga_particula = datos[2]
    masa_particula = datos[3]
    velocidad_inicial_particula = datos[4]

    distancia = (epsilon_0 * masa_particula * (velocidad_inicial_particula ** 2)) / (carga_particula * densidad_superficial)
    return distancia

# --- Función de simulación que usará los datos recopilados ---
def iniciar_simulacion(datos):
    scene = canvas(title="Simulación de Partícula y Plano con Carga",
                   width=800, height=600,
                   center=vector(0,0,0), background=vector(0.5,0.5,0.5))

    plano = box(pos=vector(0,-0.5,0), size=vector(10,1,10), color=color.green)
    particula = sphere(pos=vector(0,-100,0), radius=0.5, color=color.red, make_trail=True)

    dt = 0.01
    lanzado = False  
    velocidad = 0

    def click(event):
        nonlocal lanzado, velocidad
        if abs(event.pos.y - plano.pos.y) < plano.size.y/2:
            particula.pos = event.pos
            particula.pos.y += 0.6
            distancia_max = distancia_alejamiento(datos)
            velocidad = ((2 * distancia_max * datos[2] * datos[1]) / (datos[3] * 8.854e-12))**0.5
            lanzado = True

    scene.bind('click', click)

    while True:
        rate(100)
        if lanzado:
            particula.pos.y += velocidad * dt
            velocidad -= 9.81 * dt

            if particula.pos.y <= plano.pos.y + 0.6:
                particula.pos.y = plano.pos.y + 0.6
                lanzado = False

