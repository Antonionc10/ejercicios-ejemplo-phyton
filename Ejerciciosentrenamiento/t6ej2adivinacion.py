# un programa donde el usuario me pida el numero. Si dice el 4 gana si no pierde
#Para poner que es distinto es (!=)
def adivinanza(numero):
    if(numero == 4):
        mensaje="Bien hecho campeón"
    else:
        numero!=4
        mensaje="Eres un perdedor"
    return mensaje

#El usuario elige el numero
numero_elegido=float(input("Elige un numero del 1 a 10:"))

mensaje=adivinanza(numero_elegido)
print(mensaje)
