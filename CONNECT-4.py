def vsIA():
<<<<<<< HEAD
    return print("okey")

def JugadorvsJugador():
    return print ("vale")

def Historial():
    return print("okidoki")

controlMenu = False 
def Menu():
    print("******************************************")
    print("*              CONNECT-4                 *")
    print("******************************************")
    print("*         1. Jugador vs IA               *")
    print("*         2. Jugador vs Jugador          *")
    print("*         3. Historial de partidas       *")
    print("*         4. Salir del juego             *")
    print("******************************************")

controlMenu = False
Menu()
Opcion =int(input("Elige una opción: "))

while controlMenu == False:
    if Opcion == 1:
        vsIA()
        Menu()
        Opcion =int(input("Que desea hacer ahora: "))
    elif Opcion == 2:
        JugadorvsJugador()
        Menu()
        Opcion =int(input("Que desea hacer ahora: "))
    elif Opcion == 3:
        Historial()
        Menu()
        Opcion =int(input("Que desea hacer ahora: "))
    elif Opcion == 4:
        controlMenu = True
    elif Opcion !=1 or Opcion !=2 or Opcion !=3 or Opcion !=4 :
        Menu()
        Opcion = int(input="Valor incorrecto.Vuelva a introducir un valor: ")
    
=======
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

>>>>>>> 63aef16151dac9ad13eade9f97b744ec54d8856a
