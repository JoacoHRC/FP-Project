class Persona:
    def __init__    (self, nombre, edad): #No es  necesario agregar el __init__, pero es una práctica común y recomendada en Python para inicializar los atributos de una clase.
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Solicitar datos al usuario
nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))

# Crear una instancia de la clase Persona con los datos ingresados
persona1 = Persona(nombre, edad)

# Mostrar los datos
persona1.mostrar_datos()
