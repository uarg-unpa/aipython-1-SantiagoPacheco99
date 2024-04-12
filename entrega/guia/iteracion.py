contador = 0
while contador<=10:
    print(contador,end="-")
    contador = contador + 1
print()
print("Finde la iteracion")


#for
cadena = "AIPYTHON"
for letra in cadena:
    print(letra)

#range()
for num in range(10):
    print(num)

for indice in range(len(cadena)):
    print(cadena[indice])


#Imprimir 10 veces AIPYTHON
for _ in range(10):
    print("AIPYTHON") 
