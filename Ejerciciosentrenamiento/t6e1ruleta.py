# Para el uso de los condicionales usamos if elif o else ()va la condicion que queremos dar despues mensaje para imprimir 
def color():
    if(color=="rojo"):
        mensaje="Tu dia estará lleno de pasion y energia"
    elif(color=="verde"):
        mensaje ="Tu dia estará lleno de esperanza y crecimiento"
    elif(color=="Azul"):
        mensaje="Tu dia será muy tranquilo y calmado"
    elif(color=="Amarillo"):
        mensaje="Tendras un dia feliz y lleno de optimismo"
    else: 
        color=="Morado"
        mensaje="Tendrás un dia lleno de sabiduría"
    return mensaje
#Con esto el usuario nos dirá un color
color_elegido=input("Elige el color que quieras:")

mensaje= color()

print(mensaje)