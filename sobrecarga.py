
import numpy as np


#a = np.array([1,2,3,4,5])
#b = np.ones((3,2))


#print(a)

ok = [[1,2,3],[4,5,6],[7,8,9]]
ok2 = [10,11,12,13]

n = int(input("Cuantos numeros quieres :"))
arreglo = np.empty(n)

for i in range(arreglo.size):
    val = int(input("Dame el valor "))
    arreglo[i]=val

for i in range(arreglo.size):
    print(arreglo[i],end=" ")
print()

for i in range(4):
    print(ok2[i],end = " ")

for i in range(3):
    for j in range(3):
        print(ok[i][j]," ")
    


#for i in range(a.size):
#    print(i," ",a[i])