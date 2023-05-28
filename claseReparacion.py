class Repacion:
    __patente: str
    __repacion: str
    __precioRepuesto: int
    __precioManoDeObra: int
    __estado: str

    def __init__(self, pat, rep, pRepuestos, pMano, estado) -> None:
        self.__patente = pat
        self.__repacion = rep
        self.__precioRepuesto = pRepuestos
        self.__precioManoDeObra = pMano
        self.__estado = estado

    def getPatente (self):
        return self.__patente
    
    def getReparacion (self):
        return self.__repacion
    
    def getPRepuesto (self):
        return self.__precioRepuesto
    
    def getPManoObra(self):
        return self.__precioManoDeObra
    
    def getEstado (self):
        return self.__estado