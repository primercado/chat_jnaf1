import mysql.connector
from datetime import datetime


conexion = mysql.connector.connect (
    host="localhost",
    user="root",
    password="Pablomercado2023!",
    database='listas_despacho_jnaf1'
)

print(conexion)
cursor = conexion.cursor()

separador = '-' * 65
bienvenida = '| BIENVENIDOS AL JUZGADO DE NIÑEZ, ADOLESCENCIA Y FAMILIA N° 01 |'
print(separador)
print (bienvenida.center(65))
print(separador)


opcion = input(('Por favor, seleccione una de las siguientes opciones:\n1. Consultar la última fecha de despacho de un expediente.\n2. Listar la lista de despacho de una determinada fecha.\n'))

# Verificar la opción seleccionada y realizar la acción correspondiente
if opcion == "1":
    # Realizar acción para consultar fecha de despacho
    print("Ha seleccionado la opción 1: Consultar fecha de despacho de un expediente.\n")
    # Pedir expte al usuario
    expte = input('Por favor, ingrese el número de expediente: ')
    consulta = f"SELECT Fecha, Orden FROM despachos WHERE expediente = '{expte}' ORDER BY fecha DESC LIMIT 1"
    cursor.execute(consulta)
    # Obtener los resultados de la consulta
    resultados = cursor.fetchall()
    # Imprimir los resultados
    if len(resultados) > 0:
        print(f"El expediente {expte} salió en la lista de despacho del día {resultados[0][0]}, en el orden {resultados[0][1]}.")
        print('Muchas gracias por usar nuestro Servicios de Chat.')
    else:
        print(f"No se encontró el expediente {expte} en la lista de despacho.")
elif opcion == "2":
    # Realizar acción para listar la lista de despacho de determinada fecha
    print("Ha seleccionado la opción 2: Listar la lista de despacho de determinada fecha.\n")
    # Pedir fecha al usuario
    fecha_str = input("Por favor, ingrese la fecha que desea en formato DD/MM/AAAA: ")
    fecha = datetime.strptime(fecha_str, '%d/%m/%Y').date()
    fecha_sql = fecha.strftime('%Y-%m-%d')
    consulta_fecha = f"SELECT Orden, Expediente, Caratula FROM despachos WHERE Fecha = '{fecha_sql}'"
    cursor.execute(consulta_fecha)
    resultado_fecha = cursor.fetchall()
    encabezado = 'Lista de despacho'
    encabezado_1 = 'Juzgado de Niñez, Adolescencia y Familia n° 01'
    encabezado_2 =  f'Correspondiente al día:{fecha_str}'
    print(separador)
    print('|',encabezado.center(61),'|')
    print('|',encabezado_1.center(61),'|')
    print('|',encabezado_2.center(61),'|')
    print(separador)
    if len(resultado_fecha) > 0:
        for i in resultado_fecha:
            print (i)
    else:
        print (f"no se encontró la fecha {fecha_str}")
else:
    # Opción inválida
    print("Opción inválida. Por favor, seleccione una opción válida (1 o 2).")








   

