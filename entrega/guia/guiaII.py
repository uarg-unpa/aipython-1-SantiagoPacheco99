"""
#Punto 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Tiene edad suficiente para conducir")
else:
    print(f"Le faltan {18-edad} años para poder conducir")
"""
"""
#Punto 4
a=int(input("Ingrese un numero para a: "))
b=int(input("Ingrese otro numero para b: "))

if a>b:
    print("a es mayor que b")
elif a<b:
    print("a es menor que b")
else:
    print("a es igual a b")
"""

"""
#Punto 5
n = int(input("Ingrese un numero: "))
if n%2==0:
    print(f"{n} es un numero par")
else:
    print(f"{n} es un numero impar")
"""
n=int(input("Ingrese un numero del 1 al 7: "))
if n>=1 and n<=7:
    match n:
        case 1:
            print("Lunes")
        case 2:
            print("Martes")
        case 3:
            print("Miercoles")
        case 4:
            print("Jueves")
        case 5:
            print("Viernes")
        case 6:
            print("Sabado")
        case 7:
            print("Domingo")
else:
    print("")