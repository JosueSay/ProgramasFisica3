# P_Plano.py

def procesar_datos(datos):
    # Imprime los datos recibidos
    print("Datos recibidos en P_Plano:", datos)
    
    # Verifica si hay elementos en los datos
    if len(datos) > 1:
        # Convierte los datos a decimales, excepto el primer elemento
        datos_decimales = [datos[0]] + [float(dato) for dato in datos[1:]]
        print("Datos decimales en P_Plano:", datos_decimales)
        # Realiza el procesamiento correspondiente para el cálculo del plano
    else:
        print("\033[91mNo hay suficientes datos para procesar en P_Plano\033[0m")

