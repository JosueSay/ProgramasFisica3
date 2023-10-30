import turtle
while True:
    print("SIMULADOR DE CAMPO ELECTRICO CON VOLUMENES SIMETRICOS")
    print("0. Salir")
    print("1. Cono")
    print("2. Cono truncado")
    print("3. Hemisferio")
    
    
    choice = input("Ingrese el número correspondiente a la opción deseada: ")
    
    if choice == "1":
        print()
        import Cono
         
        print()
    elif choice == "2":
        print()
        import Cono2
         
        print()
    elif choice == "3":
        print()
        import Hemisferio
         
        print()
    elif choice == "0":
        print()
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
