import sys
import Calculos as c
from Simulacion_Cilindro import iniciarSimulacionCilindro
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QComboBox,
    QDesktopWidget,
    QMessageBox
)

def diametro_seleccionado(index):
    if tipo_diametro_selector.currentText() == "Personalizado":
        diametro_input.setEnabled(True)
        diametro_input.clear()
    else:
        diametro_input.setText(str(diametrosMM_calibre_AWG_[numero_calibre_AWG.index(tipo_diametro_selector.currentText())]))
        diametro_input.setEnabled(False)

# Función para actualizar resistividad y densidad al cambiar el material del cable
def material_seleccionado(index):
    material = material_input.currentText()
    index = material_cable.index(material)
    resistividad_text.setText(str(resistividad_material[index]))
    densidad_text.setText(str(densidad_particulas_material[index]))

def guardar_datos():
    bandera = False
    datos = []

    try:
        # Obtener valores de los campos de entrada
        longitud = longitud_input.text()
        material = material_input.currentText()
        voltaje = voltaje_input.text()
        densidad = densidad_text.text()
        resistividad = resistividad_text.text()
        tipo_diametro = tipo_diametro_selector.currentText()

        # Verificar si algún campo está vacío
        if not all([longitud, tipo_diametro, material, voltaje]):
            raise ValueError("Falta ingresar uno o más datos.")

        # Obtener el diámetro correspondiente al calibre seleccionado o el valor personalizado
        if tipo_diametro == "Personalizado":
            diametro = float(diametro_input.text())
        else:
            diametro = diametrosMM_calibre_AWG_[numero_calibre_AWG.index(tipo_diametro)]

        # Verificar si la longitud y el diámetro son no negativos
        if float(longitud) < 0 or float(diametro) < 0:
            raise ValueError("La longitud y el diámetro no pueden ser negativos.")

        # Almacenar los datos en una lista
        datos = [float(longitud), float(diametro), material, float(densidad), float(resistividad), float(voltaje)]
        bandera = True

    except ValueError as e:
        # Mostrar mensaje de error en caso de excepción
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Error")
        mensaje.setText(f"Error al guardar datos: {str(e)}")
        mensaje.exec_()

    if bandera:
        procedimientoFinal(datos)

        
def procedimientoFinal(datos):
    try:
        # Obtener datos:
        longitud = datos[0]
        diametro = datos[1]
        material = datos[2]
        densidad = datos[3]
        resistividad = datos[4]
        voltaje = datos[5]
        carga_electron = 1.62e-19

        # Calcular resistencia, corriente, potencia, velocidad y tiempo
        resistencia = c.dameResitencia(resistividad, longitud, diametro)
        corriente = c.dameCorriente(voltaje, resistencia)
        potencia = c.damePotencia(voltaje, resistencia)
        velocidad = c.dameVelocidadArrastre(corriente, densidad, carga_electron, diametro)
        tiempo = c.dameTiempo(longitud, velocidad)
        horas = tiempo / 3600
        # guardar datos
        datos1=[longitud, diametro, material, densidad, resistividad, voltaje]
        datos2 = [resistencia, corriente, potencia, velocidad, tiempo, horas]
        
        iniciarSimulacionCilindro(datos1, datos2)
        
        
    except Exception as e:
        print("Se ha producido un error:", e)


# Crear la aplicación y la ventana principal
app = QApplication(sys.argv)
app.setStyle('Fusion')

window = QWidget()
window.setWindowTitle("Ingreso de datos")

layout = QVBoxLayout()
form_layout = QFormLayout()

longitud_input = QLineEdit()
longitud_input.setPlaceholderText("Longitud del cable (Metros)")
form_layout.addRow("Longitud del cable:", longitud_input)

# Datos de los calibres y sus respectivos diámetros
numero_calibre_AWG = [
    'AWG 0000', 'AWG 000', 'AWG 00', 'AWG 0', 'AWG 1', 'AWG 2', 'AWG 3', 'AWG 4', 'AWG 5', 'AWG 6',
    'AWG 7', 'AWG 8', 'AWG 9', 'AWG 10', 'AWG 11', 'AWG 12', 'AWG 13', 'AWG 14', 'AWG 15', 'AWG 16',
    'AWG 17', 'AWG 18', 'AWG 19', 'AWG 20', 'AWG 21', 'AWG 22', 'AWG 23', 'AWG 24', 'AWG 25', 'AWG 26',
    'AWG 27', 'AWG 28', 'AWG 29', 'AWG 30', 'AWG 31', 'AWG 32', 'AWG 33', 'AWG 34', 'AWG 35', 'AWG 36',
    'Personalizado'
]

diametrosMM_calibre_AWG_ = [
    11.684, 10.404, 9.266, 8.252, 7.348, 6.544, 5.827, 5.189, 4.621, 4.115,
    3.665, 3.264, 2.906, 2.588, 2.305, 2.053, 1.828, 1.628, 1.45, 1.291,
    1.15, 1.024, 0.912, 0.812, 0.723, 0.644, 0.573, 0.511, 0.455, 0.405,
    0.361, 0.321, 0.287, 0.255, 0.227, 0.202, 0.18, 0.16, 0.143, 0.127,
    None  # None para el campo "Personalizado"
]

tipo_diametro_selector = QComboBox()
tipo_diametro_selector.addItems(numero_calibre_AWG)
# Establecer "Personalizado" como la opción predeterminada
tipo_diametro_selector.setCurrentIndex(tipo_diametro_selector.findText("Personalizado"))
tipo_diametro_selector.currentIndexChanged.connect(diametro_seleccionado)
form_layout.addRow("Tipo de diámetro de cable:", tipo_diametro_selector)

diametro_input = QLineEdit()
diametro_input.setPlaceholderText("Diámetro del cable (Milímetros)")
form_layout.addRow("Diámetro del cable (Milímetros):", diametro_input)

material_cable = ['Oro', 'Plata', 'Cobre', 'Aluminio', 'Grafito']

material_input = QComboBox()
material_input.addItems(material_cable)
material_input.currentIndexChanged.connect(material_seleccionado)
form_layout.addRow("Material del cable:", material_input)

densidad_particulas_material = [5.9e28, 5.86e28, 8.5e28, 2.2e28, 11.2e28]

resistividad_material = [2.44e-8, 1.47e-8, 1.72e-8, 2.75e-8, 3.5e-5]

densidad_text = QLineEdit()
densidad_text.setEnabled(False)
densidad_text.setText(str(densidad_particulas_material[0]))
form_layout.addRow("Densidad de partículas:", densidad_text)

resistividad_text = QLineEdit()
resistividad_text.setEnabled(False)
resistividad_text.setText(str(resistividad_material[0]))
form_layout.addRow("Resistividad del material:", resistividad_text)

voltaje_input = QLineEdit()
voltaje_input.setPlaceholderText("Voltaje (volts)")
form_layout.addRow("Voltaje:", voltaje_input)

submit_button = QPushButton("Iniciar simulación")
submit_button.clicked.connect(guardar_datos)

layout.addLayout(form_layout)
layout.addWidget(submit_button)
window.setLayout(layout)

desktop = QDesktopWidget()
screen_width = desktop.screen().width()
screen_height = desktop.screen().height()

window_width = window.frameSize().width()
window_height = window.frameSize().height()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

window.setGeometry(x, y, window_width, window_height)
window.show()

sys.exit(app.exec_())
