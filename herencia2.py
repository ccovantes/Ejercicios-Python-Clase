class persona:
    def __init__(self,edad):
        self.edad = edad

    def hablar(self,mensaje):
        print(self.edad)
        print(mensaje)

class actuario(persona):
    def __init__(self):
        print("hola")


    def contar(self,con):
        print("Yo se ",con)

class derecho(persona):
    def caso(self,con):
        print("Yo se ",con)

pedro = actuario()

print("Yo soy pedro y tengo ")
pedro.contar("contar numeros")
#pedro.hablar("Hola")