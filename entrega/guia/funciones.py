"""
def mensaje():
    print("Hola - AIPython")

mensaje()
"""

"""
def suma():
    return (4 + 6)

#suma() #Devuelve 10
#suma(3) #Devuelve Error porque no fue definido en la funcion
"""

"""
def suma(num1,num2):
    return num1 + num2

print(suma(7,3))
"""
"""
def presentacion (nombre, apellido):
    print(f"Su nombre es: {nombre}, y su apellido es: {apellido}")

presentacion("Santiago","Pacheco")
presentacion(nombre="Santiago",apellido="Pacheco")
"""


def suma(num1=2, num2=4):
    return num1 + num2

print(suma()) #Devuelve 6


