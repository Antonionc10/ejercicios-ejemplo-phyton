meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

def eleccion(numero):
    
    if (1<= numero <= 12) :
     mes_elegido=meses[numero-1]
     mensaje="Que bonito"
    
    elif mes_elegido=="Diciembre":
       mensaje="El  mejor Mes"
    
    else:
       mensaje="Vete al Peo"
    return mensaje

numero=int(input("Introduce tu numero:"))
prueba=eleccion(numero)
print(prueba)