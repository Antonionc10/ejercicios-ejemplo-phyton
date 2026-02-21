#Para crear una lista simplemente metemos nombre=[,,]

#Lista de planetas
planetas=["Mercurio","Venus","Tierra","Marte","Jupiter","Saturno","Urano","Neptuno"]

#Dado un numero del 1-8 dar el planeta

def eleccion(numero):
    
    if 1 <=numero <=8:
        mensaje=planetas[numero-1]
    else:
        mensaje="Numero incorrecto"
    return mensaje

#Para pedir un numero
numero=int(input("Introduce tu numero:"))

resultado=eleccion(numero)
print(resultado)