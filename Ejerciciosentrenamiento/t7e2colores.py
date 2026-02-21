
color_premio="azul"
ganado=False

for i in range(5):
    colores=input("Introduce 5 colores:")
    if colores == color_premio:
        ganado = True

    
    
if colores==color_premio:
    print("Has ganado")
else:
    print("has perdido")
    