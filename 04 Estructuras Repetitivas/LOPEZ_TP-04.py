
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

tu_numero_entero = input("Igresa un numero entero: ")

digitos = 0

for digito in tu_numero_entero:
    digitos += 1
    
print(f"tu numero contiene {digitos} digitos ")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
# Pedimos los dos valores al usuario



# Pedimos los dos números
inicio = int(input("📥 Ingresá el primer número: "))
fin = int(input("📥 Ingresá el segundo número: "))

# Nos aseguramos de que 'inicio' sea menor que 'fin'
if inicio > fin:
    inicio, fin = fin, inicio  # los damos vuelta si están al revés

# Sumamos todos los valores entre ellos (inclusive)
suma_total = 0
for numero in range(inicio  + 1, fin):  # "+1" para incluir el último número
    suma_total += numero

# Mostramos el resultado
print(f"✅ La suma de todos los números entre {inicio} y {fin} es: {suma_total}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
print("🔢 Sumador de números enteros (ingresá 0 para finalizar)\n")

total = 0  # Acumulador que empieza en 0

while True:
    numero = int(input("👉 Ingresá un número entero: "))
    
    if numero == 0:
        break  # Salimos del bucle si es 0
    
    total += numero  # Sumamos el número al total

print(f"\n✅ La suma total acumulada es: {total}")


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random  # Para generar el número aleatorio

# 🎲 El número secreto entre 0 y 9
numero_secreto = random.randint(0, 9)
intentos = 0  # Contador de intentos

print("🎮 Bienvenido al juego de adivinanza entre 0 y 9\n")

while True:
    intento = int(input("🔢 Adiviná el número: "))
    intentos += 1  # Aumentamos el contador
    
    if intento == numero_secreto:
        print(f"🎉 ¡Correcto! El número era {numero_secreto}.")
        print(f"🧠 Lo adivinaste en {intentos} intento(s).")
        break  # ¡Ganó! Fin del juego
    else:
        print("❌ Incorrecto. ¡Probá de nuevo!\n")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente
print("🔢 Números pares del 100 al 0 (en orden decreciente):\n")

# Usamos range con 3 argumentos: inicio, fin, paso
for numero in range(100, -1, -1):  # De 100 a 0, bajando de uno en uno
    if numero % 2 == 0:  # Si el número es par
        print(numero)
        
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
print("🔢 SUMA DE NÚMEROS DESDE 0 HASTA UN NÚMERO INDICADO")

# Pedimos al usuario que ingrese un número
numero = int(input("📥 Ingresá un número entero positivo: "))

# Verificamos que el número sea positivo
if numero < 0:
    print("⚠️ El número debe ser positivo. Intentá de nuevo.")
else:
    suma = 0
    for i in range(numero + 1):  # Desde 0 hasta el número incluido
        suma += i

    print(f"✅ La suma de los números de 0 a {numero} es: {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
print("🔢 ANÁLISIS DE NÚMEROS INGRESADOS")

# Cantidad total de números a ingresar (podés cambiarlo fácilmente para pruebas)
total_numeros = 100  # Cambialo a 5 o 10 para probar más rápido

# Inicializamos contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Bucle para ingresar los números
for i in range(1, total_numeros + 1):
    numero = int(input(f"📥 Ingresá el número {i}: "))

    # Contamos pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Contamos positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

# Mostramos los resultados
print("\n📊 RESULTADOS:")
print(f"🔹 Números pares: {pares}")
print(f"🔸 Números impares: {impares}")
print(f"➕ Números positivos: {positivos}")
print(f"➖ Números negativos: {negativos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
print("📊 CÁLCULO DE MEDIA DE NÚMEROS ENTEROS")

# Total de números que se van a ingresar
total_numeros = 100  # Podés cambiarlo a 5 o 10 para pruebas

# Inicializamos la suma
suma_total = 0

# Bucle para ingresar números
for i in range(1, total_numeros + 1):
    numero = int(input(f"📥 Ingresá el número {i}: "))
    suma_total += numero

# Calculamos la media
media = suma_total / total_numeros

# Mostramos el resultado
print(f"\n📈 La media de los {total_numeros} números ingresados es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

print("🔄 INVERSOR DE NÚMEROS (sin slicing)")

numero = int(input("📥 Ingresá un número entero: "))
numero_original = numero  # Guardamos el número para mostrarlo después

invertido = 0

# Si el número es negativo, lo convertimos en positivo temporalmente
es_negativo = numero < 0
if es_negativo:
    numero = -numero

# Inversión con operaciones matemáticas
while numero != 0:
    ultimo_digito = numero % 10
    invertido = invertido * 10 + ultimo_digito
    numero = numero // 10

# Si era negativo, lo devolvemos a negativo
if es_negativo:
    invertido = -invertido

print(f"🔁 El número {numero_original} invertido es: {invertido}")
