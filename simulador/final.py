import random


print("****************************************************")
print("*** BIENVENIDOS AL JUEGO DE LANZAMIENTO DE DADOS ***")
print("****************************************************")
print("")
print("Antes de jugar debe definir lo siguiente: ")
print("1-Cantidad de dados para jugar")
print("2-Cantidad de caras que tendran los dados")
print("3-Ingresar nombre de los jugadores")

def lanzamiento(caras): #Metodo que retorna un numero al azar entre el 1 y las caras definidas por el usuario
    return random.randint(1,caras)


cant_dados = int(input("Ingrese la cantidad de dados para jugar: "))

def ingresar_jugadores(cant,jug):
    for i in range(cant):
        jug.append()

def mostrar_jugadores(jug):
    for j in jug:
        return j

def juego():
    jugadores = []
    print("[1]-Para ver las reglas del juego")
    print("[2]-Para empezar a jugar")
    print("[3]-Para mostrar las estadisticas de los jugadores")
    print("[4]-Para mostrar los jugadores")
    while(op != 0):
        op = int(input("Ingrese la opcion: "))
        match op:
            case 1:

            case 2:
                
            case 3:

            case 4:
                print(f"Jugador:{mostrar_jugadores(jugadores)}")
            case 0:
                print("Usted ha salido del juego")
            case _:
                print("Error. Opcion no existente")


juego()




















