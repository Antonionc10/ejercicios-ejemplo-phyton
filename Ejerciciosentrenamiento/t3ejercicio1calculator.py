#Hay que realizar una Calculadora

#Para ello necesitamos un programa que primero nos pida dos números, y despúes le metamos las operaciones necesarias
#Para ello necesitamos usar los input en las variables y el tipo de número tanto float como int

#Hacer que el programa me pida un número
numero1=float(input("Dame el primer numero:"))
numero2=float(input("Dame el segundo numero:"))

#Operaciones
suma=numero1 + numero2
resta=numero1-numero2
producto=numero1*numero2
división=numero1/numero2  #habría que meter con un condicional la condicion de que si numero2=0 esto da error o es infinito(en su límite)

print("Suma",suma)
print("Resta", resta)
print("Producto", producto)
print("division",división)

if numero2 == 0: print("No se puede hacer división")
else: print("division",división)