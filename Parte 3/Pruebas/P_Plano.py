from vpython import sphere, box, vector, color, rate

# Crear una esfera
mi_esfera = sphere(pos=vector(0, 0, 0), radius=1, color=color.blue)

# Crear un plano (representado por una caja)
mi_plano = box(pos=vector(0, -2, 0), size=vector(5, 0.01, 5), color=color.green)

# Rotar la esfera y el plano
while True:
    mi_esfera.rotate(angle=0.03)
    mi_plano.rotate(angle=-0.02)
    rate(100)
