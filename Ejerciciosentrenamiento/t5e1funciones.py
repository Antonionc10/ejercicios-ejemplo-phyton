#para definir una funcion lo hacemos con el comando---> def + nombre de la funcion():  
# ¡¡¡¡Importante la tabulacion ya que nos indica lo que esta dentro de la funcion!!!!
#Funciones sin parametros

producto = input("Introduce el nombre del producto: ")
precio_unidad = float(input("Introduce el precio por unidad del producto: "))
cantidad = int(input("Introduce la cantidad de productos que deseas comprar: "))
descuento = float(input("Introduce el descuento en porcentaje: "))
iva = float(input("Introduce el IVA en porcentaje: "))

def iva(total,iva):
    iva_aplicado=total*(iva/100)
    return total+iva

def descuento(total,descuento):
    descuento_aplicado=total*(descuento/100)
    return total+descuento_aplicado

def factura(precio_unidad,iva,descuento, cantidad):
    total=precio_unidad*cantidad
    con_iva=total*iva
    con_descuento=total*descuento
    return factura

print(f"\nEl sablazo final es:", factura)




