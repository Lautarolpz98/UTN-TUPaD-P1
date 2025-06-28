
# 1) Añadir frutas al diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) Crear una lista con los nombres de frutas
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

# 4) Agenda telefónica
agenda = {}
for _ in range(5):
    nombre = input("Nombre del contacto: ")
    numero = input("Número telefónico: ")
    agenda[nombre] = numero

consulta = input("¿De quién querés saber el número?: ")
if consulta in agenda:
    print(f"Número de {consulta}: {agenda[consulta]}")
else:
    print("Contacto no encontrado.")

# 5) Palabras únicas y frecuencia
frase = input("Escribí una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)

frecuencia = {}
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Frecuencia:", frecuencia)

# 6) Notas de alumnos
alumnos = {}
for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Ingresá nota {i+1} de {nombre}: ")) for i in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio = {promedio:.2f}")

# 7) Estudiantes que aprobaron
parcial1 = {"Ana", "Luis", "Pedro", "Sofía"}
parcial2 = {"Luis", "Sofía", "María"}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# 8) Gestión de stock
stock = {'leche': 10, 'pan': 20}
producto = input("Producto a consultar o agregar: ")
if producto in stock:
    unidades = int(input("¿Cuántas unidades querés agregar?: "))
    stock[producto] += unidades
else:
    nuevo_stock = int(input("Producto nuevo. ¿Cuántas unidades?: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# 9) Agenda de eventos
agenda_eventos = {
    ('Lunes', '10:00'): 'Reunión',
    ('Martes', '15:00'): 'Clase de inglés'
}

dia = input("Ingresá el día: ")
hora = input("Ingresá la hora (HH:MM): ")

evento = agenda_eventos.get((dia, hora), "No hay actividad en ese horario.")
print("Actividad:", evento)

# 10) Invertir diccionario país-capital
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Francia': 'París',
    'Japón': 'Tokio'
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario invertido:", capitales_paises)
