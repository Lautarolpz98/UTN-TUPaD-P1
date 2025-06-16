#paqutes
import math



# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundol():
    print('Hola Mundo!')
    
#llamada
imprimir_hola_mundol()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return print(f'Hola {nombre}!')

saludar_usuario('Lautaro')

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre,apellido,edad,residencia):
    return print(f'Soy {nombre},tengo {edad} años y vivo en {residencia}')

informacion_personal("Lautaro",'Lopez',26,"Argentina,Ciudad De Buenos Aires")

# 4. Crear dos funciones: 
#     calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
#     calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
#     Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

radi2 = int(input('Ingrese el radio deseado:'))    
def calcular_area_circulo(radi2):
    return math.pi*radi2**2

area = calcular_area_circulo(radi2)
print(f"El área del círculo es: {area:.2f}")

def calcular_perimetro_circulo(radi2):
    return (radi2*2)*math.pi

perimetro = calcular_perimetro_circulo(radi2)
 
def calcular_area_circulo(radi2):
    return math.pi*radi2**2

area = calcular_area_circulo(radi2)
print(f"El perimetro del círculo es: {perimetro:.2f}")
    
# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def segundos_a_horas(segundos):
      hora = segundos / 3600
      return int(hora)
    
  
segundos = int(input('escribe la cantidad de segundos a comvertir:'))
horas = segundos_a_horas(segundos)
if(horas == 1):
    print(f'tus segudnos equivalen a {horas} hora')
elif(horas > 1):
    print(f'tus segudnos equivalen a {horas} horas')
else:
    print('Tus segundos no llegan a la hora ( recuerda 3600 segundos equivalen a 1 hora)')

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_de_multiplicar(numero):
    for i in range (1,11):
        print((f'{numero} x {i} = {numero*i}'))
        
tabla_de_multiplicar(10)
# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    
    # Devolvemos los resultados en una tupla
    return (suma, resta, multiplicacion, division)

# Pedimos los números al usuario
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

# Llamamos a la función
resultado = operaciones_basicas(a, b)

# Mostramos los resultados de forma clara
print("\n📊 Resultados de las operaciones:")
print(f"➕ Suma: {resultado[0]}")
print(f"➖ Resta: {resultado[1]}")
print(f"✖️ Multiplicación: {resultado[2]}")
print(f"➗ División: {resultado[3]}")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Pedimos datos al usuario
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calculamos el IMC usando la función
resultado_imc = calcular_imc(peso, altura)

# Mostramos el resultado con dos decimales
print(f"Su índice de masa corporal (IMC) es: {resultado_imc:.2f}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
def celsius_a_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

# Pedir la temperatura en Celsius al usuario
temperatura_c = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertir a Fahrenheit usando la función
temperatura_f = celsius_a_fahrenheit(temperatura_c)

# Mostrar el resultado
print(f"{temperatura_c}°C equivalen a {temperatura_f:.2f}°F")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

# Pedir los números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Calcular el promedio usando la función
resultado = calcular_promedio(num1, num2, num3)

# Mostrar el resultado
print(f"El promedio de los números ingresados es: {resultado:.2f}")
