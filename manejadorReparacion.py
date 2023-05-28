import os
import csv
from claseReparacion import Repacion as rp

class manejadorRepacion:
    __listaReparacion = []

    def __init__(self) -> None:
        self.__listaReparacion = []

    def agregar (self, r):
        self.__listaReparacion.append(r)

    def carga (self):
        path = './reparaciones.csv'
        archivo = open (path, 'r')
        reader = csv.reader (archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                pat = fila [0]
                rep = fila [1]
                pRep = int (fila [2])
                pMano = int (fila [3])
                estado = fila [4]
                xR = rp (pat, rep, pRep, pMano, estado)
                self.agregar(xR)
        print ('carga reparacion lista')

    def total (self, p):
        total = 0
        for i in range (len(self.__listaReparacion)):
            if self.__listaReparacion[i].getPatente() == p:
                subt = self.__listaReparacion[i].getPRepuesto() + self.__listaReparacion[i].getPManoObra()
                total += subt
        return total

    def informar (self, p):
        subt = 0
        print ('{:^10} {:^50} {:^10} {:^15}'.format('Reparacion', 'Precio Repuesto', 'Precio Mano de Obra', 'subtotal'))
        for i in range (len(self.__listaReparacion)):
            if self.__listaReparacion[i].getPatente() == p:
                subt = self.__listaReparacion[i].getPRepuesto() + self.__listaReparacion[i].getPManoObra()
                print ('{:^10} {:^30} {:^30} {:^5}'.format(self.__listaReparacion[i].getReparacion(), self.__listaReparacion[i].getPRepuesto(), self.__listaReparacion[i].getPManoObra(), subt))
                subt = 0
        total = self.total(p)
        print (f'\n Total a pagar: {total}')

    def verEstado(self, pat):
        bandera = True
        for i in range (len(self.__listaReparacion)):
            if self.__listaReparacion[i].getPatente() == pat:
                if self.__listaReparacion[i].getEstado() == 'P':
                    bandera = False
        return bandera

    
    def verReparaciones (self, mC, pat):
        b = self.verEstado (pat)
        if b == False:
            print ('Reparaciones no terminadas')
        else: 
            print ('Todas las reparaciones terminadas')
            mC.cambiarEstado(pat)
            total = self.total(pat)
            print (f'\nTotal a pagar: {total}') 

    def ReparacionesPendientes (self, pat):
        print ('Reparacion:')
        for i in range (len (self.__listaReparacion)):
            if (self.__listaReparacion[i].getPatente() == pat) and (self.__listaReparacion[i].getEstado() == 'P'):
                print (self.__listaReparacion[i].getReparacion())
