def converdollar(euro):
    return euro*1.1

def converlibra(euro):
    return euro*0.87

def conversion_total():
    euros=float(input("Introduce cantidad:"))
    dolar=converdollar(euros)
    libra=converlibra(euros)

    print("Cantidad en euros:", euros)
    print("Equivalente en dólares:", dolar)
    print("Equivalente en libras:", libra)

conversion_total()