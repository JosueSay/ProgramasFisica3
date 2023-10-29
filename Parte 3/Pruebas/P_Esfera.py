# P_Esfera.py

def procesar_datos(datos):
    # Imprime los datos recibidos
    print("Datos recibidos en P_Esfera:", datos)
    
    # Verifica si hay elementos en los datos
    if len(datos) > 1:
        # Convierte los datos a decimales, excepto el primer elemento
        datos_decimales = [datos[0]] + [float(dato) for dato in datos[1:]]
        print("Datos decimales en P_Esfera:", datos_decimales)
        # Realiza el procesamiento correspondiente para el cálculo de la esfera
    else:
        print("\033[91mNo hay suficientes datos para procesar en P_Esfera\033[0m")

