#Para usar un bucle se usa el comando--> for i in range()   donde i es la iteracion
# range() se pone las veces que se tiene que repetir. el rango

#notas a introducir
def calculo_media():
    notas=int(input("Cuantas notas introduce:"))

    for i in range(notas):
        nota=float(input("Introducir notas:"))

        suma=+nota

    nota_media=suma/notas
    print("la nota media es:",nota_media)

calculo_media()


