import turtle
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# Función para calcular el campo eléctrico mediante una integral
def electric_field_integral(Q, epsilon, H, R, d):
    integrand = lambda x: (1 - (H - x + d) / np.sqrt((H - x + d)**2 + (R - R * x / H)**2))
    result, _ = integrate.quad(integrand, 0, H)
    E = (3 * Q) / (2 * np.pi * epsilon) * result
    return E

# Pedir valores de entrada al usuario
Q = float(input("Ingrese la carga (Q en Coulombs): "))  # Carga en Coulombs
epsilon = 8.854187817e-12  # Permitividad del vacío
H = float(input("Ingrese la altura del cono (H en metros): "))  # Altura del cono en metros
R = float(input("Ingrese el radio del cono (R en metros): "))  # Radio del cono en metros

# Inicializar la variable d
d = 0

def DibujarCono(altura, radio, x, y):
    # Configuración inicial
    turtle.penup()
    turtle.goto(x, -radio)


    # Dibujar la base del cono (círculo)
    turtle.pendown()
    turtle.circle(radio)

    turtle.penup()
    turtle.goto(x, radio)
    turtle.pendown()
    turtle.goto(altura, y)
    turtle.penup()
    turtle.goto(x, -radio)
    turtle.pendown()
    turtle.goto(altura, y)
    turtle.penup()
    turtle.goto(-radio, y)
    turtle.pendown()
    turtle.goto(altura, y)
    turtle.penup()


# Función para manejar el evento de clic en el plano
def show_coordinates(x, y):
    global d  # Utilizar la variable global d
    
    if x < 0:
         E_result = round(electric_field_integral(Q, epsilon, H, R, abs(x)-H))
    else:
        d = x - H  # Actualizar la coordenada x en la variable d
        # Calcular el campo eléctrico utilizando la función electric_field_integral
        E_result = round(electric_field_integral(Q, epsilon, H, R, d))
    
    # Mostrar el resultado en el lienzo
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.dot(10, "red")  # Dibuja un punto rojo en el lugar del clic
    
    # Dibujar flecha proporcional a la magnitud del campo eléctrico
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("red")  # Cambiar el color de la flecha a rojo
    
    if x < 0:
        pen.setheading(180)  # Establecer dirección hacia la izquierda
    else:
        pen.setheading(0)  # Establecer dirección hacia la derecha

    pen.pensize(3)
    pen.forward(E_result * 0.000000001)  # Dibujar flecha proporcional a E_result (ajusta el factor según tu preferencia)
    pen.goto(x, y)  # Volver al punto de inicio de la flecha
    pen.setheading(90)  # Apuntar hacia arriba
    pen.forward(10)  # Mover hacia arriba para formar la cabeza de la flecha
    pen.penup()
    
    # Mostrar coordenadas y el valor del campo eléctrico
    pen.goto(x + 10, y + 10)  # Coloca el cursor al lado del punto para escribir las coordenadas
    pen.pendown()
    pen.color("red")  # Cambiar el color del texto a rojo
    pen.write(f"({x}, {y}), E = {E_result} N/C", align="left", font=("Arial", 12, "bold"))

# Función para dibujar la cuadrícula según los valores del eje x
def draw_x_grid_lines():
    pen.pencolor("gray")
    pen.pensize(1)  # Grosor de la línea de la cuadrícula
    for i in range(-300, 301, 50):
        pen.penup()
        pen.goto(i, -250)
        pen.pendown()
        pen.goto(i, 250)

# Función para dibujar la cuadrícula según los valores del eje y
def draw_y_grid_lines():
    pen.pencolor("gray")
    pen.pensize(1)  # Grosor de la línea de la cuadrícula
    for i in range(-250, 251, 50):
        pen.penup()
        pen.goto(-350, i)
        pen.pendown()
        pen.goto(350, i)

# Función para dibujar una línea de cuadrícula
def draw_grid_line(start_x, start_y, end_x, end_y):
    pen.penup()
    pen.goto(start_x, start_y)
    pen.pendown()
    pen.setundobuffer(1)  # Configuración para puntos punteados
    pen.pensize(1)  # Grosor de la línea
    pen.pendown()
    pen.dot(2, "gray")  # Dibuja un punto punteado en lugar de una línea
    pen.setundobuffer(0)  # Restaurar configuración
    pen.pensize(2)  # Restaurar grosor de línea




# Configuración inicial
window = turtle.Screen()
window.setup(width=800, height=600)
window.title("CAMPO ELECTRICO DE UN CONO")

# Crear el objeto Turtle
pen = turtle.Turtle()
pen.speed(0)  # Velocidad máxima

# Dibujar ejes x y y más gruesos
pen.pensize(2)
pen.penup()
pen.goto(-350, 0)
pen.pendown()
pen.forward(700)
pen.penup()
pen.goto(0, -250)
pen.setheading(90)
pen.pendown()
pen.forward(500)

# Etiquetas de los ejes
pen.penup()
pen.goto(-370, -10)
pen.pendown()
pen.write("0", align="center")
pen.penup()
pen.goto(370, -10)
pen.pendown()
pen.write("X", align="center")
pen.penup()
pen.goto(-20, 270)
pen.pendown()
pen.write("Y", align="center")

# Dibujar divisiones y valores en los ejes
for i in range(-300, 301, 50):
    pen.penup()
    pen.goto(i, -5)
    pen.pendown()
    pen.goto(i, 5)
    if i != 0:
        pen.penup()
        pen.goto(i - 10, -20)
        pen.pendown()
        pen.write(str(i), align="center")
for i in range(-250, 251, 50):
    pen.penup()
    pen.goto(-15, i)
    pen.pendown()
    pen.goto(15, i)
    if i != 0:
        pen.penup()
        pen.goto(-40, i - 10)
        pen.pendown()
        pen.write(str(i), align="center")

# Dibujar la cuadrícula...
draw_x_grid_lines()
draw_y_grid_lines()
DibujarCono(H, R, 0, 0)

# Asignar la función de clic al plano
window.onclick(show_coordinates)

# Mantener la ventana abierta hasta que se cierre manualmente
turtle.done()
