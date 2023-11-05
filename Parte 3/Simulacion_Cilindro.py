from vpython import *
from Posiciones import damePosiciones  # Obtener posiciones y & z para la creación de electrones
import random
import math

# Variables globales para gestionar el canvas y la escena
espacio = None

def crearElectrones(cant_electrones, centro_cilindro, radio_cilindro, radio_electron, velocidad):
    electrones = []

    for i in range(cant_electrones):
        pY, pZ = damePosiciones(-centro_cilindro, radio_cilindro, radio_electron)
        # Crear posición
        posicion = vector(-centro_cilindro, pY, pZ)
        # Crear esfera (electrón)
        electron = sphere(pos=posicion, radius=radio_electron, color=color.red)
        
        electron.direccion = vector(velocidad, 0, 0)  
        
        electron.velocidad = velocidad  # Establecer velocidad

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

def iniciarSimulacionCilindro(datos1, datos2):
    cerrarSimulacionActual()  # Cierra el canvas anterior si existe
    simulacionCilindro(datos1, datos2)

def simulacionCilindro(datos1, datos2):
    
    #datos1=[longitud, diametro, material, densidad, resistividad, voltaje]
    #datos2 = [resistencia, corriente, potencia, velocidad, tiempo, horas]
    # Datos ingresados  
    longitud = datos1[0]
    diametro_mostrar = datos1[1]
    diametro = 0
    if diametro_mostrar < 2:
        diametro = 3
    else:
        diametro = diametro_mostrar
    
    material = datos1[2]
    densidad = datos1[3]
    resistividad = datos1[4]
    voltaje = datos1[5]
    
    # Datos calculados
    resistencia = datos2[0]
    corriente = datos2[1]
    potencia = datos2[2]
    
    velocidad_mostrar = datos2[3]
    velocidad = abs(velocidad_mostrar)
    potencia = abs(math.floor(math.log10(abs(velocidad)))) -1
    velocidad = velocidad * 10**(potencia)
    
    tiempo = abs(datos2[4])
    horas = abs(round(datos2[5],3))

    # Constantes
    radio_electron = 0.25
    cant_electrones = 100
    radio_cable = 1
    msj = ""
    msj2 = ""
    
    # Valores usados
    radio_cilindro = int(diametro / 2)
    centro_cilindro = longitud / 2
    largo_cable = diametro
    largo_vertical = diametro

    if corriente <0:
        msj ="<- Corriente (-)"
        msj2 ="Voltaje (-) ->"
    else:
        msj ="Corriente (+) ->"
        msj2 ="<- Voltaje (+)"



    while True:
        # Configuración de la escena
        espacio = canvas(title='Simulación', width=1920, height=1080)
        
        # Mostrar los resultados de cálculos en la esquina superior izquierda
        resistencia_display = label(pos=vector(-longitud, 60, 0), text="Datos Ingresados:", height=15, border=10, font='sans')
        resistencia_display = label(pos=vector(-longitud, 55, 0), text=f"Longitud del cable: {longitud} m", height=15, border=10, font='sans')
        corriente_display = label(pos=vector(-longitud, 50, 0), text=f"Diámetro del cable: {diametro_mostrar} mm", height=15, border=10, font='sans')
        material_display = label(pos=vector(-longitud, 45, 0), text=f"Material del cable: {material}", height=15, border=10, font='sans')
        potencia_display = label(pos=vector(-longitud, 40, 0), text=f"Densidad de particula: {densidad} electrones/m^3", height=15, border=10, font='sans')        
        velocidad_display = label(pos=vector(-longitud, 35, 0), text=f"Resistividad del material: {resistividad} Ωm", height=15, border=10, font='sans')
        tiempo_display = label(pos=vector(-longitud, 30, 0), text=f"Voltaje suministrado: {voltaje} V", height=15, border=10, font='sans')
        
        # Mostrar los resultados de cálculos en la esquina superior izquierda
        resistencia_display = label(pos=vector(longitud, 55, 0), text="Datos Calculados:", height=15, border=10, font='sans')
        resistencia_display = label(pos=vector(longitud, 50, 0), text=f"Resistencia: {resistencia:.3e} Ω", height=15, border=10, font='sans')
        corriente_display = label(pos=vector(longitud, 45, 0), text=f"Corriente: {corriente:.3e} A", height=15, border=10, font='sans')
        potencia_display = label(pos=vector(longitud, 40, 0), text=f"Potencia: {potencia:.3e} W", height=15, border=10, font='sans')
        velocidad_display = label(pos=vector(longitud, 35, 0), text=f"Velocidad: {velocidad_mostrar:.3e} m/s (se multiplicó por un factor de 10^{potencia})", height=15, border=10, font='sans')
        tiempo_display = label(pos=vector(longitud, 30, 0), text=f"Tiempo: {tiempo} s ≈ {horas:.2f} h", height=15, border=10, font='sans')
        
        
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
        electrones = crearElectrones(cant_electrones, centro_cilindro, radio_cilindro, radio_electron, velocidad)

        while True:
            rate(100)  # Controla la velocidad de la animación
            for electron in electrones:
                # Lógica corregida para la dirección del movimiento de los electrones según la corriente
                if corriente > 0:  # Si la corriente es positiva
                    electron.pos += electron.direccion
                    # Verificar si el electrón sale del cable y manejar su movimiento
                    if electron.pos.x > centro_cilindro:
                        if electron.pos.x > centro_cilindro:
                            electron.visible = False  # Ocultar el electrón
                            electrones.remove(electron)  # Eliminar el electrón de la lista
                            # Crear un nuevo electrón
                            pY, pZ = damePosiciones(-centro_cilindro, radio_cilindro, radio_electron)
                            nuevo_electron = sphere(pos=vector(-centro_cilindro, pY, pZ), radius=radio_electron, color=color.red)
                            nuevo_electron.direccion = vector(velocidad, 0, 0)  # Establecer dirección inicial
                            nuevo_electron.velocidad = velocidad  # Establecer velocidad
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
                        nuevo_electron.direccion = vector(velocidad, 0, 0)  # Establecer dirección inicial
                        nuevo_electron.velocidad = -velocidad  # Establecer velocidad
                        electrones.append(nuevo_electron)  # Agregar nuevo electrón a la lista
     
#iniciarSimulacionCilindro(5, 10, 5, 0.1,  5)
