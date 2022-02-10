class persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def muestraPersona(self):
        print("Nombre :",self.nombre)
        print("Edad :",self.edad)

class alumno(persona):
    def __init__(self,nombre,edad,codigo,calificacion):
        super(alumno,self).__init__(nombre,edad)
        self.codigo = codigo
        self.calificacion = calificacion

    def muestraAlumno(self):
        print("Codigo es :",self.codigo)
        print("La calificacion es :",self.calificacion)

alu = alumno("juan",15,"12345",9.5)
alu.muestraPersona()
alu.muestraAlumno()



#pedro.hablar("Hola")