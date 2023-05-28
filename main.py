import os
from manejadorCliente import manejadorCliente
from manejadorReparacion import manejadorRepacion
from Menu import Menu

if __name__ == '__main__':
    mC = manejadorCliente()
    mR = manejadorRepacion()
    menu = Menu ()
    mC.carga()
    mR.carga()
    bandera = False
    os.system('cls')
    while not bandera:
        menu.mostrarMenu()
        opcion = int (input("Su opcion: "))
        menu.opcion(opcion, mC, mR)
        if opcion == 0:
            bandera = True
        os.system('pause')
        os.system('cls')
    os.system('exit')


## 18207111
## AB000BA