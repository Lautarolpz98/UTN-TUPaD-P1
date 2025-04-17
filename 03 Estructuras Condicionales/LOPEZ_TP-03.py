import random
import statistics




# Actividades
# 1) Escribir un programa que solicite la edad del usuario.
# Si el usuario es mayor de 18 años,deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.


edad = int(input('Ingrese su edad : '))
if edad >= 18 :
        print("Es mayor de edad")
else:
    print("No es mayor de edad")
    
    
    
# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6,
# debera mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

nota = int(input('Dime tu nota: '))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")



# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

userNumber = int(input("Ingrese un numero par: "))
if userNumber % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
    
    
# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

age = int(input("Ingrese su edad: "))
if age < 12:
    print("Niño/a")
elif age >= 12 and age <= 18:
    print("Adolescente")
elif age >= 18 and age < 30:
    print("Adulto/a Joven")
elif age >= 30:
    print("Adulto/a")
        


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.
password = input('Escribe tu password: ')
if len(password) >= 8 and len(password) <=14:
    print("Ha ingresado un password correcto")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    
   
# 6)Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(numeros_aleatorios)

#moda
moda = statistics.mode(numeros_aleatorios)
#mediana
mediana = statistics.median(numeros_aleatorios)
#media
media = statistics.mean(numeros_aleatorios)



#tipo de sesgo
if media > mediana > moda:
    print("El sesgo es Positivo  o a la derecha")
elif media < mediana < moda:
    print("El sesgo es Negativo o a la izquierda") 
elif media == mediana == moda:
    print("El sesgo es Sin sesgo")     



print(f"La mediana es: {mediana}")
print(f"La moda es: {moda}")
print(f"La media es: {media}")



# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

frase = input("Escribe una frase: ")
ultimaLetra = frase[-1]

if ultimaLetra == "a":
    print(frase + '!')

elif ultimaLetra == "e":
    print(frase + '!')

elif ultimaLetra == "i":
    print(frase + '!')

elif ultimaLetra == "o":
    print(frase + '!')

elif ultimaLetra == "u":
    print(frase + '!')
else:
    print(frase)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.


IngreseNombre = input("Ingresa tu nombre: ")

opciones = int(input("""Selecciones una de las opciones:\n
                     1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n
                     2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n
                     3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.\n
                    Ingrese su opcion: 
                     """))
if opciones == 1:
    print(IngreseNombre.upper())
elif opciones == 2:
    print(IngreseNombre.lower())
elif opciones == 3:
    print(IngreseNombre.title())
else:
    print("No seleccionaste ninguna de las opciones")
    
# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = int(input("Escribe la magnitud del terremoto: "))
if magnitud < 3 :
    print("Muy leve (imperceptible)")
elif magnitud >= 3  and magnitud < 4 :
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)") 
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles")
elif magnitud >= 6 and magnitud < 7:    
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print( "Extremo (puede causar graves daños a gran escala)")
else:
    print("DEVASTADOR 😱😱")
          
          
          
#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año        

# | 📅 Periodo del año                                   | 🌍 Hemisferio Norte | 🌎 Hemisferio Sur |
# |------------------------------------------------------|---------------------|-------------------|
# | Desde el 21 de diciembre hasta el 20 de marzo       | Invierno            | Verano            |
# | Desde el 21 de marzo hasta el 20 de junio           | Primavera           | Otoño             |
# | Desde el 21 de junio hasta el 20 de septiembre      | Verano              | Invierno          |
# | Desde el 21 de septiembre hasta el 20 de diciembre  | Otoño               | Primavera         |


# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

print("🧭 Estación del año según fecha y hemisferio")

hemisferio = input("¿En qué hemisferio estás? (N/S): ")
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))


if hemisferio == "N" or hemisferio == "n":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
elif hemisferio == "S" or hemisferio == "s":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

# Mostramos el resultado
print("Estación del año:", estacion)


