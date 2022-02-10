class rectangulo:
    def __init__(self,al=0,ba=0):
        self.__altura = al
        
    def getAltura(self):
        return self.__altura

    def setAltura(self,al):
        self.__altura = al

    def getBase(self):
        return self.__base

    def setBase(self,ba):
        self.__base = ba

    def area(self):
        area = self.__base*self.__altura
        return area

x = rectangulo()

x.setAltura(10)
x.setBase(5)
print(x.area())

