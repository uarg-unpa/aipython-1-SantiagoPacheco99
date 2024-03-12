"""
print("Taller de AlPython P1 E2")
print() 
#Print() #error
#print( #error
#print #error

print("Hola","soy","Santiago")
print()
print("hola","soy","Santiago",sep="*")
print("Probando argumentos","soy el segundo argumento", end='*')
print("Soy otra linea")

print(6/3)  #Division
print(6//3) #Division entera
print(6%3) #Modulo
print(2**3) #Potencia

print(2+(9**2-(4//2)))

print(type(40))
print(type("hola"))

#Variables
primer_nombre='Santiago'
apellido_paterno='Pacheco'

print(apellido_paterno)

#Variables NO aceptadas
#primer-nombre
#primer@nombre
#primer$nombre
"""

"""
---------------------------------------------------------------------------------
print("Usando la funcion"+" print()")
print("Usando la funcion print()" *3)
"""
"""
edad = int(input("Ingrese su edad: "))

#print("Su edad es "+edad) #Forma incorrecta
#Forma correcta
print("Su edad es ",edad)
print("Su edad es "+ str(edad))
"""
"""
num1=10
num2=5
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} % {num2} = {num1%num2}")
print(f"{num1} / {num2} = {num1/num2}")
print(f"{num1} // {num2} = {num1//num2}")
print(F"{num1} ** {num2} = {num1**num2}")
"""

"""
texto = "EsTo eS uN texTo MeZclaDo"
#Funciones de cadenas

#tittle (Pone las primeras letras en mayusculas y las demas en minusculas)
print(texto.title())
#print(texto)
#texto = texto.title()
#print(texto)

#upper lower
print(texto.upper()) #Pone todo en mayuscula
print(texto.lower()) #Pone todo en minuscula

#replace
print(texto.replace(" ","-")) #Los espacios en blanco se pone el -

#len
print(len(texto)) #Longitud de la cadena
print(len('AIPython'))
"""
"""
#Inmutables

cadena = "AIPYTHON"
print(cadena[5])
#cadena[5]="h" #No se puede hacer por la inmutabilidad
"""

"""
frase = input("Ingrese una frase: ")
caracter = input("Ingrese un caracter: ")
#Buscar la primera aparicion del caracter
posicion = frase.find(caracter)

if posicion != -1:
    print(f"El caracter {caracter} se encuentra en la posicion {posicion+1}")
    subcadena = frase[posicion:]
    print(f"Subcadena a partir de la posicion {posicion+1}: {subcadena}")
else:
    print(f"El caracter {caracter} no se encuentra en la frase")
"""


num = int(input("Ingrese un numero: "))
while num > 0:
    if num%2==0:
        print("Finalizando el bucle")
        break
    num = int(input())


suma = 0
for i in range(1,30):
    print(i)
    if i > 10:
        continue 
    suma = suma+1
print(suma)
        





