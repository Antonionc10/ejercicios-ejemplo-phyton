#Para definir una funcion simplemente usamos el comando---> def+nombre de la funcion():
#Con tabulacion indicamos que es lo que va dentro de la funcion

frase=input("Dime una frase:")
   
longitud=len(frase)
print("Su longitud es:",longitud)

mayuscula=frase.upper()
print("Pone la frase en:",mayuscula)

minuscula=frase.lower()
print("Pone la frase en:", minuscula)