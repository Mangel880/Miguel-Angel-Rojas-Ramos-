a=int(input("ingrese el numero factorial\n"))
b=1
c=1
while(a>0):
    c=c*b
    b=b+1
    a=a-1
print ("El factorial es: ",c)