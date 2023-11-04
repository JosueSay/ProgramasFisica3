import math

# Variables de entrada
longitud_cable = 0
diametro_cable = 0
voltaje = 0
resistividad = 0
densidad_particula = 0

# Valores conocidos
carga_electron = 1.6e-19
material_cable = ['oro', 'plata', 'cobre', 'aluminio', 'grafito']
densidad_particulas_material = [5.9e28, 5.86e28, 8.5e28, 2.2e28, 11.2e28]
resistividad_material = [2.44e-8, 1.47e-8, 1.72e-8, 2.75e-8, 3.5e-5]

diametrosMM_calibre_AWG_ = [
    11.684, 10.404, 9.266, 8.252, 7.348, 6.544, 5.827, 5.189, 4.621, 4.115,
    3.665, 3.264, 2.906, 2.588, 2.305, 2.053, 1.828, 1.628, 1.45, 1.291,
    1.15, 1.024, 0.912, 0.812, 0.723, 0.644, 0.573, 0.511, 0.455, 0.405,
    0.361, 0.321, 0.287, 0.255, 0.227, 0.202, 0.18, 0.16, 0.143, 0.127
]

numero_calibre_AWG = [
    'AWG 0000', 'AWG 000', 'AWG 00', 'AWG 0', 'AWG 1', 'AWG 2', 'AWG 3', 'AWG 4', 'AWG 5', 'AWG 6',
    'AWG 7', 'AWG 8', 'AWG 9', 'AWG 10', 'AWG 11', 'AWG 12', 'AWG 13', 'AWG 14', 'AWG 15', 'AWG 16',
    'AWG 17', 'AWG 18', 'AWG 19', 'AWG 20', 'AWG 21', 'AWG 22', 'AWG 23', 'AWG 24', 'AWG 25', 'AWG 26',
    'AWG 27', 'AWG 28', 'AWG 29', 'AWG 30', 'AWG 31', 'AWG 32', 'AWG 33', 'AWG 34', 'AWG 35', 'AWG 36'
]


# Cálculos

def dameResitencia(rho, l, d):
    R = (4 * rho * l) / (math.pi * d**2)
    return R

def dameCorriente(V, R):
    I = V / R
    return I

def damePotencia(V, R):
    P = (V ** 2) / R
    return P

def dameVelocidadArrastre(I, n, q, D):
    v_d = (4 * I) / (n * q * math.pi * D**2)
    return v_d

def dameTiempo(l, v):
    t = l / v
    return t
    










