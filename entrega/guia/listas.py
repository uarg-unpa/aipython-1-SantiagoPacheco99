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

"""
#rebanadas
numeros=[2,6,-2,-5,3,8]
sub_numeros = numeros[:3]
print(sub_numeros)
"""



#Palabra del

web = ["HTML","CSS","JS","Node","MongBD"]
"""
print(web)
del web[2] #Borra JS
print(web)

del web #Elimina toda la lista
print(web)


#Metodo remove
print(web)
web.remove("JS") #Busca el elemento que le pasamos por parametro
print(web)
"""

"""
#Metodo pop

print(web)
web.pop() #Elimina el ultimo elemento
print(web)
web.pop(0) #Busca el elemento que le indicamos con el indice en el parametro
print(web)
"""

"""
#Metodo index

print(web.index("CSS")) #Nos da el indice de donde esta ese elemento en la lista
"""

"""
#Rebanadas en listas
sub_web = web[:3]   #El cuarto elemento no se incluye (En este caso no se incluye Node)
print(sub_web)
"""


