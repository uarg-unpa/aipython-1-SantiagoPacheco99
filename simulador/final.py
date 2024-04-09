import random

#Metodo que retorna un numero al azar entre el 1 y las caras definidas por el usuario
def lanzamiento(caras): 
    return random.randint(1,caras)

#Metodo que lanza los dados
def lanzamientos_dados(dados, caras, lanzamientos, result):
    print("Ingrese l para lanzar o s para salir")
    lanzar = input("Lanzar: ")
    for l in range(lanzamientos):
        if(lanzar == "l"):
            print(f"Lanzamiento N°{l + 1}:")
            for d in range(dados):
                dado = lanzamiento(caras)
                print(f"Dado N°{d + 1}: {dado}")
                result.append(dado)
            lanzar = input("Presiona l para lanzar de nuevo o s para salir: ")
            if (lanzar == "s"):
                break
        elif (lanzar == "s"):
            break
    return result

#Metodo que muestra la suma total de los tiros
def total_resultado(result):
    suma = 0
    for i in result:
        suma = suma + i 
    return suma

#Metodo que retorna el numero mayor de la lista (el mejor tiro)
def mejor_tiro(result):
    max = 0
    for i in result:
        if i > max:
            max = i
    return max    

#Metodo que retorna el numero menor de la lista (el peor tiro)
def peor_tiro(result):
    men = result[0]
    for i in result:
        if i < men:
            men = i
    return men

#Metodo que muestra todos las caras de los dados de todos los tiros
def recorrer_tiros(tiros):
    for t in tiros:
        print(t,end="-")

def juego_dados():
    print("****************************************************")
    print("*** BIENVENIDOS AL JUEGO DE LANZAMIENTO DE DADOS ***")
    print("****************************************************")
    print("")
    print("Antes de jugar debe definir lo siguiente: ")
    print("1-Cantidad de dados para jugar")
    print("2-Cantidad de caras que tendran los dados")
    print("3-Ingresar cantidad de tiros")
    print("4-Ingresar nombre del jugador")


    cant_dados = int(input("Ingrese la cantidad de dados para jugar: "))
    caras = int(input("Ingrese la cantidad de caras que tendran los dados: "))
    cant_tiros = int(input("Ingrese la cantidad de tiros que tendra el jugador: "))
    jugador = input("Ingrese el nombre del jugador: ")
    resultados = []
    op = -1
    print()
    while(op!=0):
        print("[1]-Para ver las reglas del juego")
        print("[2]-Para empezar a jugar")
        print("[3]-Para mostrar las estadisticas del jugador")
        op = int(input("Ingrese la opcion: "))
        match op:
            case 1:
                print("==========================================================================")
                print("\t            ****REGLAS****")
                print(f"1-El jugador tiene {cant_tiros} cantidad de tiros de dados")
                print(f"2-El jugador en cada tiro tendrá {cant_dados} dados para lanzar")
                print("3-Cuando un jugador termine de lanzar, se sumará el resultado de sus tiros")
                print("\t        ****¡¡DIVIERTETE!!****")
                print("==========================================================================")
            case 2:
                resultados = []
                print("================================================================")
                print("\t****COMIENZA EL JUEGO****")
                lanzamientos_dados(cant_dados,caras,cant_tiros,resultados)
                print("\t****JUEGO TERMINADO****")
                print("================================================================")
            case 3:
                print("==================================================")
                print("****ESTADISTICAS****")
                print(f"Estadisticas del jugador {jugador}:")
                print("")
                print("Tiros: ",end="")
                recorrer_tiros(resultados)
                print("")
                print(f"Mejor tiro: {mejor_tiro(resultados)}")
                print(f"Peor tiro: {peor_tiro(resultados)}")
                print(f"Total: {total_resultado(resultados)}")
                print("==================================================")
            case 0:
                print("Usted ha salido del juego")
            case _:
                print("Error. Opcion no existente, vuelva a ingresar una opcion!!")

juego_dados()


