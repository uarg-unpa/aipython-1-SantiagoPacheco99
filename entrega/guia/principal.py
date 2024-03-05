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

edad = int(input("Ingrese su edad: "))

#print("Su edad es "+edad) #Forma incorrecta
#Forma correcta
print("Su edad es ",edad)
print("Su edad es "+ str(edad))
