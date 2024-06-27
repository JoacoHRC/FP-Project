def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def producto(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "ERROR! No se puede dividir entre 0."

def calculadora():
    while True:
        print("Calculadora simple: ")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

        op = input("Seleccione la operacion que desea realizar (1-5): ")

        while op not in ['1', '2', '3', '4', '5']:
            print("Entrada no valida. Intente nuevamente.")
            op = input("Seleccione la operacion que desea realizar (1-5): ")

        if op == '5':
            print("Saliendo...")
            break
        
        num1 = float(input("Ingrese el valor del primer numero: "))
        num2 = float(input("Ingrese el valor del segundo numero: "))

        if op == '1':
            resultado = suma(num1, num2)
            print(f"La suma de {num1} y {num2} es: {resultado}")
        elif op == '2':
            resultado = resta(num1, num2)
            print(f"La diferencia entre {num1} y {num2} es: {resultado}")
        elif op == '3':
            resultado = producto(num1, num2)
            print(f"El producto de {num1} y {num2} es: {resultado}")
        elif op == '4':
            resultado = division(num1, num2)
            print(f"El cociente entre {num1} y {num2} es: {resultado}")

calculadora()