"""class ErrorTipo1(Exception):
    def __init__(self,valor)


x  = [1,2,3,4,5,6,7,8,9,10]

for i in range(10):
    if(x[0]==0):
        raise ErrorTipo1("El primer valor no puede ser cero")
    print(x[i])"""
class MiError(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return repr(self.valor)

try:
    raise MiError(2*2)
except MiError as e:
    print('Ha ocurrido mi excepción, valor:', e.valor)