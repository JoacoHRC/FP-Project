import math
import datetime
import random

def factorial(numero):
    if numero>= 1:
        return numero*factorial(numero-1);
    return 1;

def MCD(numero1,numero2):
    if numero1 == 0:
        return numero2;
    return MCD(numero2 % numero1, numero1);

MICONSTANTE = 20;
nombre = "Luis";
print(random.randrange(1,12,4));
print(nombre[0:2]);
print("Edad: %2d" % 20);
print("Hola a todos");
print("Python", "es uno de los lenguajes");
print("Python\nEs un lenguaje interpretado");
print("="*100);
print("La version actual de python es:{0:.1f} fue creado por{1}-{1}".format(3.3, "Guido Van Rossum"));

if __name__ == '__main__':
    print('hola');
    print(factorial(5));
    print(MCD(12,6));