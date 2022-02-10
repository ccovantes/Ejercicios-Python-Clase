file1 = open("archivo_texto.txt","r")

i=0
cadena = file1.read()

#inicio = int(input("Dame el inicio del archivo")) 
#fin = int(input("Dame el fin del archivo"))
palabra = input("Dame palabra")
aux =0
cad_aux =""
val =0
mayor = ""
for i in cadena:
    if(i!=" " and i!='\n'):
        cad_aux = cad_aux+i
    else:
        #print(cad_aux)
        if(palabra==cad_aux):
            print("Encontrado")    
        if(val==0):
            mayor = cad_aux
            cad_aux =""
            val=1
        else:
            if(len(cad_aux)>len(mayor)):
                mayor = cad_aux
            cad_aux=""

print("La palabra mayor es :",mayor)    

file1.close()
