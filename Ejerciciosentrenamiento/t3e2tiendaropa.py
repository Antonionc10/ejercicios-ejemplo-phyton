#tema de concatenar cadenas.....usando ciertas funciones cono len(longitud)
#upper(mayusculas) lower(minusculas) 

#Como nos piden varios artiuclos podemos crea una cadena con esos articulos
precio_camiseta=10
precio_sudadera=20.5
precio_gorra=5.5

#Cantidad de articulos que coge el cliente
camiseta=int(input("He cogido:"))
sudadera=int(input("He cogido :"))
gorra=int(input("He cogido :"))

#Total de la compra
subtotal=(camiseta*precio_camiseta + sudadera*precio_sudadera+ gorra*precio_gorra)

#Añadir iva
iva=subtotal*0.21

compra_final= subtotal+ iva


print("Me he gastado en total:", compra_final)