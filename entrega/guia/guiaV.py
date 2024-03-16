"""
#Punto 1
lista = []

#Punto 2

l = [1,2,3,4,5,6,7]
"""

"""
#Punto 3

lis = [1,2,3]
print(len(lis))
"""

"""
#Punto 4
frutas = ["Frutilla","Manzana","Banana","Durazno"]
print(len(frutas))
print(frutas)
frutas.pop(0)
frutas.append("Pera")
print(frutas)
"""

"""
#Punto 5
lis = [1,2,3,4,5]
print(lis[0])
i = len(lis)//2
print(lis[i])
print(lis[-1])
"""

"""
#Punto 6

datos_personales = ["Santiago",21,1.74,"soltero","Las Piedras 226"]
"""
"""
#Punto 7
flores= ["rosas","orquídea","lirio","tulipan","margarita","dalia","hortensia"]

print(flores[2:])
"""


"""
#Punto 8
num = [1,2,3,4,5,6,7,8,9,10]
num_b = num[:3]
print(num_b)
"""

"""
#Punto 9
letras = ["a","b","c","d","e","f","g","h","i","j"]

segundos_elementos = letras[1::2]

print(segundos_elementos)
"""

"""
#Punto 10

clubes = ["River Plate","Boca Juniors","Independiente","Racing","San Lorenzo"]
clubes_inversa = clubes[::-1]
print(clubes_inversa)
"""

"""
#Punto 11
numeros = [1,2,3,4,5,6,7,8,9,10]
sub_num = numeros[:3]
print(sub_num)
"""
"""
#Punto 12
flores= ["rosas","orquídea","lirio","tulipan","margarita","dalia","hortensia"]

for flor in flores:
"""
"""
#Punto 13
def vocales(palabras):
    cont = 0
    for i in palabras:
        if(palabras[i].lower == "a" or  palabras[i].lower == "e" or palabras[i].lower == "i" or palabras[i].lower == "o" or palabras[i].lower == "u"):
            cont = cont + 1
    return cont
"""



"""
#Punto 14

def lista_union(lista1,lista2):
    lista = lista1 + lista2
    return lista

nombres = ["Santiago", "Lionel", "Julian", "Ignacio"]
apellidos = ["Pacheco", "Messi","Alvarez","Scocco"]
print(lista_union(nombres,apellidos))
"""

"""
#Punto 15
def promedio(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    prom = suma/len(lista)
    return prom

numeros = [1,2,3,4,5,6,7,8,9,10]
print(f"Promedio: {promedio(numeros)}")
"""
