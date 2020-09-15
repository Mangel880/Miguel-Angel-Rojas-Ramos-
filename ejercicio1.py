#Miguel Angel Rojas Ramos 
#C.I.:12571639
#Ingerese un tiempoX que estara representado en segundos,luego ingrese el tiempo que
# tomara en realizarse una tareaZ representado en horas,minutos y segundos.
# se pide verificar si con el tiempo X se puede finalizar la tarea Z
x=int(input("ingrese un tiempo en segundos:\n"))
print("ingrese el tiempo de trabajo")
h=int(input("Horas:\n"))
m=int(input("Minutos:\n"))
s=int(input("Segundos\n"))
hseg=h*60*60
mseg=m*60/1
z=hseg+mseg+s
sol=x-z
if (sol>=0):
    print("Si se puede cumplir la tarea en el tiempo establecido",sol)
else:
        print("No se puede realizar el trabajo en el tiempo establecido",sol)