def mcd(numero1, numero2):
    if numero1 == 0:
        return numero2
    return mcd(numero2 % numero1, numero1)


if __name__ == '__main__':
    print("Binenvenido, ingrese 2 numeros")
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    print(mcd(num1, num2))
