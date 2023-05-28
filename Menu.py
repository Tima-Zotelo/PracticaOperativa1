import os

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1: self.opc1,
                            2: self.opc2,
                            3: self.opc3,
                            4: self.opc4,
                            0: self.salir
                        }

    def opcion(self,op, mC, mR):
        func=self.__switcher.get(op, lambda: print("Opción no válida, intente de nuevo"))
        if op == 1 or op == 2 or op == 3 or op == 4:
            func( mC, mR)
        else:
            func()

    def mostrarMenu(self):
        print("""
---------->Menu Principal<----------

-> 1: Informar los datos del cliente
-> 2: determinar si todas las reparaciones están terminadas por patente
-> 3: Ver Clientes Pendientes
-> 4: Determinar el o los clientes que le hacen servicio a más de un vehículo
-> 0: Salir del programa
""")

## OPCIONES

    def opc1 (self,  mC, mR):
        os.system('cls')
        dni = int (input ('ingrese DNI del cliente: '))
        mC.informar(dni, mR)

    def opc2 (self,  mC, mR):
        os.system('cls')
        pat = input ('Ingrese patente a buscar: ')
        mR.verReparaciones (mC, pat)

    def opc3 (self,  mC, mR):
        os.system('cls')
        mC.verClientesPendientes(mR)
    
    def opc4 (self,  mC, mR):
        mC.verDoble(mR)

    def salir (self):
        print ('saliendo...')