# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario
numero_por_usuario = int(input(f'De que numero quieres el factorial?:'))

def f_recursiva(num):
    if num == 0:
        return 1
    else:
        return f_recursiva(num - 1)* num
    
    
for i in range(1,numero_por_usuario + 1):
    print(f'El factorial de {i} es {f_recursiva(i)}')    
    
# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.
# Función recursiva para calcular el número de Fibonacci en la posición n
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Pedir al usuario la cantidad de términos
posicion = int(input("¿Hasta qué posición de la serie de Fibonacci querés ver?: "))

# Mostrar la serie completa desde 0 hasta la posición indicada
for i in range(posicion + 1):
    print(f'F({i}) = {fibonacci(i)}')

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛
# 𝑚 = 𝑛 ∗ 𝑛
# (𝑚−1)
# . Prueba esta función en un
# algoritmo general.
# Función recursiva para calcular la potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Solicitar base y exponente al usuario
base = int(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente: "))

# Mostrar el resultado
print(f"{base} elevado a la {exponente} es igual a {potencia(base, exponente)}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
# unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
# procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
# TECNICATURA UNIVERSITARIA
# EN PROGRAMACIÓN
# A DISTANCIA
# 2
# Programación I
# 🧠Ejemplo:
# Convertir el número 10 a binario:
# 10 ÷ 2 = 5 resto: 0
# 5 ÷ 2 = 2 resto: 1
# 2 ÷ 2 = 1 resto: 0
# 1 ÷ 2 = 0 resto: 1
# Función recursiva para convertir decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Pedir número al usuario
numero = int(input("Ingresá un número entero positivo en base decimal: "))

# Validar entrada y mostrar resultado
if numero == 0:
    print("El número binario es: 0")
else:
    binario = decimal_a_binario(numero)
    print(f"El número binario es: {binario}")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().
def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 letra, es palíndromo
    if len(palabra) <= 1:
        return True
    # Comparamos primera y última letra
    if palabra[0] == palabra[-1]:
        # Llamada recursiva sin la primera y última letra
        return es_palindromo(palabra[1:-1])
    else:
        return False

# Prueba de la función
palabra = input("Ingresá una palabra (sin espacios ni tildes): ").lower()

if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Prueba
numero = int(input("Ingresá un número entero positivo: "))
print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
#  Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Prueba
niveles = int(input("¿Cuántos bloques tiene el nivel más bajo de la pirámide?: "))
print(f"Se necesitan {contar_bloques(niveles)} bloques en total para construir la pirámide.")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0 

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

# Pruebas
print(contar_digito(12233421, 2))  # → 3
print(contar_digito(5555, 5))      # → 4
print(contar_digito(123456, 7))    # → 0
