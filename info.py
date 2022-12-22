class Jugador:

    def __init__(self, nombre, edad, movimientos, figura, tamaño,puntos, celdas):

        self.nombre = nombre
        self.edad = edad
        self.movimientos = movimientos
        self.tamaño = tamaño
        self.figura = figura
        self.puntos = puntos
        self.celdas = celdas

class Persona:

    def __init__(self, fila, columna):

        self.fila = fila
        self.columna = columna