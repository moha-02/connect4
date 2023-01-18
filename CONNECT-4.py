def vsIA():
    return "okey"

def JugadorvsJugador():
    return "vale"

def Historial():
    return "okidoki"

def salir():
    return breakpoint



print("******************************************")
print("*              CONNECT-4                 *")
print("******************************************")
print("*         1. Jugador vs IA               *")
print("*         2. Jugador vs Jugador          *")
print("*         3. Historial de partidas       *")
print("*         4. Salir del juego             *")
print("******************************************")
Opcion =int(input("Elige una opción: "))

if Opcion == 1:
    vsIA()

elif Opcion == 2:
    JugadorvsJugador()

elif Opcion == 3:
    Historial()

