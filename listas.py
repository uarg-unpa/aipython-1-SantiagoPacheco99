#Listas
#Creacion lista vacia
"""
nombres = []

#Valores iniciales

nombres = ["Santiago","Joaquin",21,9,12,"Pacheco"]

#Mostrar lista
print(nombres)

#Iterar sobre la lista usando indices
for i in range(len(nombres)):
    print(nombres[i])

#Accedemos a los elementoa

#Accedemos al primer elemento
primerElemento = nombres[0]

print(f"El primer elemento es: {primerElemento}")
"""

"""
#Creacion de listas usando el metodo

#nombres = list()

#Crear una lista con valores iniciales


nombres = list(["Villarroel","Edul","Julian"])


#Metodos, append, permite agregar un elemento al final de la lista

nombres.append("Alberto")
print(nombres)

#Insert
nombres.insert(0,"Sandra")
print(nombres)


#Utilizar el operador in
for nombre in nombres:
    print(nombre,end=" ")

#mutabilidad 
print()
nombres [4] = "Lorenzo"
for nombre in nombres:
    print(nombre,end=" ")

print(id(nombres))


#id
num = 40
print(id(num))
num = 22
print(id(num))
"""

#rebanadas
numeros=[2,6,-2,-5,3,8]
sub_numeros = numeros[:3]
print(sub_numeros)
