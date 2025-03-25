# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

'''2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla.'''
nombre = input("Ingrese su nombre: ")
print(f'Hola {nombre}!')

''' 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.
'''
tu_nombre = input("Ingrese su nombre: ")
tu_apellido = input("Ingrese su apellido: ")
tu_edad = input("Ingrese su edad: ")
tu_residencia = input("Ingrese su lugar de residencia: ")
print(f'Soy {tu_nombre} {tu_apellido}, tengo {tu_edad} años y vivo en {tu_residencia}')

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
#Área: Pi multiplicado por el radio al cuadrado.
#Perímetro (circunferencia): Dos veces Pi multiplicado por el radio.
pi = 3.14
tu_radio = float(input("Ingrese el radio de un círculo: "))
area = pi * tu_radio**2
perimetro = 2 * pi * tu_radio
print(f'El área del círculo es: {area} y el perímetro es: {perimetro}')


#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
tus_segundos = int(input("Ingrese una cantidad de segundos: "))
tus_horas = tus_segundos / 3600
print(f"La cantidad de segundos equivalen a {tus_horas} horas")



#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número
dame_un_numero = int(input('Ingrese su numero: '))
print(f'{dame_un_numero} x 1 = {dame_un_numero*1}')
print(f'{dame_un_numero} x 2 = {dame_un_numero*2}')
print(f'{dame_un_numero} x 3 = {dame_un_numero*3}')
print(f'{dame_un_numero} x 4 = {dame_un_numero*4}')
print(f'{dame_un_numero} x 5 = {dame_un_numero*5}')
print(f'{dame_un_numero} x 6 = {dame_un_numero*6}')
print(f'{dame_un_numero} x 7 = {dame_un_numero*7}')
print(f'{dame_un_numero} x 8 = {dame_un_numero*8}')
print(f'{dame_un_numero} x 9 = {dame_un_numero*9}')
print(f'{dame_un_numero} x 10 = {dame_un_numero*10}')
 


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero_uno = int(input('ingrese el primer numero: '))
numero_dos = int(input('ingrese el segundo numero: '))
suma = numero_uno + numero_dos
resta = numero_uno - numero_dos
division = numero_uno / numero_dos
multiplicacion = numero_uno * numero_dos

print(f'los resultados de sumar,restar,dividir,multiplicar tus dos numeros son : suma:{suma},resta:{resta},division:{division},multiplicacion:{multiplicacion}')



'''8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
𝐼𝑀𝐶 =𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
     (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2'''
     
tu_peso =float(input('ingresa tu peso en kg: '))
tu_altura=float(input('ingresa tu altura m:'))
tu_imc_es = tu_peso / (tu_altura **2)
print(f'Tu IMC es: {tu_imc_es}')



'''9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5. 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32'''
celsius = float(input('ingresa tus grados Celsius a convertir: '))
grados_f = float((9/5* celsius) + 32)
print(f'Tus grados Celsius equivalen a {grados_f} grados Fahrenheit')




#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
_1erNumero = int(input('ingresa el primer numero :'))
_2doNumero = int(input('ingrese el segundo numero :'))
_3erNumero = int(input('ingrese el tercer numero: '))
promedio = (_1erNumero + _2doNumero + _3erNumero) / 3
print(f'Tu promedio es de : {promedio}')
 