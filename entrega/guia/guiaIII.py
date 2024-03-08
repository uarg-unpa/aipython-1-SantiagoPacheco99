"""
#Punto 1
i = int(0)
while(i<=100):
    print(i)
    i = i + 1
"""

"""
#Punto 2
for num in range(0,101):
    print(num, end=" ")
"""

"""
#Punto 3
i = int(10)
while(i>=0):
    print(i)
    i = i - 1


for num in range(10,-1,-1):
    print(num)
"""

"""
#Punto 5
i = int(1)
while(i<=7):
    print("#"*i)
    i = i+1
"""
"""
#Punto 6

for _ in range(7):
    for _ in range(7):
        print("#",end="")
    print("#")
print()
"""


"""
#Punto 7
nombre = input("Ingrese su nombre: ")
i = int(input("Ingrese un numero: "))
for ind in range(1,i+1):
    print(nombre*ind)
"""

"""
#Punto 9

i = int(0)
while(i<=10):
    resul = i * i
    print(f"{i} x {i} = {resul}")
    i = i + 1

for num in range(0,11):
    resultado = num * num
    print(f"{num} x {num} = {resultado}")
"""

"""
#Punto 10
for i in range(0,7):
    print(f"0 {i}")
"""

"""
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
if num1 < num2:
    for i in range(num1,num2):
        if i%2 == 0:
            print(i)
else:
    for i in range(num2,num1):
        if i%2 == 0:
            print(i)
"""

"""
#Punto 12
N = int(input("Ingrese un numero: "))
i=int(1)
resultado = int(0)
while(i<=N):
    if i<N:
        print(f"{i} +",end=" ")
    else:
        print(f"{i}",end=" ")
    resultado = resultado + i
    i = i + 1
print(f"= {resultado}")

#Con for
N = int(input("Ingrese un numero: "))
resultado = int(0)
for num in range(1,N+1):
    if num<N:
        print(f"{num} +",end=" ")
    else:
        print(f"{num}",end=" ")
    resultado = resultado + num
print(f"= {resultado}")
"""
"""
#Punto 13
N = int(input("Ingrese un número natural: "))
resultado = int(0)
for num in range(0,N+1,2):
    resultado = resultado + num
print(f"El numero elegido {N}, su suma de los numeros enteros pares es: {resultado}")
"""









