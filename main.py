from lectura import Lista_Doble
if __name__ == '__main__':

    n = 0
    rutas = Lista_Doble()

    while( n != 2):

        print('Ingrese el nombre de su archivo: \n')

        ruta = input('\t →  ')

        rutas.insertar(ruta)

        print('¿Quiere agregar otro archivo? \n')
        print('1. Si')
        print('2. No\n')

        n = int(input('ingrese la opción deseada: '))

    listaE = rutas.cargarJugadores()

    print()
    listaE.mostrarJugadores()