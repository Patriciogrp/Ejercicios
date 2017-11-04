#Resuelto por Patricio González

#Estos ejercicios son didácticos para el aprendizaje respecto al tema de conjuntos

################################ Literal a ################################
print("Literal a")

#Primero pedimos el ingreso de una frase y la almacenamos, y la llevamos a minusculas
frase=input("Ingrese una frase: ").lower()

#Ahora para obtener todas las palabras, haremos un split en función del espacio " "

l_frase=frase.split(" ")    #l_frase tendrá la forma de [palabra1, palabra2, ... etc]

#Como queremos palabra sin repetir simplemente convertimos la lista a conjunto
c_frase=set(l_frase)
#Lo volvemos a llevar a lista para presentarlo por pantalla

print("La palabras sin repetir son: %s"%list(c_frase))



################################ Literal b ################################
print("\nLiteral b")
#Usaremos estas 3 lista para el ejercicio
lista1=["papa","arroz","aceite","ajo"]
lista2=["ajo","zanahoria","aceite","cebolla"]
lista3=["aceite","berenjena","azúcar","ajo"]

#Como queremos los productos en común entre los 3 usuarios, los llevaremos a conjuntos y
#Realizaremos la intersección entre estos para obtener el resultado
c1=set(lista1)
c2=set(lista2)
c3=set(lista3)

resultado=c1&c2&c3

print("Los productos en común son: %s"%resultado)


################################ Literal c ################################
print("\nLiteral b")
#Usaremos estas 2 lista para el ejercicio
Lista_A= ["naruto@konoha.com", "beerus@dbz.gob", "daenarys@got.uk", "pepe@espol.edu.ec"]
Lista_B= ["pepe@espol.edu.ec", "beerus@dbz.gob", "champa@dbs.ec"]

#Como queremos los usarios sin repetir de ambas listas, los convertiremos en conjuntos y los uniremos para obtener el resultado deseado
cA=set(Lista_A)
cB=set(Lista_B)

resultado_c=cA|cB

print("Los correos sin repetir son : %s"%resultado_c)