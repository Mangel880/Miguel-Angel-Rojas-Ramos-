#Miguel Angel Rojas Ramos 
#C.I.:12571639
#Utilizando los coeficientes (a,b,c) de una ecuacion de segundo grado se pide mostrar 
# la naturaleza de sus raices
a=int(input("ingrese un numero:\n "))
b=int(input("ingrese un numero:\n "))
c=int(input("ingrese un numero:\n "))
D=(b**2)-4*(a*c)
if (D>0):
    print("El discriminante",D,"son reales y diferentes")
elif (D==0):
    print("El descriminante",D,"son reales e iguales")
elif (D<0):
    print("El discriminante",D,"son complejas")