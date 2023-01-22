import datetime
import random 

game_over2 = True #### interruptor para 1vs1
gameOver = True

################### IMPRIMIR TABLERO ##############################
def imprimir_tablero(tablero):
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



###################    Funcion que me determina que proximo movimineto  que tiene la CPU para ganar  ################################

def movimientoGanadorCPU(ficha):
    ######## COMPROBAR ESPACIOS HORIZONTALES ##########
  for y in range(columnas - 3):
    for x in range(filas):
       if (tablero[x][y] == ficha and tablero[x][y+1] == ficha and tablero[x][y+2] == ficha and tablero[x][y+3]=="") and (tablero[x-1][y+3]!=""):
        return True

    for y in range(columnas - 3):
      for x in range(filas):
        if (tablero[x][y+3] == ficha and tablero[x][y+2] == ficha and tablero[x][y+1] == ficha and tablero[x][y]=="") and (tablero[x-1][y] !=""):
          return True

  for y in range(columnas - 3):
    for x in range(filas):
      if (tablero[x][y] == ficha and tablero[x][y+1] == "" and tablero[x][y+2] == ficha and tablero[x][y+3]== ficha) and (tablero[x-1][y+1] !=""):
        return True

  for y in range(columnas - 3):
    for x in range(filas):
      if (tablero[x][y] == ficha and tablero[x][y+1] == ficha and tablero[x][y+2] == "" and tablero[x][y+3]== ficha) and (tablero[x-1][y+2] !=""):
        return True

  #### COMPROBAR ESPACIOS VERTICALES ###############
  for y in range(columnas):
    for x in range(filas - 3):
       if tablero[x][y] == ficha and tablero[x+1][y] == ficha and tablero[x+2][y] == ficha and tablero[x+3][y]=="":
        return True

  ######COMPROBAR DIAGONAL NEGATIVA ########### #######
  for y in range(columnas-3):
    for x in range(3, filas):
      if (tablero[x][y] == ficha and tablero[x-1][y+1] == ficha and tablero[x-2][y+2] == ficha and tablero[x-3][y+3]=="") and (tablero[x+2][y-3]!=""):
        return True

  ####### COMPROBAR DIAGONAL POSITIVA ############
    for y in range(columnas-3):
      for x in range(filas-3):
        if (tablero[x][y] == ficha and tablero[x+1][y+1] == ficha and tablero[x+2][y+2] == ficha and tablero[x+3][y+3]=="") and (tablero[x+2][y+3]!=""):
          return True



#################     Funcion que mete la ficha en el tablero para que la CPU gane ###############################

def winCPU(FICHA):
    ######## COMPROBAR ESPACIOS HORIZONTALES ##########
  for y in range(columnas - 3):
    for x in range(filas):
       if tablero[x][y] == FICHA and tablero[x][y+1] == FICHA and tablero[x][y+2] == FICHA and tablero[x][y+3]=="":
        tablero[x][y+3] = FICHA
        return tablero

    for y in range(columnas - 3):
      for x in range(filas):
        if tablero[x][y+3] == FICHA and tablero[x][y+2] == FICHA and tablero[x][y+1] == FICHA and tablero[x][y]=="":
          tablero[x][y] = FICHA
          return tablero

  for y in range(columnas - 3):
    for x in range(filas):
      if tablero[x][y] == FICHA and tablero[x][y+1] == "" and tablero[x][y+2] == FICHA and tablero[x][y+3]== FICHA:
        tablero[x][y+1] = FICHA
        return tablero

  for y in range(columnas - 3):
    for x in range(filas):
      if tablero[x][y] == FICHA and tablero[x][y+1] == FICHA and tablero[x][y+2] == "" and tablero[x][y+3]== FICHA:
        tablero[x][y+2] = FICHA
        return tablero

  #### COMPROBAR ESPACIOS VERTICALES ###############
  for y in range(columnas):
    for x in range(filas - 3):
       if tablero[x][y] == FICHA and tablero[x+1][y] == FICHA and tablero[x+2][y] == FICHA and tablero[x+3][y]=="":
        tablero[x+3][y] = FICHA
        return tablero

  ######COMPROBAR DIAGONAL NEGATIVA ########### #######
  for y in range(columnas-3):
    for x in range(3, filas):
      if tablero[x][y] == FICHA and tablero[x-1][y+1] == FICHA and tablero[x-2][y+2] == FICHA and tablero[x-3][y+3]=="":
        tablero[x-3][y+3] = FICHA
        return tablero

  ####### COMPROBAR DIAGONAL POSITIVA ############
    for y in range(columnas-3):
      for x in range(filas-3):
        if tablero[x][y] == FICHA and tablero[x+1][y+1] == FICHA and tablero[x+2][y+2] == FICHA and tablero[x+3][y+3]=="":
          tablero[x+3][y+3] = FICHA
          return tablero



###################    Funcion que me determina que proximo movimineto que tiene el usuario para ganar  ################################

def moviminetoGanadorUsuario(ficha):
    ######## COMPROBAR ESPACIOS HORIZONTALES ##########
  for y in range(columnas - 3):
    for x in range(filas):
      if (tablero[x][y] == ficha and tablero[x][y+1] == ficha and tablero[x][y+2] == ficha and tablero[x][y+3]=="") and (tablero[x-1][y+3] !=""):
        return True
  
    for y in range(columnas - 3):
      for x in range(filas):
        if (tablero[x][y+3] == ficha and tablero[x][y+2] == ficha and tablero[x][y+1] == ficha and tablero[x][y]=="") and (tablero[x-1][y] !=""):
          return True

  for y in range(columnas - 3):
    for x in range(filas):
      if (tablero[x][y] == ficha and tablero[x][y+1] == "" and tablero[x][y+2] == ficha and tablero[x][y+3]== ficha) and (tablero[x-1][y+1] !=""):
        return True

  for y in range(columnas - 3):
    for x in range(filas):
      if (tablero[x][y] == ficha and tablero[x][y+1] == ficha and tablero[x][y+2] == "" and tablero[x][y+3]== ficha) and (tablero[x-1][y+2] !=""):
        return True

  #### COMPROBAR ESPACIOS VERTICALES ###############
  for y in range(columnas):
    for x in range(filas - 3):
       if tablero[x][y] == ficha and tablero[x+1][y] == ficha and tablero[x+2][y] == ficha and tablero[x+3][y]=="":
        return True

  ######COMPROBAR DIAGONAL NEGATIVA ########### #######
  for y in range(columnas-3):
    for x in range(3, filas):
      if (tablero[x][y] == ficha and tablero[x-1][y+1] == ficha and tablero[x-2][y+2] == ficha and tablero[x-3][y+3]=="") and (tablero[x-2][y-3]!=""):
        return True

  ####### COMPROBAR DIAGONAL POSITIVA ############
    for y in range(columnas-3):
      for x in range(filas-3):
        if (tablero[x][y] == ficha and tablero[x+1][y+1] == ficha and tablero[x+2][y+2] == ficha and tablero[x+3][y+3]=="") and (tablero[x+2][y+3]!=""):
          return True



#################     Funcion que mete la ficha en el tablero para evitar que el usuario gane ###############################

def evitarDerrotaCPU(ficha,FICHA):
    ######## COMPROBAR ESPACIOS HORIZONTALES ##########
  for y in range(columnas - 3):
    for x in range(filas):
       if tablero[x][y] == ficha and tablero[x][y+1] == ficha and tablero[x][y+2] == ficha and tablero[x][y+3]=="":
        tablero[x][y+3] = FICHA
        return tablero

    for y in range(columnas - 3):
      for x in range(filas):
        if tablero[x][y+3] == ficha and tablero[x][y+2] == ficha and tablero[x][y+1] == ficha and tablero[x][y]=="":
          tablero[x][y] = FICHA
          return True

  for y in range(columnas - 3):
    for x in range(filas):
      if tablero[x][y] == ficha and tablero[x][y+1] == "" and tablero[x][y+2] == ficha and tablero[x][y+3]== ficha:
        tablero[x][y+1] = FICHA
        return tablero

  for y in range(columnas - 3):
    for x in range(filas):
      if tablero[x][y] == ficha and tablero[x][y+1] == ficha and tablero[x][y+2] == "" and tablero[x][y+3]== ficha:
        tablero[x][y+2] = FICHA
        return tablero

  #### COMPROBAR ESPACIOS VERTICALES ###############
  for y in range(columnas):
    for x in range(filas - 3):
       if tablero[x][y] == ficha and tablero[x+1][y] == ficha and tablero[x+2][y] == ficha and tablero[x+3][y]=="":
        tablero[x+3][y] = FICHA
        return tablero

  ######COMPROBAR DIAGONAL NEGATIVA ########### #######
  for y in range(columnas-3):
    for x in range(3, filas):
      if tablero[x][y] == ficha and tablero[x-1][y+1] == ficha and tablero[x-2][y+2] == ficha and tablero[x-3][y+3]=="":
        tablero[x-3][y+3] = FICHA
        return tablero

  ####### COMPROBAR DIAGONAL POSITIVA ############
    for y in range(columnas-3):
      for x in range(filas-3):
        if tablero[x][y] == ficha and tablero[x+1][y+1] == ficha and tablero[x+2][y+2] == ficha and tablero[x+3][y+3]=="":
          tablero[x+3][y+3] = FICHA
          return tablero



#### Funcion para resetear el tablero

def vaciarTablero(tablero,filas,columnas):
  for i in range(filas):
    for j in range(columnas):
      if tablero[i][j] == "🔵":
        tablero[i][j] = ""
      elif tablero[i][j] == "🔴":
        tablero[i][j] = ""
  return tablero

#################### Funcion parar determinar si hay un empate  ######################
def empate(tablero):
  for i in range(filas):
    for j in range(columnas):
      if tablero[i][j]=="":
        return False
  return True      


######################## Modo 1 contra 1 ###################################

def inicio1vs1(tablero,historial):
#########  INTERCAMBIO DE TURNOS (inicializar turno en 0)##############
  turn = 0
################ BUCLE DE EJECUCION DE LA PARTIDA ###########################3
  imprimir_tablero(tablero) ##### IMPRIMIR TABLERO PARA PRIMER VISTAZO

  while not game_over2:
    if turn == 0:
      col = int(input("Introduzca la columna que desea jugador 1 : "))
      while col !=0 and col !=1 and col !=2 and col !=3 and col !=4 and col !=5 and col !=6:
        col = int(input("Columna inexistente.Vuelva a introducir una columna jugador 1: "))
      while hueco(tablero,col) == False:
        col = int(input("Columna llena escoja otra : "))
      if hueco(tablero,col) == True:
        fila_disp = hueco_disponible(tablero,col)
        meter_fitcha(tablero,fila_disp,col,"🔵")
        tablero = tablero[::-1] ####### el tablero se imprime al reves debido al comportamiento de la matriz /// con este metodo se imprime como toca #######
        imprimir_tablero(tablero)
        if ganador("🔵") == True:
          print("EL jugador 🔵 es el ganador, FELICIDADES!!!!!")
          game_over2 == True
          vaciarTablero(tablero,filas,columnas)
          nombre = input("Introduce tu nombre para que sea registrado: ")
          fechaActual = datetime.datetime.now()
          fechaFormateada = fechaActual.strftime('%H:%M de %d / %m / %Y')
          historial.update({"Ganador": nombre,"fichaUtilizada": "🔵", "Fecha": fechaFormateada })
          return historial
        elif empate(tablero) == True:
          print("Ha habido un empate")
          game_over2== True
          vaciarTablero(tablero,filas,columnas)
          return historial
        tablero = tablero[::-1] ##### devolver el orden de la matriz al original para poder ejecutar las funciones #########
    else:
      col = int(input("Introduzca la columna que desea jugador 2 : "))
      while col !=0 and col !=1 and col !=2 and col !=3 and col !=4 and col !=5 and col !=6:
        col = int(input("Columna inexistente.Vuelva a introducir una columna jugador 2: "))
      while hueco(tablero,col) == False:
        col = int(input("Columna llena escoja otra : "))
      if hueco(tablero,col) == True:
        fila_disp = hueco_disponible(tablero,col)
        meter_fitcha(tablero,fila_disp,col,"🔴")
        tablero = tablero[::-1]
        imprimir_tablero(tablero)
        if ganador("🔴") == True:
          print("EL jugador 🔴 es el ganador, FELICIDADES!!!!!")
          game_over2 == True
          vaciarTablero(tablero,filas,columnas)
          nombre = input("Introduce tu nombre para que sea registrado: ")
          fechaActual = datetime.datetime.now()
          fechaFormateada = fechaActual.strftime('%H:%M de %d / %m / %Y')
          historial.update({"Ganador": nombre,"fichaUtilizada": "🔴", "Fecha": fechaFormateada })
          return historial
        elif empate(tablero) == True:
          print("Ha habido un empate")
          game_over2== True
          vaciarTablero(tablero,filas,columnas)
          return historial
        tablero = tablero[::-1]
    turn +=1  ##### Permite intercalar turnos ""
    turn = turn%2 #### permite interclar turnos ""


########################## Modo facil CPU ####################################

def iniciovsCPU(tablero):
  turno = 0 #Controlador de turnos
  imprimir_tablero(tablero)
  while not gameOver:
    if turno == 0:
      col = int(input("Introduzca la columna que desea jugador 1 : "))
      while col !=0 and col !=1 and col !=2 and col !=3 and col !=4 and col !=5 and col !=6:
        col = int(input("Columna inexistente.Vuelva a introducir una columna jugador 1: "))
      while hueco(tablero,col) == False:
        col = int(input("Columna llena escoja otra : "))
      if hueco(tablero,col) == True:
        fila_disp = hueco_disponible(tablero,col)
        meter_fitcha(tablero,fila_disp,col,"🔵")
        tablero = tablero[::-1] ####### el tablero se imprime al reves debido al comportamiento de la matriz /// con este metodo se imprime como toca #######
        imprimir_tablero(tablero)
        if ganador("🔵") == True:
          print("EL jugador 🔵 es el ganador, FELICIDADES!!!!!")
          game_over2 == True
          vaciarTablero(tablero,filas,columnas)
          nombre = input("Introduce tu nombre para que sea registrado: ")
          fechaActual = datetime.datetime.now()
          fechaFormateada = fechaActual.strftime('%H:%M de %d / %m / %Y')
          historial.update({"Ganador": nombre,"fichaUtilizada": "🔵", "Fecha": fechaFormateada })
          return historial
        elif empate(tablero) == True:
          print("Ha habido un empate")
          game_over2== True
          vaciarTablero(tablero,filas,columnas)
          return historial
        tablero = tablero[::-1] ##### devolver el orden de la matriz al original para poder ejecutar las funciones #########
    else:
      print("CPU pensando..................")
      eleccionCPU = random.randint(0,6)
      while hueco(tablero,eleccionCPU)== False:
        eleccionCPU = random.randint(0,6)
      if hueco(tablero,eleccionCPU)== True:
        fila_disponible = hueco_disponible(tablero,eleccionCPU)
        meter_fitcha(tablero,fila_disponible,eleccionCPU,"🔴")
        tablero = tablero[::-1]
        imprimir_tablero(tablero)
        if ganador("🔴") == True:
          print("Ha ganado la CPU,:P")
          gameOver == True
          vaciarTablero(tablero,filas,columnas)
          return historial
        elif empate(tablero) == True:
          print("Ha habido un empate")
          game_over2== True
          vaciarTablero(tablero,filas,columnas)
          return historial
        tablero = tablero[::-1] ##### devolver el orden de la matriz al original para poder ejecutar las funciones #########
    turno +=1  ##### Permite intercalar turnos ""
    turno = turno%2 #### permite interclar turnos ""


########################## Modo dificil CPU #######################################

def inicioVsCPUmodoDificil(tablero):
  turno = 0 #Controlador de turnos
  gameOver3 = False
  imprimir_tablero(tablero)
  while not gameOver3:
    if turno == 0:
      col = int(input("Introduzca la columna que desea jugador 1 : "))
      while col !=0 and col !=1 and col !=2 and col !=3 and col !=4 and col !=5 and col !=6:
        col = int(input("Columna inexistente.Vuelva a introducir una columna jugador 1: "))
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
          vaciarTablero(tablero,filas,columnas)
          nombre = input("Introduce tu nombre para que sea registrado: ")
          fechaActual = datetime.datetime.now()
          fechaFormateada = fechaActual.strftime('%H:%M de %d / %m / %Y')
          historial.update({"Ganador": nombre,"fichaUtilizada": "🔵", "Fecha": fechaFormateada })
          return historial
        elif empate(tablero) == True:
          print("Ha habido un empate")
          game_over2== True
          vaciarTablero(tablero,filas,columnas)
          return historial
        tablero = tablero[::-1] ##### devolver el orden de la matriz al original para poder ejecutar las funciones #########
    else:
      print("CPU pensando..................")
      if movimientoGanadorCPU("🔴") == True:
          winCPU("🔴")
          tablero = tablero[::-1]
          print(imprimir_tablero(tablero))
          if ganador("🔴") == True:
            print("Ha ganado la CPU,:P")
            gameOver3 == True
            vaciarTablero(tablero,filas,columnas)
            return historial
          tablero = tablero [::-1]
      elif moviminetoGanadorUsuario("🔵") == True:
        evitarDerrotaCPU("🔵","🔴")
        tablero = tablero[::-1]
        print(imprimir_tablero(tablero))
        if ganador("🔴") == True:
            print("Ha ganado la CPU,:P")
            gameOver3 == True
            vaciarTablero(tablero,filas,columnas)
            return historial
        tablero = tablero [::-1]
      else:
        eleccionCPU = random.randint(0,6)
        while hueco(tablero,eleccionCPU)== False:
          eleccionCPU = random.randint(0,6)
        if hueco(tablero,eleccionCPU)== True:
          fila_disponible = hueco_disponible(tablero,eleccionCPU)
          meter_fitcha(tablero,fila_disponible,eleccionCPU,"🔴")
          tablero = tablero[::-1]
          print(imprimir_tablero(tablero))
          if ganador("🔴") == True:
            print("Ha ganado la CPU,:P")
            gameOver3 == True
            vaciarTablero(tablero,filas,columnas)
            return historial
        elif empate(tablero) == True:
          print("Ha habido un empate")
          game_over2== True
          vaciarTablero(tablero,filas,columnas)
          return historial
        tablero = tablero[::-1] ##### devolver el orden de la matriz al original para poder ejecutar las funciones #########
    turno +=1  ##### Permite intercalar turnos ""
    turno = turno%2 #### permite interclar turnos ""
      

        


#############################################################
def Historial(historial):
    return print(historial)



########################## MENUS DEL JUEGO (activa los interruptores) #####################################
def Menu():
    print("******************************************")
    print("*              CONNECT-4                 *")
    print("******************************************")
    print("*         1. Jugador vs IA               *")
    print("*         2. Jugador vs Jugador          *")
    print("*         3. Historial de partidas       *")
    print("*         4. Salir del juego             *")
    print("******************************************")

def MenuCPU():
    print("******************************************")
    print("*              CONNECT-4                 *")
    print("******************************************")
    print("*              Dificultad                *")
    print("*             *************              *")
    print("*            1. Modo Facil               *")
    print("*            2. MOdo Dificil             *")
    print("*                                        *")
    print("******************************************")


controlMenu = False
historial = {}
################## TABLERO (matriz: array 2D, 6 filas x 7 columnas) ######################################3
tablero = [["","","","","","",""], ["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
filas = 6
columnas = 7
Menu()
Opcion =int(input("Elige una opción: "))

while controlMenu == False:
    if Opcion == 1:
        MenuCPU()
        modoCPU = int (input("Elige la dificultadad: "))
        while modoCPU !=1 and modoCPU !=2:
          MenuCPU()
          modoCPU = int (input("Error vuelva a introducirlo. 1-MODO FACIL o 2-MODO DIFICIL: "))
        if modoCPU == 1:
          gameOver= False
          iniciovsCPU(tablero)
          Menu()
          Opcion =int(input("Que desea hacer ahora: "))
        else:
          gameOver3 = False
          inicioVsCPUmodoDificil(tablero)
          Menu()
          Opcion =int(input("Que desea hacer ahora: "))
    elif Opcion == 2:
        game_over2 = False
        inicio1vs1(tablero,historial)
        Menu()
        Opcion =int(input("Que desea hacer ahora: "))
    elif Opcion == 3:
        Historial(historial)
        Menu()
        Opcion =int(input("Que desea hacer ahora: "))
    elif Opcion == 4:
        print("Gracias por jugar,vuelva pronto.")
        controlMenu = True
    elif Opcion !=1 or Opcion !=2 or Opcion !=3 or Opcion !=4 :
        Menu()
        Opcion = int(input="Valor incorrecto.Vuelva a introducir un valor: ")
   