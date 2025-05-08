#  1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
multiplos_de_4 = list (range(4,101,4))
print(multiplos_de_4)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!
print("------------------------------------------------------------------------------------------------------")
gustos = ['pizza','video juegos','boxeo','peliculas','idiomas']
print(gustos[-2])
print("------------------------------------------------------------------------------------------------------")

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
lista_vacia = []
lista_vacia.append('El Eternauta')
lista_vacia.append(2025)
lista_vacia.append('Que Buena Serie')
print(lista_vacia)
print("------------------------------------------------------------------------------------------------------")

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
animales[-2] = "oso"
animales[1] = "loro"
print(animales)
print("------------------------------------------------------------------------------------------------------")


# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# numeros = [8,15,3,22,7]
# numeros.remove(max(numeros))
# print(numeros)
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(f"""LO QUE HACE ES CREAR UNA LISTA DESORDENADA DE NUMEROS
LUEGO SE REMUEVE EL NUMERO MAS GRANDE DE LA LISTA UTILIZANDO "MAX()"
Y SE IMPRIME POR PANTALLA:
    {numeros}""")
print("------------------------------------------------------------------------------------------------------")


# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.
print('LISTA 10 A 30 DE 5 EN 5')
uno_al_treinta = list(range(10,30 + 1,5))
print(uno_al_treinta)
print("PRIMEROS 2 DE LA LISTA")
traer_De_lista = uno_al_treinta[0:2]
print(traer_De_lista)
print("------------------------------------------------------------------------------------------------------")
# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
print((f'Original \n{autos}'))
autos[1] = "mazda"
autos[2] = "ferrari"
print((f'Modificada \n{autos}'))
print("------------------------------------------------------------------------------------------------------")
# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
# ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")            
compras[1][1] = "tallarines"         
compras[0].remove("pan")             
print(compras)             
print("------------------------------------------------------------------------------------------------------")
# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False

Posición_lista_anidada_0_= [15]
Posición_lista_anidada_1_=[True]
Posición_lista_anidada_2_0_=[25.5]
Posición_lista_anidada_2_1_=[57.9]
Posición_lista_anidada_2_2_=[30.6]
Posición_lista_anidada_3_=[False]


sublista_anidada = Posición_lista_anidada_2_0_ + Posición_lista_anidada_2_1_+Posición_lista_anidada_2_2_
# Imprimir la lista resultante por pantalla.
Lista_anidad = Posición_lista_anidada_0_ + Posición_lista_anidada_1_ + [sublista_anidada] +Posición_lista_anidada_3_
print(Lista_anidad)
print("------------------------------------------------------------------------------------------------------")



