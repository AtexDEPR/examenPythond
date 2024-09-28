def menu():
    while True:
        print('')
        print("--------------------------------------------+")
        print("** MENU PRINCIPAL **                        |")
        print("                                            |")
        print("1) Copia de una factura                     |")
        print("2) Resumen de todas la facturas (1 cliente) |")
        print("3) Inforrme diagrama de barras              |")
        print("4) Poductos mas comprados                   |")
        print("5) Salir del sistema...                     |")
        print(">>> Seleccione una opcion del menu          |")
        print("--------------------------------------------+")
        print(">>> opcion? ")
        
        try:
            opcion = int(input("")) # Solicita al usuario que ingrese una opción.

            if opcion <1 or opcion > 5:
                print("Error. Opcion no valida.") # Mensaje de error si la opción no es válida.
                input("presione cualquier tecla para volver al menu ...")
                continue # Vuelve al inicio del menú.
            return opcion # Retorna la opción válida.
        except ValueError:
            print("Error. Opcion no valida.") # Mensaje de error si la entrada no es un número válido.
            input("presione cualquier tecla para volver al menu ...")

def facturas_set_mes(mes,codigo):
    print('=' * 40)
    print(f'*** FACTURAS DEL MES {mes}, DEL CLIENTE {codigo} ***')
    print('[]\n' * 15)

def diagrama_de_barras():
    print('====================')
    print('  FACTURACIÓN DEL 2024')
    print('====================')
    print(' ')
    print(' MESES')
    print('-------------')
    print('06 ****')
    print('07 ****')
    print('08 ********************')
    print('09 ******************')