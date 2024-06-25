def invertCad(cad):
    newCad = ""
    for i in cad:
        newCad = i + newCad
    return newCad

def vocales(cad):
    count = 0
    for i in cad:
        if i == "a":
            count += 1
        elif i == "e":
            count += 1
        elif i == "i":
            count += 1
        elif i == "o":
            count += 1
        elif i == "u":
            count += 1
    return count


if __name__ == '__main__':
    print(invertCad("hola"))
    print(vocales("holacamarera"))