from nodo import Nodo
from info import Jugador, Persona

#ElementTree
import xml.etree.ElementTree as ET

class Lista_Doble:

    def __init__(self):

        self.primero = None
        self.ultimo = None
        self.size = 0

    #insetar en lista
    def insertar(self, dato):

        nuevo = Nodo(dato)
        self.size += 1 

        if self.primero == None: 
            self.primero = nuevo
            self.ultimo = nuevo
        else: 
            self.ultimo.siguiente = nuevo 
            nuevo.anterior = self.ultimo 
            self.ultimo = nuevo 
    
    #mostrar datos en consola
    def mostrar(self):

        temp = self.primero 

        while temp != None:

            print(temp.dato) 

            temp = temp.siguiente 
    
    def cargarJugadores(self):
        puntos=0
        actual = self.primero

        #Lista para los jugadores
        listaJugadores = Lista_Doble()

        #atributos de un jugador
        nombreE = ''
        edad = 0
        movimientos = 0
        tamaño = 0
        celdas = Lista_Doble()

        #atributos de jugador
        fila = ''
        columna = ''


        while actual != None:

            tree = ET.parse(actual.dato) 
            root = tree.getroot() #obtengo la etiqueta raíz

            for elemento in root: # elemento es la etiqueta

                if elemento.tag == 'jugador':

                    for subelemento in elemento: # subelemento sera la etiquetas que tienen un nivel menos, en este caso 

                        if subelemento.tag == 'datospersonales': # si es la etiqueta

                            for sub in subelemento: # sub sera las etiquetas <nombre> <edad>

                                if sub.tag == 'nombre': # si es la etiqueta <nombre>

                                    nombreE = sub.text
                                    #print(nombreE)
                                elif sub.tag == 'edad': # si es la etiqueta <edad>

                                    edad = int(sub.text) # la propiedad "text" me devuelve un cadena con int() lo convierto a entero
                                    #print(edad)

                        elif subelemento.tag == 'movimientos': # si es la etiqueta <movimientos>

                            movimientos = int(subelemento.text) # la propiedad "text" me devuelve un cadena con int() lo convierto a entero
                            #print(movimientos)
                            if movimientos<5:
                                puntos+=100
                            elif movimientos>5 and movimientos<10:
                                puntos+=75
                            elif movimientos>10 and movimientos<15:
                                puntos+=50
                            elif movimientos>15 and movimientos<20:
                                puntos+=25
                            
                        
                        elif subelemento.tag == 'tamaño': # si es la etiqueta <tamaño>
                            
                            tamaño = int(subelemento.text) # la propiedad "text" me devuelve un cadena con int() lo convierto a entero
                            #print(tamaño)
                            if tamaño>30:
                                print("Error, el tamanio excede el limite permitido")
                            if tamaño % 5 == 0:
                                print("")
                            else:
                                print("Error, el tamanio ingresado no es multiplo de 5")
                            if tamaño==5:
                                puntos+=25
                            elif tamaño==10:
                                puntos+=50
                            elif tamaño==15:
                                puntos+=75
                            elif tamaño==20:
                                puntos+=100
                            elif tamaño==25:
                                puntos+=125
                            elif tamaño==30:
                                puntos+=150
                        
                        elif subelemento.tag == 'figura': # si es la etiqueta <figura>
                            figura = subelemento.text
                            if figura=='arbol':
                                puntos+=250
                            elif figura=='estrella de Belén':
                                puntos+=500
                            elif figura=='regalo':
                                puntos+=100

                        elif subelemento.tag == 'puzzle': # si es la etiqueta <puzzle>

                            for sub in subelemento: # sub sera la etiqueta <jugador>

                                if sub.tag == 'celda': # si es la etiqueta <jugador>

                                    fila = sub.get('f') 
                                    columna = sub.get('c') 

                                    #print(fila + ' ' +columna)

                                    jugador = Persona(fila, columna) # creo un objeto jugador
                                    celdas.insertar(jugador) # inserto un jugador en la lista celdas 

                #print('-----------------------------------------')
                jugadors = Jugador(nombreE, edad, movimientos,figura, puntos, tamaño, celdas) # creo un objeto jugador
                listaJugadores.insertar(jugadors) # inserto un jugadors en la lista jugadore

                #limpiar la lista celdas
                celdas = Lista_Doble()

            actual = actual.siguiente #pasamos a la siguiente ruta un archivo xml, siempre que hayamos agregado mas.
        return listaJugadores # retornamos la lista de jugadores
        

    def mostrarJugadores(self):

        temp = self.primero 

        while temp != None:

            print('------------------------------------\njugador: {}\nEdad: {}\nmovimientos: {}\ntamaño: {}\nfigura: {}\npuntos: {}\n\npuzzle:\n'.format(temp.dato.nombre, temp.dato.edad, temp.dato.movimientos, temp.dato.tamaño, temp.dato.figura, temp.dato.puntos)) 

            temp.dato.celdas.mostrarRejillas()

            temp = temp.siguiente 
    

    def mostrarRejillas(self):

        temp = self.primero 

        while temp != None:

            print('f: {}\nc: {}\n'.format(temp.dato.fila, temp.dato.columna)) 

            temp = temp.siguiente 

    #por dimension, 25pts por cada 5x5, por cantidad de movimientos = menos de 5 movimientos son 100pts, menos de 10 movimientos son 75pts, menos de 15 movimeintos son 50pts, menos de 20 son 25pts, mas de 20 0 pts, por figura estrella=500, 250 por arbol de navidad y 100 por regalo
   