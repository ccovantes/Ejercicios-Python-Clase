print("Hola")

try:
    #print(n/0)
    #lista = [1,2]
    #print(lista[9])
    file1 = open("archivooooo.txt","r")
except(FileNotFoundError):
    print("Error con el archivo")
except(IndentationError):
    print("Error")
except(NameError):
    print("Variable no existe")
except(ZeroDivisionError):
    print("División entre cero")
except(IndexError):
    print("Lista fuera del rango")
except(ValueError):
    print("Los valores introducidos no son correctos")
except(Exception):
    print("Error general")
print("Adios")

"""
import numpy as np 

x  = [1,2,3,4,5,6,7,8,9,10]

#num=0
for i in range(10):
    if(x[0]==0):
        raise ErrorTipo1("El primer valor no puede ser cero")
    print(x[i])
#    num = int(input("Dame valor :"))
"""
