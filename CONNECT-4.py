
'''
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



################## TABLERO (matriz: array 2D, 6 filas x 7 columnas) ######################################3
columnaspossible = ["A","B","C","D","E","F","G"]
tablero = [["","","","","","",""], ["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
filas = 6
columnas = 7

################### IMPRIMIR TABLERO ##############################
def imprimir_tablero():
  print("\n     1    2    3    4    5    6    7  ", end="")
  for x in range(filas):
    print("\n   +----+----+----+----+----+----+----+")
    print("   |", end="")
    for y in range(columnas):
      if(tablero[x][y] == "🔵"):
        print("",tablero[x][y], end=" |")
      elif(tablero[x][y] == "🔴"):
        print("", tablero[x][y], end=" |")
      else:
        print(" ", tablero[x][y], end="  |")
  print("\n   +----+----+----+----+----+----+----+")
'''
############ COMPROBAR GANADOR ######################
def ganador(fitcha):
  ######## COMPROBAR ESPACIOS HORIXONTALES ##########
  for y in range(columnas - 3):
    for x in range(filas):
       if tablero[x][y] == fitcha and tablero[x][y+1] == fitcha and tablero[x][y+2] == fitcha and tablero[x][y+3] == fitcha:
        return True

  #### COMPROBAR ESPACIOS VERTICALES ###############
  for y in range(columnas):
    for x in range(filas - 3):
       if tablero[x][y] == fitcha and tablero[x+1][y] == fitcha and tablero[x+2][y] == fitcha and tablero[x+3][y] == fitcha:
        return True

  ##### COMPROBAR DIAGONAL (arriba a la derecha a abajo a la izquierda) #########################################
  for y in range(columnas - 3):
    for x in range(3, filas):
      if tablero[x][y] == fitcha and tablero[x+1][y-1] == fitcha and tablero[x+2][y-2] == fitcha and tablero[x+3][y-3] == fitcha:
        return True

  ######## COMPROBAR DIAGONAL (arriba a la izquierda a abajo a la derecha) ########################################333
  for y in range(columnas - 3):
    for x in range(filas - 3):
      if tablero[x][y] == fitcha and tablero[x+1][y+1] == fitcha and tablero[x+2][y+2] == fitcha and tablero[x+3][y+3] == fitcha:
        return True
  return False
'''
############### COMPROBAR LUGAR VALIDO (si columna correcta) ##########
def hueco(tablero, col):
    return tablero[filas-1][col] == 0

########### HUECO DISPONIBLE (fila disponible en columna seleccionada) ##########
def hueco_disponible(tablero, col):
    for x in range(filas):
        if tablero[x][col] == 0:
            return x

###### INTRODUCIR FITCHA ################
def meter_fitcha(tablero, row, col, fitcha):
    tablero[row][col] = fitcha

def vsIA():
  game_over = False
  turno = 0
  while not game_over:
    if turno == 0:
      col = int(input("Jugador 1 elija columna"))
      if hueco(tablero,col):
        fila = hueco_disponible(tablero,col)
        meter_fitcha(tablero,fila,col,"🔵")
        imprimir_tablero()
    else:
      col = int(input("Jugador 2 elija columna"))
      if hueco(tablero,col):
        fila = hueco_disponible(tablero,col)
        meter_fitcha(tablero,fila,col,"🔴")
        imprimir_tablero()
    turno +=1
    turno = turno%2