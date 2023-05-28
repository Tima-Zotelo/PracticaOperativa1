class ClienteyReparacion:
    __dni: int
    __apellido: str
    __nombre: str
    __telefono: int
    __patente: str
    __vehiculo: str
    __estado: str

    def __init__(self, dni, apellido, nombre, telefono, patente, vehiculo, estado) -> None:
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__telefono = telefono
        self.__patente = patente
        self.__vehiculo = vehiculo
        self.__estado = estado

    def __eq__ (self, otro):
        primero = self.__dni == otro.__dni
        segundo = self.__nombre == otro.__nombre
        tercero = self.__apellido == otro.__apellido
        cuarto = self.__telefono == otro.__telefono
        return primero == segundo == tercero == cuarto

    def getDni(self):
        return self.__dni
    
    def getApellido (self):
        return self.__apellido
    
    def getNombre (self):
        return self.__nombre
    
    def getTelefono (self):
        return self.__telefono
    
    def getPatente (self):
        return self.__patente
    
    def getVehiculo (self):
        return self.__vehiculo
    
    def getEstado (self):
        return self.__estado
    
    def setEstado (self, e):
        self.__estado = e