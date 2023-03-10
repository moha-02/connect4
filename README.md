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
En esta fase buscaremos información sobre el juego(como se juega,modo de juegos,normas...) y en base a esa información podremos crear un pseudocódigo para tener un concepto inicial de la estructura así como las distinstans funciones que compondrán el juego.

### Segunda Fase: Diseño inicial
Fase en la que se absorbe toda la información obtenida de la fase anterior y se plasma en forma de pseudocódigo.El lenguaje que se utilizará para la implementación del juego sera Python,eso quiere decir, que a la hora de elaborar el pseudocódigo debemos acomodarlo al lenguaje que se va utilizar.Teniendo en cuenta eso,se determinará las distintas funciones que tendra nuestra programa inicial.

### Tercera Fase: Codificación y desarollo del juego
En esta etapa se compondrá la codificación del juego.Se hará un fichero maestro donde se plasmará la estructura junto a las funciones relacionadas con el 4 en raya.Con las herramientas que nos ofrece Git,cada miembro del equipo podrá desarrollar las distintas funciones en un archivo que mediante comandos y con la aprobación del otro miembro,se podra fusionar con en el fichero maestro.

### Cuarta Fase: Test de pruebas y errores
En esta última fase ponemos a prueba el juego y verificar las distintas funcionalidades que la componen.También servira para detectar cualquier error que pueda surgir a la hora de ejecutarlo.


# Documentación del Juego

## Documento Definición Del juego

A continuación,explicaremos como se juega al 4 en raya. Como queremos hacer 2 modos, solo desarollaremos uno de ellos, ya que tienen casi las mismas funcionalidades.

**4 EN RAYA (1 VS 1)**
- **Antes de la partida**
~~~
1. Los jugadores han de seleccionar el tipo de ficha que querrán para jugar.
2. Ya con las fichas seleccionadas se le repartiran 21 fichas a cada uno porque el tablero solo tiene 6x7 casillas.
3. Se decide quien de los dos jugadores meterá la 1º ficha al tablero
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
Función que te imprime un Menu,donde se visualizará las distintas opciones a elegir.

Habrá un bucle en el cual hasta que el usuario no elija la opción correcta no sale.

EL ususario tendrá 4 opciones a elegir:

1. Juego contra la CPU
2. Juego 1 VS 1
3. Historial
4. Salida del Juego

Dentro de cada **OPCIÓN**,el usuario encontrará una **FUNCIÓN** que ejecute lo deseado.

#### Opción Juego contra CPU

Se visualizará por pantalla,mediante una **función** , otro menu para que el usuario determine el nivel de dificultad.

Dependiendo de la elección se ejecutará la correspondiente función para que de inicio al juego.

- USUARIO ELIGE MODO FACIL CPU 
~~~
Se imprimirá por pantalla una función que te mostrará el tablero vacio.

Se inicia un bucle,donde se va alternando los turnos hasta que ciertas condiciones se cumplan(Victoria o empate).

Se te pedirá que introduzcas un numero entre el 0 y el 6 para que introduzcas la ficha donde quieras

Una vez introducida, se asegura que el numero esta entre los números establecidos

Despues comprueba si la columna seleccionada hay un hueco disponible para meter la ficha mediante una funcion.

Si hay un hueco introducirá la ficha,sino

pedirá al usuario que elija otra columna.

La introducción de la ficha se hace mediante una función que coge la posición del tablero y lo iguala a la ficha.

Despues de que se introduzca la ficha,se comprueba con una función si el jugador que ha introducido ha ganado

La función que determina si se gana tiene en cuenta si hay 4 fichas seguidas de forma horizontal,vertical o diagonal.

Si ha ganado, te pedirá tu nombre y este se guardará en un diccionario para que quede guardado en el historial

y tras finalizar esa operación,te devuelve al Menu pricipal con el historial.

Si aun no ha ganado,se comprueba si hay un empate

La función empate recorre cada casilla del tablero y si hay alguna casilla vacia devuelve un FALSE

Si hay un empate ,  se visualiza por pantalla que ha habido un empate y te regresa al Menu de inicio

y si no hay un empate,se cambia de turno.

En el turno de la CPU,tiene la misma funcionalidad que el usuario salvo que la elección del numero lo obtiene de forma aleatoria dentro de los rangos establecidos.

Para el random se utiliza su correspondiente librería.

~~~

- USUARIO ELIGE MODO DIFICIL CPU 

~~~~
Tiene las mismas características que el modo fácil ,salvo que que a la hora de introducir la fichas tiene distintas funciones 
para (Ganar o evitar la victoria al usuario)
Si no cumple con niguno de los requisitos que proponen las funciones ,mete la ficha de forma aleatoria.

Todo lo demas funciona de la misma manera que el modo Fácil de la CPU.
~~~~

#### Opción Juego 1 vs 1

~~~
Se imprime mediante una función el tablero donde se va ha disputar la partida.

Inicio de un bucle que durará hasta que haya una victoria o un empate.

Se le pedirá al jugador que inicia un numero entre el 0 y el 6 para que introduzca la ficha donde quiera

Una vez introducida, se asegura que el numero esta entre los numeros establecidos

Despues comprueba si la columna seleccionada hay un hueco disponible para meter la ficha mediante una funcion.

Si hay un hueco introducirá la ficha,sino

pedirá al usuario que elija otra columna.

La introducción de la ficha se hace mediante una función que coge la posición del tablero y lo iguala a la ficha.

Despues de que se introduzca la ficha,se comprueba con una función si el jugador que ha introducido ha ganado

La función que determina si se gana tiene en cuenta si hay 4 fichas seguidas de forma horizontal,vertical o diagonal.

Si ha ganado, te pedirá tu nombre y este se guardará en un diccionario para que quede guardado en el historial

y tras finalizar esa operación,te devuelve al Menu pricipal con el historial.

Si aun no ha ganado,se comprueba si hay un empate

La función empate recorre cada casilla del tablero y si hay alguna casilla vacia devuelve un FALSE

Si hay un empate ,  se visualiza por pantalla que ha habido un empate y te regresa al Menu de inicio

y si no hay un empate,se cambia de turno al otro juugador.

~~~

#### Opción Historial

~~~
Visualiza por pantalla todos los ganadores anteriores.

Esta información se almacena en un diccionario.

Tras visualizarse por pantalla,te devuelve al Menu principal.
~~~

#### Salir del juego

~~~
Finaliza el programa
~~~


# Documento Codificación y Desarollo del Juego

El código se divide en diferentes funciones las cuales trabajan conjuntamente. Estas se ejecutan conforme la opción seleccionada en el menu principal. También cuenta con variables a las cuales acceden las diferentes funciones.
### Partes:

1.  Variables generales. Estas son basicamente los interruptores de los algoritmos y los elementos que necesitan ser accedidos por diferentes funciones.
~~~
import datetime
import random 
import time      #Distintas librerias que se han utilizado

game_over2 = True #### interruptor para 1 vs 1
gameOver = True #### interruptor para 1 vs CPU .Contoladores

####### interruptor + declaracion de historial #######
controlMenu = False
historial = {}    #Diccionario para almacenar los ganadores despues de cada partida

################## TABLERO (matriz: array 2D, 6 filas x 7 columnas) ######################################
tablero = [["","","","","","",""], ["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
filas = 6
columnas = 7  #EL TABLERO EN EL 4 EN RAYA tiene 42 casillas(6 filas y 4 columnas)
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
  print("\n   +----+----+----+----+----+----+----+") #Diseño del tablero

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
    tablero[fila_disp][col] = fitcha           #Coloca la ficha en columna yfila disponible 
~~~

3. Función del juego. Esta permite comprobar el ganador. Mediante esta función se comprueba si existen 4 fichas iguales en linea. Existen 4 casos:
~~~
1. Para los espacios horizontales se recorre la matriz restando 3 columnas, asi queda solo la posiblidad de máximo 4 fichas consecutivas:

    ######## COMPROBAR ESPACIOS HORIZONTALES ##########
  for y in range(columnas - 3):      #Como es un 4 en raya solo necesitas localizar 4 fichas
    for x in range(filas):            #recores las columanas solamente ya que es en la misma fila.
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

4. Para el caso de un empate existe una función que comprueba que el tablero está completo.:
~~~

#################### Funcion parar determinar si hay un empate  ######################
def empate(tablero):
  for i in range(filas):
    for j in range(columnas):
      if tablero[i][j]=="":
        return False     #Recorrres el tablero entero y si hay una casilla que no tiene ficha pues eso significa que aun se sigue jugando.
  return True      
~~~

5.  El modo 1 vs 1 se encuentra en una función que se activa mediante el interruptor del menu:
~~~
def inicio1vs1(tablero,historial):
#########  INTERCAMBIO DE TURNOS (inicializar turno en 0)##############
  turn = 0
################ BUCLE DE EJECUCION DE LA PARTIDA ###########################3
  imprimir_tablero(tablero) ##### IMPRIMIR TABLERO PARA PRIMER VISTAZO

  while not game_over2:
    if turn == 0:
      col = int(input("Introduzca la columna que desea jugador 1 : "))    #Selección de columnas
      while col !=0 and col !=1 and col !=2 and col !=3 and col !=4 and col !=5 and col !=6:   #inicio bucle para que el usuario meta el numero que toca.
        col = int(input("Columna inexistente.Vuelva a introducir una columna jugador 1: "))     #Pedimos al usuario que lo vuelva a introducir
      while hueco(tablero,col) == False:                        #si el hueco no esta disponible
        col = int(input("Columna llena escoja otra : "))        #Elegir otra columna
      if hueco(tablero,col) == True:                             #Si esta libre....
        fila_disp = hueco_disponible(tablero,col)               #Obtener la fila
        meter_fitcha(tablero,fila_disp,col,"🔵")                #meter la ficha en la fila y columna seleccionada
        tablero = tablero[::-1] ####### el tablero se imprime al reves debido al comportamiento de la matriz /// con este metodo se imprime como toca #######
        print(imprimir_tablero(tablero))   #Imprimir trablero
        if ganador("🔵") == True:         #Determinar el ganador,si es el ganador
          print("EL jugador 🔵 es el ganador, FELICIDADES!!!!!")      #Felicitar por pantalla
          game_over2 == True                      #cambio valor para romper el bucle
          vaciarTablero(tablero,filas,columnas)     #Funcion que vacia el tablero
          nombre = input("Introduce tu nombre para que sea registrado: ")   #Registrarse
          fechaActual = datetime.datetime.now()
          fechaFormateada = fechaActual.strftime('%H:%M de %d / %m / %Y')  #Obtener fecha actual formateada
          historial.update({"Ganador": nombre,"fichaUtilizada": "🔵", "Fecha": fechaFormateada })    #añadir información anterior en el diccionario
          return historial      #Devolver diccionario
        elif empate(tablero) == True:   #En caso de que hay un empate,
          print("Ha habido un empate")  #Visualizar por pantalla que ha habido un empate
          game_over2== True
          vaciarTablero(tablero,filas,columnas)  #vaciar tablero
          return historial    #devuelvo el historial
        tablero = tablero[::-1] ##### devolver el orden de la matriz al original para poder ejecutar las funciones #########
    else:      #Mismo procerso que anteriormente
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
    turn = turn%2 #### permite interclar turnos "" #Cambios de turnos

~~~

6.  En el modo vs CPU se distingue entre fácil y díficil, esta opción se puede escoger en el menu principal:

Vamos primero con el modo facil de la CPU en la cual la parte del jugador es la misma que el anterior pero la parte del CPU cambia.
~~~

    else:
      print("CPU pensando..................") #para que actue como si esta pensando
      time.sleep(1)   #tiempo que tardara para ejecutar la siguente instruccion.SE utiliza un import
      eleccionCPU = random.randint(0,6)  #pido que me de un numero aleatorio entre los rangos establecidos
      while hueco(tablero,eleccionCPU)== False:  #Siempre que haya hueco
        eleccionCPU = random.randint(0,6)
      if hueco(tablero,eleccionCPU)== True:
        fila_disponible = hueco_disponible(tablero,eleccionCPU) 
        meter_fitcha(tablero,fila_disponible,eleccionCPU,"🔴") #meto cpu mete la casilla  en la columna random que ha elegido
        tablero = tablero[::-1]     #Mismo que 1 vs1 a partir de aqui salvo que si cpu gana o empata no se registrar la victoria
        imprimir_tablero(tablero)
        if ganador("🔴") == True:
          print("Ha ganado la CPU,:P")
          gameOver == True
          vaciarTablero(tablero,filas,columnas)
          return historial
        elif empate(tablero) == True:
          ("Ha habido un empate ,gracias por jugar. Hasta la próxima !!!")
          game_over2== True
          vaciarTablero(tablero,filas,columnas)
          return historial
        tablero = tablero[::-1] ##### devolver el orden de la matriz al original para poder ejecutar las funciones #########
    turno +=1  ##### Permite intercalar turnos ""
    turno = turno%2 #### permite interclar turnos "" 
~~~

Ahora ,pasemos al modo díficil, esta funcion tiene un par de funciones ,para determinar su victotia.Basicamente va intentar evitar tu victoria.
~~~
    else:
      print("CPU pensando..................")
      time.sleep(1)
      if movimientoGanadorCPU("🔴") == True:  #Funcion que determina si la siguienete jugada se puede ganar
          winCPU("🔴")        #Función mete la ficha enCASILLA  si lo anterior returna un True
          tablero = tablero[::-1] 
          imprimir_tablero(tablero)
          if ganador("🔴") == True:   #Deermino ganador
            print("Ha ganado la CPU,:P")
            gameOver3 == True
            vaciarTablero(tablero,filas,columnas)
            return historial
          tablero = tablero [::-1]
      elif moviminetoGanadorUsuario("🔵") == True:  #Determina si el siguiento movimiento puede ganar el usuario
        evitarDerrotaCPU("🔵","🔴")  #Si lo anterior es True,esta función mete la ficha para impedir la victoria
        tablero = tablero[::-1]
        imprimir_tablero(tablero)
        if ganador("🔴") == True:   #Determinar ganador
            print("Ha ganado la CPU,:P")
            gameOver3 == True
            vaciarTablero(tablero,filas,columnas)
            return historial
        tablero = tablero [::-1]
      else:
        eleccionCPU = random.randint(0,6)              #A partir de aquí es como el codigo del modo Facil.
        while hueco(tablero,eleccionCPU)== False:
          eleccionCPU = random.randint(0,6)
        if hueco(tablero,eleccionCPU)== True:
          fila_disponible = hueco_disponible(tablero,eleccionCPU)
          meter_fitcha(tablero,fila_disponible,eleccionCPU,"🔴")
          tablero = tablero[::-1]
          imprimir_tablero(tablero)
          if ganador("🔴") == True:
            print("Ha ganado la CPU,:P")
            gameOver3 == True
            vaciarTablero(tablero,filas,columnas)
            return historial
        elif empate(tablero) == True:
          print("Ha habido un empate ,gracias por jugar. Hasta la próxima !!!")
          game_over2== True
          vaciarTablero(tablero,filas,columnas)
          return historial
        tablero = tablero[::-1] ##### devolver el orden de la matriz al original para poder ejecutar las funciones #########
    turno +=1  ##### Permite intercalar turnos ""
    turno = turno%2 #### permite interclar turnos ""
~~~

Y a continuación, las funciones que hace que la CPU analice las jugadas:
~~~
###################    Funcion que me determina que proximo movimineto que tiene el usuario para ganar  ################################

def moviminetoGanadorUsuario(ficha):
    ######## COMPROBAR ESPACIOS HORIZONTALES ##########  COMPRUEBA LOS DISTINTOS CASOS CUANDO ESTA DE MANERA HORIZONTAL
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

  #### COMPROBAR ESPACIOS VERTICALES ###############    COMPRUEBA LOS DISTINTOS CASOS CUANDO ESTA DE MANERA VERTICAL
  for y in range(columnas):
    for x in range(filas - 3):
       if tablero[x][y] == ficha and tablero[x+1][y] == ficha and tablero[x+2][y] == ficha and tablero[x+3][y]=="":
        return True

  ######COMPROBAR DIAGONAL NEGATIVA ########### ####### COMPRUEBA LOS DISTINTOS CASOS CUANDO ESTA DIAGONAL INVERSA
  for y in range(columnas-3):
    for x in range(3, filas):
      if (tablero[x][y] == ficha and tablero[x-1][y+1] == ficha and tablero[x-2][y+2] == ficha and tablero[x-3][y+3]=="") and (tablero[x-2][y-3]!=""):
        return True

  ####### COMPROBAR DIAGONAL POSITIVA ############        COMPRUEBA LAS DISNTINTOS CASOS CUANDO ESTA DE MANERA DIAGONAL
    for y in range(columnas-3):
      for x in range(filas-3):
        if (tablero[x][y] == ficha and tablero[x+1][y+1] == ficha and tablero[x+2][y+2] == ficha and tablero[x+3][y+3]=="") and (tablero[x+2][y+3]!=""):
          return True
~~~

~~~
###################    Funcion que me determina que proximo movimineto  que tiene la CPU para ganar  ################################

def movimientoGanadorCPU(ficha):
    ######## COMPROBAR ESPACIOS HORIZONTALES ##########   LO MISMO QUE LO ANTERIOR CUMPLE CON LAS MISMAS
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
~~~

Cada uno de las dos funciones,tiene una otra funcion para colocar la ficha en la casilla seleccionada.Tiene la una codificación similar excepto a la hora de volver un return True  te devuelve la ficha ya colocada en el casillero. 

7. Menu principal. Este interactua sobre todo las funciones del juego. Existen 2 funciones para la estética del menu:
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
El tablero se rellena de arriba a abajo puesto que es una matriz.
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
Crear una función que vacia la matriz recorriendo esta y eliminando las fichas en las posiciones que se encuentran:

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

### Fallo:
~~~
Si introduces un valor que no sea de los demandados en el menu o cuando estas jugando,da un error y se rompe el progrma.
~~~
### Solución
~~~
Crear una función que me arregle el tema de los errores

################## TRATACION DE ERRORES #########################
def treat_error(prompt):
   while True:
    try:
        prompt = int(input("Introduce numero: "))
        return prompt
    except ValueError:
        print("Valor introduzdido incorrecto, vuelve a probar")
~~~

### Fallo:
~~~
Problemas para guardar en el diccionario los ganadores de la partida.
~~~
### Solución
~~~
Declarar el diccionario como variable global , pasarlo por parametro en las distintas funciones y respetando la sintaxis a la hora de hacer los returns
~~~

### Fallo:
~~~
Fallos al hacer la CPU en modo dificil.
~~~
### Solución
~~~
Crear funciones que miminicen las carencias de la CPU a la hora de leer el tablero.
~~~
