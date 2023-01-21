######## INTERRUPTORES DEL LAS DIFERENTES OPCIONES ########
game_over2 = True #### interruptor para 1vs1
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
        game_over2 = False
        controlMenu = True
        break
    elif Opcion == 3:
        Historial()
        Menu()
        Opcion =int(input("Que desea hacer ahora: "))
    elif Opcion == 4:
        controlMenu = True
    elif Opcion !=1 or Opcion !=2 or Opcion !=3 or Opcion !=4 :
        Menu()
        Opcion = int(input="Valor incorrecto.Vuelva a introducir un valor: ")
    


################## TABLERO (matriz: array 2D, 6 filas x 7 columnas) ######################################3
columnaspossible = ["A","B","C","D","E","F","G"]
tablero = [["","","","","","",""], ["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
filas = 6
columnas = 7
################### IMPRIMIR TABLERO ##############################
def imprimir_tablero(tablero = tablero):
  print("\n     0    1    2    3    4    5    6  ", end="")
  for x in range(6):
    print("\n   +----+----+----+----+----+----+----+")
    print("   |", end="")
    for y in range(7):
      if(tablero[x][y] == "🔵"):
        print("",tablero[x][y], end=" |")
      elif(tablero[x][y] == "🔴"):
        print("", tablero[x][y], end=" |")
      else:
        print(" ", tablero[x][y], end="  |")
  print("\n   +----+----+----+----+----+----+----+")

############### COMPROBAR LUGAR VALIDO (si columna escojida está disponible correcta) ##########
def hueco(tablero, col):
    if tablero[filas-1][col] == "":
      return True
    else:
      return False

########### HUECO DISPONIBLE (primera fila disponible en columna seleccionada///permite el efecto gravedad) ##########
def hueco_disponible(tablero, col):
    for x in range(filas):
        if tablero[x][col] == "":
            return x

###### INTRODUCIR FITCHA  ################
def meter_fitcha(tablero, fila_disp, col, fitcha):
    tablero[fila_disp][col] = fitcha

############ COMPROBAR GANADOR ######################
def ganador(fitcha):
  ######## COMPROBAR ESPACIOS HORIZONTALES ##########
  for y in range(columnas - 3):
    for x in range(filas):
       if tablero[x][y] == fitcha and tablero[x][y+1] == fitcha and tablero[x][y+2] == fitcha and tablero[x][y+3] == fitcha:
        return True

  #### COMPROBAR ESPACIOS VERTICALES ###############
  for y in range(columnas):
    for x in range(filas - 3):
       if tablero[x][y] == fitcha and tablero[x+1][y] == fitcha and tablero[x+2][y] == fitcha and tablero[x+3][y] == fitcha:
        return True

  ######COMPROBAR DIAGONAL NEGATIVA ########### #######
  for y in range(columnas-3):
    for x in range(3, filas):
      if tablero[x][y] == fitcha and tablero[x-1][y+1] == fitcha and tablero[x-2][y+2] == fitcha and tablero[x-3][y+3] == fitcha:
        return True

  ####### COMPROBAR DIAGONAL POSITIVA ############
    for y in range(columnas-3):
      for x in range(filas-3):
        if tablero[x][y] == fitcha and tablero[x+1][y+1] == fitcha and tablero[x+2][y+2] == fitcha and tablero[x+3][y+3] == fitcha:
          return True


#########  INTERCAMBIO DE TURNOS (inicializar turno en 0)##############
turn = 0
################ BUCLE DE EJECUCION DE LA PARTIDA ###########################3
imprimir_tablero(tablero) ##### IMPRIMIR TABLERO PARA PRIMER VISTAZO
while not game_over2:
  if turn == 0:
    col = int(input("Introduzca la columna que desea jugador 1 : "))
    while hueco(tablero,col) == False:
      col = int(input("Columna llena escoja otra : "))
    if hueco(tablero,col) == True:
      fila_disp = hueco_disponible(tablero,col)
      meter_fitcha(tablero,fila_disp,col,"🔵")
      tablero = tablero[::-1] ####### el tablero se imprime al reves debido al comportamiento de la matriz /// con este metodo se imprime como toca #######
      print(imprimir_tablero(tablero))
      if ganador("🔵") == True:
        print("EL jugador 🔵 es el ganador, FELICIDADES!!!!!")
        game_over2 == True
        break
      tablero = tablero[::-1] ##### devolver el orden de la matriz al original para poder ejecutar las funciones #########
  else:
    col = int(input("Introduzca la columna que desea jugador 2 : "))
    while hueco(tablero,col) == False:
      col = int(input("Columna llena escoja otra : "))
    if hueco(tablero,col) == True:
      fila_disp = hueco_disponible(tablero,col)
      meter_fitcha(tablero,fila_disp,col,"🔴")
      tablero = tablero[::-1]
      print(imprimir_tablero(tablero))
      if ganador("🔴") == True:
        print("EL jugador 🔴 es el ganador, FELICIDADES!!!!!")
        game_over2 == True
        break
      tablero = tablero[::-1]
  turn +=1  ##### Permite intercalar turnos ""
  turn = turn%2 #### permite interclar turnos ""