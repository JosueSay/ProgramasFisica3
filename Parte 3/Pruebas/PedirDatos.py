# Importa el módulo P_Esfera o P_Plano
import P_Esfera
import P_Plano
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
    QDesktopWidget
)

# Definir partículas predefinidas
particulas_predefinidas = {
    "Protón": [1.602e-19, 1.673e-27],
    "Positrón": [1.602e-19, 9.109e-31],
    "Alfa": [3.204e-19, 6.644e-27],
    "Electrón": [-1.602e-19, 9.109e-31],
    "Neutrón": [0, 1.675e-27]
}

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
            print("\033[91mLa velocidad ingresada es mayor a la de la luz. Se actualizó la velocidad inicial de la partícula a la de la velocidad de la luz.\033[0m")
    except ValueError:
        print("\033[91mIngresa valores numéricos para la carga de la partícula, masa y velocidad.\033[0m")
        return

    datos += [carga_particula, masa, velocidad]
    
    print("Datos ingresados:")
    print(datos)
    print("")
    
    # realizar calculo
    if tipo == "Plano":    
        # convertir datos
        datos_decimales = [datos[0]] + [float(dato) for dato in datos[1:]]
        
        # obtener variables
        epsilon_0 = 8.854e-12
        densidad_p = datos_decimales[1]
        carga_p = datos_decimales[2]
        masa_p = datos_decimales[3]
        velocidad_inicial_p = datos_decimales[4]
        distancia_pp = (epsilon_0 * masa_p * (velocidad_inicial_p ** 2)) / (carga_p * densidad_p)
        
        
        print("\033[94mLa distancia calculada es: ", distancia_pp)
        print(" \033[0m")
        print("Hare una nueva simulación con: ", velocidad_inicial_p)

        # Iniciar una nueva simulación con los datos actualizados
        P_Plano.iniciar_simulacion(5, velocidad_inicial_p)
       
    else:
        print("Hola")
        #P_Esfera.procesar_datos(datos)
        #simulacion(datos_decimales)

def cerrar_simulacion():
    # Detener la simulación aquí
    exit()  # Cerrar el programa

app = QApplication(sys.argv)
app.setStyle('Fusion')  # Para un estilo más consistente en distintos sistemas operativos
window = QWidget()
window.setWindowTitle("Registro de Datos")  # Nombre del encabezado de la ventana

layout = QVBoxLayout()

form_layout = QFormLayout()

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

submit_button = QPushButton("Guardar datos")
submit_button.clicked.connect(guardar_datos)

layout.addLayout(form_layout)
layout.addWidget(submit_button)
window.setLayout(layout)

# Obtener información sobre la pantalla
desktop = QDesktopWidget()
screen_width = desktop.screen().width()
screen_height = desktop.screen().height()

# Obtener el tamaño de la ventana
window_width = window.frameSize().width()
window_height = window.frameSize().height()

# Calcular el centro
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Establecer la posición en el centro
window.setGeometry(x, y, window_width, window_height)

window.show()
sys.exit(app.exec_())
