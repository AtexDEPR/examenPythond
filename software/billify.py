import menus
import datos


def clear_screen():
    print('\n' *  50)


while True:
    
    while True:
        op = menus.menu()
        match op:
            case 1:
                clear_screen()
                codigo_factura = int(input('Ingrese el codigo de la factura:  '))
                datos.copia_de_factura(codigo_factura)
                print('\n\n\n\n\n')
            case 2:
                clear_screen()
                datos.factura_mes()
                print('\n\n\n\n\n')
            case 3:
                clear_screen()
                menus.diagrama_de_barras()
                print('\n\n\n\n\n')
            case 4:
                clear_screen()
                datos.Listado_productos_mas_comprados()
                print('\n\n\n\n\n')
            case 5:
                clear_screen()
                print('Gracias por usar el software . . .')
                break

    break