# Importar librerías necesarias
import sys
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

# Función para cerrar la aplicación
def cerrar_aplicacion():
    sys.exit()

# Función para actualizar la densidad y resistividad según el material seleccionado
def actualizar_densidad_resistividad():
    material = material_input.currentText()
    densidad = densidad_particulas_material[material_cable.index(material)]
    resistividad = resistividad_material[material_cable.index(material)]
    densidad_text.setText(str(densidad))
    resistividad_text.setText(str(resistividad))

# Función para cargar el tipo de diámetro
def cargar_tipo_diametro(index):
    if tipo_diametro_selector.currentText() == "Personalizado":
        diametro_input.setEnabled(True)
    else:
        diametro_input.setEnabled(False)

# Función para guardar los datos ingresados en los campos
def guardar_datos():
    try:
        # Obtener valores de los campos de entrada
        longitud = longitud_input.text()
        diametro = diametro_input.text() if tipo_diametro_selector.currentText() == "Personalizado" else tipo_diametro_selector.currentText()
        material = material_input.currentText()
        voltaje = voltaje_input.text()
        densidad = densidad_text.text()
        resistividad = resistividad_text.text()

        # Verificar si algún campo está vacío
        if not all([longitud, diametro, material, voltaje]):
            raise ValueError("Falta ingresar uno o más datos.")

        # Verificar si los datos son numéricos
        try:
            # Intentar convertir a tipo float
            longitud = float(longitud)
            voltaje = float(voltaje)
            # Si el diámetro es personalizado, intentar convertir a tipo float
            if tipo_diametro_selector.currentText() == "Personalizado":
                diametro = float(diametro)
        except ValueError:
            raise ValueError("Error de conversión a número.")

        # Almacenar los datos en una lista
        datos = [longitud, diametro, material, densidad, resistividad, voltaje]

        # Mostrar los datos en la consola
        print("Datos guardados:", datos)

    except ValueError as e:
        # Mostrar mensaje de error en caso de excepción
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Error")
        mensaje.setText(f"Error al guardar datos: {str(e)}")
        mensaje.exec_()

# Crear la aplicación y la ventana principal
app = QApplication(sys.argv)
app.setStyle('Fusion')

window = QWidget()
window.setWindowTitle("Simulación de Cableado")

layout = QVBoxLayout()
form_layout = QFormLayout()

# Crear campos de entrada y opciones
longitud_input = QLineEdit()
longitud_input.setPlaceholderText("Longitud del cable (Metros)")
form_layout.addRow("Longitud del cable:", longitud_input)

tipo_diametro_selector = QComboBox()
tipo_diametro_selector.addItems(["Personalizado", "Tipo 1", "Tipo 2", "Tipo 3"])  # Agregar más tipos si es necesario
tipo_diametro_selector.currentIndexChanged.connect(cargar_tipo_diametro)
form_layout.addRow("Tipo de diámetro de cable:", tipo_diametro_selector)

diametro_input = QLineEdit()
diametro_input.setPlaceholderText("Diámetro del cable (Milímetros)")
diametro_input.setEnabled(True)  # Habilitar campo desde el inicio
form_layout.addRow("Diámetro del cable:", diametro_input)

material_cable = ['Oro', 'Plata', 'Cobre', 'Aluminio', 'Grafito']

material_input = QComboBox()
material_input.addItems(material_cable)
material_input.currentIndexChanged.connect(actualizar_densidad_resistividad)
form_layout.addRow("Material del cable:", material_input)

densidad_particulas_material = [5.90e28, 5.86e28, 8.50e28, 2.20e28, 11.2e28]

resistividad_material = [2.44e-8, 1.47e-8, 1.72e-8, 2.75e-8, 3.50e-5]

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

submit_button = QPushButton("Guardar datos")
submit_button.clicked.connect(guardar_datos)
finish_button = QPushButton("Cerrar")
finish_button.clicked.connect(cerrar_aplicacion)

# Agregar elementos al diseño de la ventana
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
