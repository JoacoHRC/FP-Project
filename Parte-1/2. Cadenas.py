def invertCad(cad):
    newCad = ""
    for i in cad:
        newCad = i + newCad
    return newCad

if __name__ == '__main__':
    cadena = input("Ingrese una cadena: ")
    print("Cadena invertida:")
    print(invertCad(cadena))
