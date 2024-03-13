"""
#Punto 1

def producto(num1,num2):
    return num1 * num2

print(producto(4,5))
"""
"""
#Punto 3

def mensaje(nombre):
    print(f"{nombre} se puede describir en 5 letras: CRACK")

nom = input("Ingrese su nombre: ")

mensaje(nom)
"""

"""
#Punto 4

def tabla_multiplicar(num):
    for i in range(1,11):
       resultado = num * i
       print(f"{num} x {i} = {resultado}")

numero = int(input("Ingrese el numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)
"""

"""
#Punto 5

def par_impar(n):
    if n % 2 == 0:
        print(f"El numero {n} es par")
    else:
        print(f"El numero {n} es impar")


num = int(input("Ingrese un numero para determinar si es par o impar: "))
par_impar(num)
"""

"""
#Punto 6
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact= fact * i
    return fact
n = int(input("Ingrese un numero: "))
print(f"El resultado de {n}! = {factorial(n)}")
"""
"""
#Punto 7

def maximo(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    else:
        return n3

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un segundo numero: "))
num3 = int(input("Ingrese un tercer numero: "))


print(f"El numero maximo entre {num1},{num2} y {num3} es: {maximo(num1,num2,num3)}")
"""

"""
#Punto 8

def invertir(palabra):
    print(palabra)
    print(palabra[::-1])


pal = input("Ingrese una palabra: ")
invertir(pal)
"""

"""
#Punto 9

def palindromo(p):
    if(p.lower() == p.lower()[::-1]):
        return "Es palindromo"
    else:
        return "No es palindromo"

palabra = input("Ingrese una palabra: ")
print(palindromo(palabra))
"""

"""
#Punto 10
def temp(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

tempetarura = float(input("Ingrese la temperatura (en grados fahrenheit): "))
print(f"La temperatura {tempetarura}°F a grados celsius es de: {temp(tempetarura)}°C")
"""










