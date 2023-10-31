# Importar módulos necesarios
from P_Plano import iniciar_simulacion_plano, cerrar_simulacion_plano
from P_Esfera import iniciar_simulacion_esfera, cerrar_simulacion_esfera
import math
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QComboBox,
    QDesktopWidget,
    QMessageBox
)

# Definir partículas predefinidas
particulas_predefinidas = {
    "Protón": [1.602e-19, 1.673e-27],
    "Positrón": [1.602e-19, 9.109e-31],
    "Alfa": [3.204e-19, 6.644e-27],
    "Núcleo de helio": [3.20435e-19, 6.64424e-27],
    "Núcleo de hidrogeno": [1.60217663e-19, 1.673e-27]
}

# Función para cerrar la simulación y salir del programa
def cerrar_simulacion():
    global current_scene
    try:
        cerrar_simulacion_plano()  # Intenta cerrar la simulación gráfica
        cerrar_simulacion_esfera()  # Intenta cerrar la simulación gráfica
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Finalizado")
        mensaje.setText("El programa ha finalizado.")
        mensaje.exec_()
        sys.exit()
    except KeyboardInterrupt:
        print("\033[1m\033[91mPrograma finalizado por el usuario.\033[0m")
    except SystemExit:
        print("\033[1m\033[91mSimulación finalizada.\033[0m")
    except Exception as e:
        print(f"\033[1m\033[91mError al cerrar la simulación: {e}\033[0m")
        sys.exit()
        

def cargar_particula(index):
    if part_selector.currentText() == "Partícula personalizada":
        carga_particula_input.setEnabled(True)
        masa_input.setEnabled(True)
        carga_particula_input.clear()
        masa_input.clear()
    else:
        carga_particula_input.setText(str(particulas_predefinidas[part_selector.currentText()][0]))
        masa_input.setText(str(particulas_predefinidas[part_selector.currentText()][1]))
        carga_particula_input.setEnabled(False)
        masa_input.setEnabled(False)

def tipo_cambiado(index):
    if index == 0:  # Índice 0 es 'Esfera'
        densidad_input.setEnabled(False)
        radio_input.setEnabled(True)
        carga_esfera_input.setEnabled(True)
    else:
        densidad_input.setEnabled(True)
        radio_input.setEnabled(False)
        carga_esfera_input.setEnabled(False)

def guardar_datos():    
    tipo = tipoSelector.currentText()
    if tipo == "Plano":
        densidad = densidad_input.text()
        datos = [tipo, densidad]
    else:
        radio = radio_input.text()
        carga_esfera = carga_esfera_input.text()
        datos = [tipo, radio, carga_esfera]

    carga_particula = carga_particula_input.text()
    masa = masa_input.text()
    velocidad = velocidad_input.text()

    # Validar que los valores sean numéricos
    try:
        float(carga_particula)
        float(masa)
        velocidad = float(velocidad)
        if velocidad > 3 * 10**8:
            velocidad = 3 * 10**8
            print("\033[1m\033[91mLa velocidad ingresada es mayor a la de la luz. Se actualizó la velocidad inicial de la partícula a la de la velocidad de la luz.\033[0m")
    except ValueError:
        print("\033[1m\033[91mIngresa valores numéricos para la carga de la partícula, masa y velocidad.\033[0m")

        return

    datos += [carga_particula, masa, velocidad]    
    datos_nuevos = [datos[0]] + [float(dato) for dato in datos[1:]]

    # realizar calculo
    if tipo == "Plano":    
        llamarPlano(datos)
       
    else:
        llamarEsfera(datos)

def llamarPlano(datos):
    
    try:
        # Obtener variables
        densidad_pl = float(datos[1])
        carga_p = float(datos[2])
        masa_p = float(datos[3])
        velocidad_inicial_p = float(datos[4])
        epsilon_0 = 8.85e-12
        
        # Mostrar datos
        print("\033[1m\nLos datos que ingresaste son:\033[0m")
        print("\t• Distribución: ", datos[0])
        print("\t• Densidad superficial: ", densidad_pl, "C/m^2")
        print("\t• Carga de la partícula: ", carga_p, "C")
        print("\t• Masa de la partícula: ", masa_p, "Kg")
        print("\t• Velocidad inicial de la partícula: ", velocidad_inicial_p, "m/s")
        
        # Calcular distancia
        distancia = (epsilon_0 * masa_p * velocidad_inicial_p**2) / (abs(carga_p * densidad_pl))
        print("\033[1m\033[34mLa distancia recorrida por la partícula es de:\033[0m", distancia, "m\n")
        
        # Iniciar simulación
        iniciar_simulacion_plano(distancia, velocidad_inicial_p, densidad_pl, carga_p)
    except Exception as e:
        print("Error en llamarPlano:", e)
    
 
def llamarEsfera(datos):
    try:
        # Obtener variables
        radio_e = float(datos[1])
        carga_e = float(datos[2])
        carga_p = float(datos[3])
        masa_p = float(datos[4])
        velocidad_inicial_p = float(datos[5])
        epsilon_0 = 8.85e-12
        v_luz = 3.00e8
        agujero_negro = False
        aviso = ""
        
        # Mostrar datos
        print("\033[1m\nLos datos que ingresaste son:\033[0m")
        print("\t• Distribución: ", datos[0])
        print("\t• Radio de la esfera: ", datos[1], "m")
        print("\t• Carga de la esfera: ", datos[2], "C")
        print("\t• Carga de la partícula: ", datos[3], "C")
        print("\t• Masa de la partícula: ", datos[4], "Kg")
        print("\t• Velocidad inicial de la partícula: ", datos[5], "m/s\n")
        
        ## Calculos
        # Calcular distancia
        distancia = (masa_p * velocidad_inicial_p**2 * 2 * math.pi * epsilon_0 * radio_e**2) / (abs(carga_p * carga_e)) + radio_e
        print("\033[1m\033[34mLa distancia recorrida por la partícula es de:\033[0m", distancia, "m\n")
        
        # Velocidad de escape
        velocidad_escape = math.sqrt((abs(carga_p * carga_e)) / (2 * math.pi * epsilon_0 * masa_p * radio_e))
        print("\033[1m\033[34mLa velocidad de escape es de:\033[0m", velocidad_escape, "m/s\n")
        
        # Caga máxima
        Q_max = (v_luz**2 * 2 * math.pi * epsilon_0 * masa_p * radio_e) / abs(carga_p)
        print("\033[1m\033[34mLa carga máxima es de:\033[0m", Q_max, "C\n")
        
        if velocidad_escape == velocidad_inicial_p:
            if carga_e < Q_max:
                # Iniciar simulación
                iniciar_simulacion_esfera(distancia,velocidad_inicial_p, radio_e, 0,1)
                aviso = "\033[1mLa partícula no volverá\033[0m"
                print(f"\033[1m\033[34m***Dado que la velocidad inicial de la particula {velocidad_inicial_p} m/s = que la velocidad de escape {velocidad_escape} m/s. ***\033[0m \n{aviso}")
            else:
                # Iniciar simulación
                iniciar_simulacion_esfera(distancia, velocidad_inicial_p, radio_e,  -1, 1)
                agujero_negro = True
                aviso = "\033[1mLa esfera se ha convertido en un agujero negro electrostático.\033[0m"
                print(f"\033[1m\033[34m***Dado que carga de la esfera {carga_e} C >= que la carga máxima {Q_max} C. ***\033[0m \n{aviso}")
        else:
            
            if carga_e >= Q_max:
                # Iniciar simulación
                iniciar_simulacion_esfera(distancia, velocidad_inicial_p, radio_e,  -1, 1)
                agujero_negro = True
                aviso = "\033[1mLa esfera se ha convertido en un agujero negro electrostático.\033[0m"
                print(f"\033[1m\033[34m***Dado que carga de la esfera {carga_e} C >= que la carga máxima {Q_max} C. ***\033[0m \n{aviso}")
            else:
                # Iniciar simulación
                iniciar_simulacion_esfera(distancia, velocidad_inicial_p, radio_e,  carga_e, carga_p)
        
    except Exception as e:
        print("Error en llamarEsfera:", e)

# Creación de la aplicación y la ventana principal
app = QApplication(sys.argv)
app.setStyle('Fusion')  # Establecer el estilo de la aplicación
window = QWidget()
window.setWindowTitle("Registro de Datos")  # Nombre del encabezado de la ventana

layout = QVBoxLayout()  # Diseño de la ventana
form_layout = QFormLayout()  # Diseño de formulario dentro de la ventana

# Creación de elementos para interactuar con el usuario (Entradas, ComboBox, etc.)
# Cada uno se agrega al formulario
tipoSelector = QComboBox()
tipoSelector.addItems(["Esfera", "Plano"])
tipoSelector.setCurrentIndex(1)  # Iniciar con la opción de "Plano"
tipoSelector.currentIndexChanged.connect(tipo_cambiado)
form_layout.addRow("Selecciona el tipo de distribución:", tipoSelector)

radio_input = QLineEdit()
radio_input.setPlaceholderText("Radio de la esfera (Metros)")
radio_input.setEnabled(False)
form_layout.addRow("Radio de la esfera:", radio_input)

carga_esfera_input = QLineEdit()
carga_esfera_input.setPlaceholderText("Carga de la esfera (Coulombs)")
carga_esfera_input.setEnabled(False)
form_layout.addRow("Carga de la esfera:", carga_esfera_input)

densidad_input = QLineEdit()
densidad_input.setPlaceholderText("Densidad superficial (Coulombs/Metro cuadrado)")
form_layout.addRow("Densidad superficial:", densidad_input)

part_selector = QComboBox()
part_selector.addItems(list(particulas_predefinidas.keys()) + ["Partícula personalizada"])
part_selector.setCurrentIndex(len(particulas_predefinidas))  # Iniciar con "Partícula personalizada"
part_selector.currentIndexChanged.connect(cargar_particula)
form_layout.addRow("Selecciona una partícula:", part_selector)

carga_particula_input = QLineEdit()
carga_particula_input.setPlaceholderText("Carga de la partícula (Coulombs)")
carga_particula_input.setEnabled(True)  # Iniciar habilitado para "Partícula personalizada"
form_layout.addRow("Carga de la partícula:", carga_particula_input)

masa_input = QLineEdit()
masa_input.setPlaceholderText("Masa de la partícula (Kilogramos)")
masa_input.setEnabled(True)  # Iniciar habilitado para "Partícula personalizada"
form_layout.addRow("Masa de la partícula:", masa_input)

velocidad_input = QLineEdit()
velocidad_input.setPlaceholderText("Velocidad inicial (Metros/Segundos)")
form_layout.addRow("Velocidad inicial:", velocidad_input)

submit_button = QPushButton("Guardar datos")  # Botón para guardar datos
submit_button.clicked.connect(guardar_datos)  # Conectar el botón a la función guardar_datos
finish_button = QPushButton("Finalizar")  # Botón para finalizar
finish_button.clicked.connect(cerrar_simulacion)  # Conectar el botón a la función cerrar_simulacion

# Añadir todos los elementos al diseño de la ventana
layout.addLayout(form_layout)
layout.addWidget(submit_button)
layout.addWidget(finish_button)
window.setLayout(layout)

# Configurar la ventana y mostrarla en el centro de la pantalla
desktop = QDesktopWidget()
screen_width = desktop.screen().width()
screen_height = desktop.screen().height()

window_width = window.frameSize().width()
window_height = window.frameSize().height()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

window.setGeometry(x, y, window_width, window_height)
window.show()



sys.exit(app.exec_())  # Iniciar la aplicación y esperar a que el usuario interactúe