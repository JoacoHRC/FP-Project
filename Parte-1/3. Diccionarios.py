agenda = {
    "usuario": 903231474,
    "Hola": 98978542516,

}

def nombre():
    name = input("Inserte un nombre: ")
    return name

def numero():
    num = int(input("Inserte un numero: "))
    return num

def add_contact(name,num):
    agenda[name] = num

def add():
    name = input("Ingrese un nombre: ")
    num = int(input("Ingrese un numero: "))
    add_contact(name, num)

def delete_contact(name):
    agenda.pop(name, -1)

def delete(agenda):
    show(agenda)
    name = input("Ingrese el nombre del contacto a eliminar")
    delete_contact(name)

def show(agenda):
    for contact in agenda.keys():
        print(contact, " : ", agenda.get(contact))
    input("Presione ENTER para continuar...")


if __name__ == '__main__':
    while True:
        print(
            "Bienvenido a su agenda de contactos, por favor, ingrese una opcion\n"
            "\t1) Ingresar un contacto\n"
            "\t2) Eliminar un contacto\n"
            "\t3) Mostrar contactos\n"
        )
        opcion = int(input())
        if opcion == 1:
            add()
        if opcion == 2:
            delete(agenda)
        if opcion == 3:
            show(agenda)

