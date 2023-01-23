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
En esta fase buscaremos informacón sobre el juego(como se juega,modo de juegos,normas...) y en base a esa información podremos crear un pseudocódigo para tener un concepto inicial de la estructura así como las distinstans funciones que compondran el juego.

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
# CODIGO
## División
El codigo se divide en diferentes funciones las cuales trabajan conjuntamente. Estas se ejecutan conforme la opcion seleccionada en el menu principal. También cuenta con variables a las cuales acceden las diferentes funciones.
### Partes:

1.  Variables generales. Estas son basicamente los interruptores de los algoritmos y los elementos que necesitan ser accedidos por diferentes funciones.










DIVISION DEL PROYECTO
TABLERO: Mohammed
MENU: Fabian
CONTRA CPU:Mohammed
1 VS 1: Fabian
Fichas/colocado : Mohammed  
