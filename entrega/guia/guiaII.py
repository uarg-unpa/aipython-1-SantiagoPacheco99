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
"""
n=int(input("Ingrese un numero del 1 al 7: "))
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
    case _:
        print(F"{n} no está permitido")
"""
"""
#Punto 7
calificacion=int(input("Ingrese calificacion: "))

if calificacion >=90 and calificacion <=100:
    print("A")
elif calificacion >=70 and calificacion <=89:
    print("B")
elif calificacion >=60 and calificacion<=69:
    print("C")
elif calificacion >= 50 and calificacion <=59:
    print("D")
elif calificacion>=0 and calificacion<=49:
    print("F")
else:
    print("Numero no permitido")
"""

#Punto 8
edad = int(input("Ingrese la edad: "))
if edad < 4:
    print("El cliente tiene entrada gratis")
elif edad >=4 and edad<= 18:
    print("El cliente debe pagar $5")
else:
    print("El cliente debe pagar $10")



#Punto 9

