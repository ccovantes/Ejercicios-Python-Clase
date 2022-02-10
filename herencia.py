class instrumento:
    def __init__(self,precio):
        self.precio = precio
    
    def tocar(self):
        print("Estamos tocando musica")

    def romper(self):
        print("Si lo rompes lo pagas")
        print("Son",self.precio)

class bateria(instrumento):
    pass

class guitarra(instrumento):
    pass