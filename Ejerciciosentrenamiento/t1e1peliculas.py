#Para meter variables simplemente nombramos y metemos el valor de la variable

#Peliculas
Título = "El último Samurai"
Año = "2003" #Los enteros se meten con int
Director = "Edward Zwick"
Genero = "Acción/Bélico"
Duración = "2 HORAS 34 minutos"
Premios = True #Los booleanos no tienen que llevar las "" e ir en mayúsculas

#Hay que tener cuidado, cuando lo quieres imprimir poner el nombre y la variable ¡¡NO el valor!!
print( "Título:", Título)
print( "Año:", Año)
print( "Director:", Director)
print( "Genero:", Genero)

#Que pasa si yo quiero meter informacion al usuario.Si es una cadena(string)-->input   si es un numero-->int o float
Título=input("¿Qué título tiene?")
print("titulo",Título)
Año=int(input("¿De que año es?"))
print("Año", Año)

