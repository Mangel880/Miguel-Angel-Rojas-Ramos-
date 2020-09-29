#Miguel Angel Rojas Ramos
#Calcular la factorial de un numero utilizando la estructura while
a=int(input("ingrese el numero factorial\n"))
b=1
c=1
while(a>0):
    c=c*b
    b=b+1
    a=a-1
print ("El factorial es: ",c)