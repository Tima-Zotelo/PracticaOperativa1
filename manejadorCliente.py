import os
import csv
from claseClienteyReparacion import ClienteyReparacion as cr

class manejadorCliente:
    __listaClientes = []

    def __init__(self) -> None:
        self.__listaClientes = []

    def agregarCliente (self, c):
        self.__listaClientes.append(c)

    def carga (self):
        path = './clientes.csv'
        archivo = open (path, 'r')
        reader = csv.reader (archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                dni = int (fila [0])
                apellido = fila [1]
                nombre = fila [2]
                tel = fila [3]
                pat = fila [4]
                veh = fila [5]
                estado = fila [6]
                xCliente = cr (dni, apellido, nombre, tel, pat, veh, estado)
                self.agregarCliente(xCliente)
        print ('carga clientes lista')
        

    def buscarCliente (self, dni):
        valorRetorno=None
        bandera=False
        indice=0
        while (indice < len(self.__listaClientes) and not bandera):
            if (dni == self.__listaClientes[indice].getDni()):
                valorRetorno = indice
                bandera = True
            else:
                indice+=1
        return valorRetorno  

    def informar (self, dni, mR):
        i = self.buscarCliente (dni)
        print (f'''
DNI: {self.__listaClientes[i].getDni()}     Apellido y Nombre: {self.__listaClientes[i].getNombre() + ' ' + self.__listaClientes[i].getApellido()}
Patente: {self.__listaClientes[i].getPatente()}         Vehiculo: {self.__listaClientes[i].getVehiculo()}
        ''')
        mR.informar (self.__listaClientes[i].getPatente())

    # def buscarClientePat (self, patente):
    #     valorRetorno=None
    #     bandera=False
    #     indice=0
    #     while (indice < len(self.__listaClientes) and not bandera):
    #         if (patente == self.__listaClientes[indice].getPatente()):
    #             valorRetorno = indice
    #             bandera = True
    #         else:
    #             indice+=1
    #     return valorRetorno 

    def cambiarEstado(self, pat):
        for i in range (len (self.__listaClientes)):
            if self.__listaClientes[i].getPatente() == pat:
                self.__listaClientes[i].setEstado('T')
                indice = i
        self.mostrarClienteTerminado(indice)

    def mostrarClienteTerminado (self, i):
        print (f'''
Apellido y Nombre: {self.__listaClientes[i].getNombre() + ' ' + self.__listaClientes[i].getApellido()}
Telefono: {self.__listaClientes[i].getTelefono()}         Vehiculo: {self.__listaClientes[i].getVehiculo()}''')

    def verClientesPendientes(self, mR):
        for i in range (len ((self.__listaClientes))):
            print (f'kauhwdka {self.__listaClientes[i].getEstado()}')
            if self.__listaClientes[i].getEstado() == 'P':
                print (f'''
Apellido y Nombre: {self.__listaClientes[i].getNombre() + ' ' + self.__listaClientes[i].getApellido()} Telefono: {self.__listaClientes[i].getTelefono()}
Patente: {self.__listaClientes[i].getPatente()}        Vehiculo: {self.__listaClientes[i].getVehiculo()}''')
                mR.ReparacionesPendientes(self.__listaClientes[i].getPatente())
    
    def verDoble (self, mR):
        for i in range (len (self.__listaClientes)-1):
            if self.__listaClientes[i] == self.__listaClientes[i+1]:
                print (f'''
DNI: {self.__listaClientes[i].getDni()}     Apellido y Nombre: {self.__listaClientes[i].getNombre() + ' ' + self.__listaClientes[i].getApellido()}
Patente: {self.__listaClientes[i].getPatente()}         Vehiculo: {self.__listaClientes[i].getVehiculo()}
                ''')



