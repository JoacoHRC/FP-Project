def escribir_datos(nombre_archivo, datos):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(datos)
            print(f"Datos escritos en el archivo {nombre_archivo}.")
    except Exception as e:
        print(f"Ocurrió un error al escribir en el archivo: {e}")

def leer_datos(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = archivo.read()
            print(f"Datos leídos desde el archivo {nombre_archivo}:")
            print(datos)
            return datos
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

# Solicitar al usuario el nombre del archivo y los datos a escribir
nombre_archivo = input("Ingrese el nombre del archivo: ")
datos_a_escribir = input("Ingrese el texto que desea escribir en el archivo: ")

# Escribir datos en el archivo
escribir_datos(nombre_archivo, datos_a_escribir)

# Leer datos desde el archivo
datos_leidos = leer_datos(nombre_archivo)
