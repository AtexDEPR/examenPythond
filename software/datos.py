import datetime
import menus

def copia_de_factura(codigo_factura):
    
    print('')
    print('=' * 40)
    print('')
    print('*** COPIA DE FACTURA ***')
    print('')
    print('Datos del cliente:')
    print('[]')
    print('')
    print('')
    print('Datos de la factura')
    print(f'[Codigo : {codigo_factura}]')
    print('')
    print('')
    print('')
    print('')
    print('')
    return copia_de_factura

def factura_mes():
    data = open('software/ventas.dat', 'r')
    mes = input('Ingrese el mes donde quiere imprimir las facturas de un cliente (2 digitos, ejemplo 01):  ')  # Solicita el mes
    codigo = input('Ingrese el codigo del cliente:  ')
    factura_mes_mes = [codigo,data
    ]
    if factura_mes_mes:
        True
    else:
        False

    return menus.facturas_set_mes(mes, codigo)

def Listado_productos_mas_comprados():
    print('None')

