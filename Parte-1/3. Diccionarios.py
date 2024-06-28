# Definición de la agenda telefónica como un diccionario
agenda = {}

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Agenda Telefónica ---")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Editar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar todos los contactos")
    print("6. Salir")

# Función para añadir un contacto
def añadir_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    agenda[nombre] = telefono
    print(f"Contacto {nombre} añadido con éxito.")

# Función para buscar un contacto
def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto que desea buscar: ")
    if nombre in agenda:
        print(f"El número de teléfono de {nombre} es {agenda[nombre]}.")
    else:
        print(f"El contacto {nombre} no se encuentra en la agenda.")

# Función para editar un contacto
def editar_contacto():
    nombre = input("Ingrese el nombre del contacto que desea editar: ")
    if nombre in agenda:
        telefono = input(f"Ingrese el nuevo número de teléfono para {nombre}: ")
        agenda[nombre] = telefono
        print(f"Contacto {nombre} actualizado con éxito.")
    else:
        print(f"El contacto {nombre} no se encuentra en la agenda.")

# Función para eliminar un contacto
def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado con éxito.")
    else:
        print(f"El contacto {nombre} no se encuentra en la agenda.")

# Función para mostrar todos los contactos
def mostrar_todos_los_contactos():
    if agenda:
        print("\n--- Lista de Contactos ---")
        for nombre, telefono in agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
    else:
        print("La agenda está vacía.")

# Función principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")
        if opcion == '1':
            añadir_contacto()
        elif opcion == '2':
            buscar_contacto()
        elif opcion == '3':
            editar_contacto()
        elif opcion == '4':
            eliminar_contacto()
        elif opcion == '5':
            mostrar_todos_los_contactos()
        elif opcion == '6':
            print("Saliendo de la agenda. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

# Ejecución del programa principal
if __name__ == "__main__":
    main()


