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
        
        electron.direccion = vector(velocidad_electron, 0, 0)  
        
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

def iniciarSimulacionCilindro(diametro_c, longitud_c, densidad_e, velocidad_e, corriente_c):
    cerrarSimulacionActual()  # Cierra el canvas anterior si existe
    simulacionCilindro(diametro_c, longitud_c, densidad_e, velocidad_e, corriente_c)

def simulacionCilindro(diametro_c, longitud_c, densidad_e, velocidad_e, corriente_c):
    longitud = int(longitud_c)
    radio_cilindro = int(diametro_c/2)
    radio_electron = 0.25
    velocidad_electron = velocidad_e
    centro_cilindro = longitud / 2
    cant_electrones = 100
    largo_cable = 30
    radio_cable = 1
    largo_vertical = 30
    msj = ""
    msj2 = ""
    if corriente_c <0:
        msj ="<- Corriente (-)"
        msj2 ="Voltaje (-) ->"
    else:
        msj ="Corriente (+) ->"
        msj2 ="<- Voltaje (+)"

    while True:
        # Configuración de la escena
        espacio = canvas(title='Simulación', width=1920, height=1080)
        
        # Crear cilindro azul horizontal vacío en el centro de la escena
        cable = cylinder(pos=vector(-centro_cilindro, 0, 0), axis=vector(longitud, 0, 0), radius=radio_cilindro, color=color.blue, opacity=0.5)
        
        # Dirección de la corriente
        # Calcular la posición del texto
        # Ubicación x del centro del cilindro
        centro_x = cable.pos.x + cable.axis.x / 2
        # La altura del texto se establece en 1, centrado a lo largo del radio del cilindro
        centro_y = radio_cilindro
        # Ubicación z del texto
        centro_z = 0

        # Crear texto centrado en el cilindro
        texto = text(text=msj, pos=vector(centro_x, centro_y, centro_z), depth=0.1, height=1, color=color.green)
        
        # Crear cables de conexion
        cable_izquierdo = cylinder(pos=vector(-centro_cilindro - largo_cable, 0, 0), axis=vector(largo_cable, 0, 0), radius=radio_cable, color=color.orange)
        cable_derecho = cylinder(pos=vector(centro_cilindro, 0, 0), axis=vector(largo_cable, 0, 0), radius=radio_cable, color=color.orange)

        # Crear cables de conexion
        cable_vertical_izquierdo = cylinder(pos=vector(-centro_cilindro - largo_cable, 0, 0), axis=vector(0, 0, largo_vertical), radius=radio_cable, color=color.orange)
        cable_vertical_derecho = cylinder(pos=vector(centro_cilindro + largo_cable, 0, 0), axis=vector(0, 0, largo_vertical), radius=radio_cable, color=color.orange)

        # Crear cables de conexion
        cable_horizontal_izquierdo = cylinder(pos=vector(-centro_cilindro - largo_cable, 0, largo_vertical), axis=vector(largo_cable, 0, 0), radius=radio_cable, color=color.orange)
        cable_horizontal_derecho = cylinder(pos=vector(centro_cilindro + largo_cable, 0, largo_vertical), axis=vector(-largo_cable, 0, 0), radius=radio_cable, color=color.orange)

        # Crear fuente
        fuente = box(pos=vector(0, 0, largo_vertical), size=vector(longitud, radio_cilindro, radio_cilindro), color=color.red)
        # Crear texto encima de la caja (fuente)
        texto_caja = text(text=msj2, pos=vector(centro_x, centro_y/2 + 1, centro_z + largo_vertical), depth=0.1, height=1, color=color.green)


        # Llama a la función crearElectrones para generar los electrones
        electrones = crearElectrones(cant_electrones, centro_cilindro, radio_cilindro, radio_electron, velocidad_electron)

        while True:
            rate(100)  # Controla la velocidad de la animación
            for electron in electrones:
                # Lógica corregida para la dirección del movimiento de los electrones según la corriente
                if corriente_c > 0:  # Si la corriente es positiva
                    electron.pos += electron.direccion
                    # Verificar si el electrón sale del cable y manejar su movimiento
                    if electron.pos.x > centro_cilindro:
                        if electron.pos.x > centro_cilindro:
                            electron.visible = False  # Ocultar el electrón
                            electrones.remove(electron)  # Eliminar el electrón de la lista
                            # Crear un nuevo electrón
                            pY, pZ = damePosiciones(-centro_cilindro, radio_cilindro, radio_electron)
                            nuevo_electron = sphere(pos=vector(-centro_cilindro, pY, pZ), radius=radio_electron, color=color.red)
                            nuevo_electron.direccion = vector(velocidad_electron, 0, 0)  # Establecer dirección inicial
                            nuevo_electron.velocidad_electron = velocidad_electron  # Establecer velocidad
                            electrones.append(nuevo_electron)  # Agregar nuevo electrón a la lista
                    
                else:  # Si la corriente es negativa
                    electron.pos -= electron.direccion  # Movimiento en dirección opuesta a la corriente
                    # Verificar si el electrón sale del cable y manejar su movimiento
                    if electron.pos.x < -centro_cilindro:
                        electron.visible = False  # Ocultar el electrón
                        electrones.remove(electron)  # Eliminar el electrón de la lista
                        # Crear un nuevo electrón
                        pY, pZ = damePosiciones(centro_cilindro, radio_cilindro, radio_electron)
                        nuevo_electron = sphere(pos=vector(centro_cilindro, pY, pZ), radius=radio_electron, color=color.red)
                        nuevo_electron.direccion = vector(velocidad_electron, 0, 0)  # Establecer dirección inicial
                        nuevo_electron.velocidad_electron = -velocidad_electron  # Establecer velocidad
                        electrones.append(nuevo_electron)  # Agregar nuevo electrón a la lista
     
iniciarSimulacionCilindro(5, 10, 5, 0.1,  5)