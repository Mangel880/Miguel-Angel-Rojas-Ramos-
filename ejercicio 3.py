#Miguel Angel Rojas Ramos 
#C.I.:12571639
#Dado los valores(hora,minuto,segundo)sumarle un segundo
H=int(input("Ingrese  hora:\n"))
M=int(input("Ingrese minutos\n"))
S=int(input("Ingrese segundos\n"))
S=S+1
if (S>=59):
    S=0
    M=M+1
    if (M>=59):
        M=0
        H=H+1
        if (H>=24):
            H=0
        
print(format(H, '02'),":",format(M,'02'),":",format(S,'02'))
