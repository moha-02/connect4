# CONNECT-4
Primer proyecto en Python del  modulo DAW. Autores : Mohammed y Fabian

## Objetivos
Lo primordial en este proyecto en conjunto es aplicar todos los conocimientos adquiridos,durante este tiempo,sobre el lenguaje de programación Python  y poder así realizar varias funciones con el objetivo de crear un juego.

El juego que hemos elegido es el clasico  *** 4 en raya *** ,donde el usuario tendra 2 modos de juego:
- Contra la IA
- Contra otro jugador

## Estructura Del Proyecto
La estrctura del proyecto se compone de 4 fases: Definición del juego,diseño inicial,desarollo y codificación del juego y test de pruebas y errores.

### Primera Fase: Definición del juego
En esta fase buscaremos información sobre el juego(como se juega,modo de juegos,normas...) y en base a esa información podremos crear un pseudocódigo para tener un concepto inicial de la estructura así como las distinstans funciones que compondran el juego.

### Segunda Fase: Diseño inicial
Fase en la que se absorbe toda la información obtenida de la fase anterior y se plasma en forma de pseudocódigo.El lenguaje que se utilizará para la implementación del juego sera Python,eso quiere decir, que a la hora de elaborar el pseudocódigo debemos acomodarlo al lenguaje que se va utilizar.Teniendo en cuenta eso,se determinará las distintas funciones qque tendra nuestra programa inicial.

### Tercera Fase: Codificación y desarollo del juego
En esta etapa se compondrá la codificación del juego.Se hará un fichero maestro donde se plasmará la estructura junto a las funciones relacionadas con el 4 en raya.Con las herramientas que nos ofrece Git,cada miembro del equipo podra desarrollar las distintas funciones en un archivo que mediante comandos y con la aprobación del otro miembro,se podra fusionar con en el fichero maestro.

### Cuarta Fase: Test de pruebas y errores
En esta ultima fase ponemos a prueba el juego y verificar las distintas funcionalidades que la componen.También servira para detectar cualquier error que pueda surgir a la hora de ejecutarlo.


# Documentación del Juego

## Documento Definición Del juego

A continuación,explicaremos como se juega al 4 en raya. Como queremos hacer 2 modos, solo desarollaremos un0 de ellos, ya que tienen casi las mismas funcionalidades.

**4 EN RAYA (1 VS 1)**
- **Antes de la partida**
~~~
1. Los jugadores han de seleccionar el tipo de ficha que querrán para jugar.
2. Ya con las fichas seleccionadas se le repartiran 21 fichas a cada uno porque el tablero solo tiene 6x7 casillas.
3. Se decide quien de los dos jugaadores metera la 1º ficha al tablero
~~~
***Inicio partida***

- **Partida**
~~~
1.En cada turno los jugadores colocarán una ficha de su color en una columna y esta cae hasta la primera casilla disponible
~~~
- **Finalización de Partida**

Hay 2 formas de finalizar el juego:
~~~
1. El primer jugador en ubicar 4 fichas del mismo color seguidas en horizontal,vertical o diagonal positiva/negativa.
2. Si el tablero termina con todas las casillas ocupadas y no hay 4 fichas del mismo color seguidas,la partida termina en empate.
~~~

# Documento Diseño Inicial
## Inicio
Funcion que te imprima un Menu,donde se visualizara las distintas opciones a elegir.

Habra un bucle en el cual hasta que el usuario no elija la opción correcta no sale.

EL ususario tendra 4 opciones a elegir:
- Juego contra la CPU
- jUEGO






# Documento Codificación y Desarollo del Juego
## División
El codigo se divide en diferentes funciones las cuales trabajan conjuntamente. Estas se ejecutan conforme la opcion seleccionada en el menu principal. También cuenta con variables a las cuales acceden las diferentes funciones.
### Partes:

1.  Variables generales. Estas son basicamente los interruptores de los algoritmos y los elementos que necesitan ser accedidos por diferentes funciones.
~~~
import datetime
import random 

game_over2 = True #### interruptor para 1 vs 1
gameOver = True #### interruptor para 1 vs CPU

####### interruptor + declaracion de historial #######
controlMenu = False
historial = {}
################## TABLERO (matriz: array 2D, 6 filas x 7 columnas) ######################################
tablero = [["","","","","","",""], ["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
filas = 6
columnas = 7
~~~

2. Funciones del tablero. Estas permiten imprimir el tablero y conocer su estado para poder operar sobre este (huecos disponibles, lugares validos, introducir una ficha)
~~~
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
~~~

3. Funcion del juego. Esta permite comprobar el ganador. Mediante esta funcion se comprueba si existen 4 fitchas iguales en linea. Existen 4 casos:
~~~
1. Para los espacios horizontales se recorre la matriz restando 3 columnas, asi queda solo la posiblidad de máximo 4 fichas consecutivas:

    ######## COMPROBAR ESPACIOS HORIZONTALES ##########
  for y in range(columnas - 3):
    for x in range(filas):
       if (tablero[x][y] == ficha and tablero[x][y+1] == ficha and tablero[x][y+2] == ficha and tablero[x][y+3]=="") and (tablero[x-1][y+3]!=""):
        return True

2. Para los espacios verticales aplicamos la misma funcion que para los espacios horizontales, pero en este caso teniendo en cuenta que seran -3 filas:

  for y in range(columnas):
    for x in range(filas - 3):
       if tablero[x][y] == fitcha and tablero[x+1][y] == fitcha and tablero[x+2][y] == fitcha and tablero[x+3][y] == fitcha:
        return True
        
3. Para comprobar la diagonal negativa se intercalan las filas y columnas:

  for y in range(columnas-3):
    for x in range(3, filas):
      if tablero[x][y] == fitcha and tablero[x-1][y+1] == fitcha and tablero[x-2][y+2] == fitcha and tablero[x-3][y+3] == fitcha:
        return True
        
4. Para comprobar la diagonal positiva se aumentan las filas y columnas en el mismo orden:

    for y in range(columnas-3):
      for x in range(filas-3):
        if tablero[x][y] == fitcha and tablero[x+1][y+1] == fitcha and tablero[x+2][y+2] == fitcha and tablero[x+3][y+3] == fitcha:
          return True
~~~

4. Para el caso de un empate existe una funcion que comprueba que el tablero está completo.:
~~~

#################### Funcion parar determinar si hay un empate  ######################
def empate(tablero):
  for i in range(filas):
    for j in range(columnas):
      if tablero[i][j]=="":
        return False
  return True      
~~~

5.  El modo 1 vs 1 se encuentra en una funcion que se activa mediante el interruptor del menu:
~~~
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
      col = int(input("Introduzca la columna que desea jugador 2 : "))
      while col !=0 and col !=1 and col !=2 and col !=3 and col !=4 and col !=5 and col !=6:
        col = int(input("Columna inexistente.Vuelva a introducir una columna jugador 2: "))
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

~~~

6.  En el modo vs CPU se distingue entre facil y dificil, esta opcion se puede escojer en el menu principal:
~~~

****** ESTO ES TUYO FABIAN *******
~~~

7. Menu principal. Este interactua sobre todo las funciones del juego. Existen 2 funciones para la estetica del menu:
~~~

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
############### IMPRIMIR EL MENU ESTETICO DE LA FUNCION ##########
Menu()
Opcion =int(input("Elige una opción: "))

############# MECANICA DEL MENU #########
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
   
~~~

# Documento Test de Pruebas y Errores
### Fallo:
~~~
El tablero se rrelena de arrib a bajo puesto que es una matriz.
~~~
### Solución:
~~~
Invertir la matriz a la hora de imprimir, posteriormente revertirlo al estado original:

tablero = tablero[::-1] ####### el tablero se imprime al reves debido al comportamiento de la matriz /// con este       metodo se imprime como toca #######
tablero = tablero[::-1] ##### devolver el orden de la matriz al original para poder ejecutar las funciones #########
~~~

### Fallo:
~~~
El tablero no borra la partida anterior para poder jugar la siguiente partida
~~~
### Solución:
~~~
Crear una funcion que vacia la matriz recorriendo esta y eliminando las fichas en las posiciones que se encuentran:

#### Funcion para resetear el tablero

def vaciarTablero(tablero,filas,columnas):
  for i in range(filas):
    for j in range(columnas):
      if tablero[i][j] == "🔵":
        tablero[i][j] = ""
      elif tablero[i][j] == "🔴":
        tablero[i][j] = ""
  return tablero
~~~
