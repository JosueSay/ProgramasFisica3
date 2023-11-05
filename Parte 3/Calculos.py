import math

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
    










