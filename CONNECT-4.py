'''
def vsIA():
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
    
'''
print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A","B","C","D","E","F","G"]
gameBoard = [["","","","","","",""], ["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
rows = 6
cols = 7

def printGameBoard():
  print("\n     A    B    C    D    E    F    G  ", end="")
  for x in range(rows):
    print("\n   +----+----+----+----+----+----+----+")
    print(x, " |", end="")
    for y in range(cols):
      if(gameBoard[x][y] == "🔵"):
        print("",gameBoard[x][y], end=" |")
      elif(gameBoard[x][y] == "🔴"):
        print("", gameBoard[x][y], end=" |")
      else:
        print(" ", gameBoard[x][y], end="  |")
  print("\n   +----+----+----+----+----+----+----+")

def modifyTurn(spacePicked, turn):
  gameBoard[spacePicked[0]][spacePicked[1]] = turn


print(printGameBoard())