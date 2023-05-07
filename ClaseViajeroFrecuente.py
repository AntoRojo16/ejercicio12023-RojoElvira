class ViajeroFrecuente:
    __num=0
    __dni=""
    __nombre=""
    __apellido=""
    __millas=0


    def __init__(self,num,dni,nom,ape,millas):
        self.__nombre=nom
        self.__num=num
        self.__dni=dni
        self.__apellido=ape
        self.__millas=millas

    def cantidadYotaldeMillas(self):
        return self.__millas
    

    def acumularMillas(self, millasA):
        self.__millas+=int(millasA)

    def canjearMillas(self,canje):
        if canje<=self.__millas:
            print("Se pueden canjear las millas")
            self.__millas=self.__millas-canje
            return True
        else:
            print("no se pueden canjear las millas")
            return False

    def __str__(self):
        return 'numero: {}, dni: {}, nombre: {}, apellido: {}, millas: {}'.format(self.__num,self.__dni,self.__nombre,self.__apellido,self.__millas)
    

    def getNumero(self):
        return self.__num
    

    def acumulaMillas(self,mi):
        self.__millas+=int(mi)