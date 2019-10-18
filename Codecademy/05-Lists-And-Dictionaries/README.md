# Listas y Diccionarios
* 8.1 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

zoo_animals = [ "Halcón", "Búho", "Urraca", ];
# One animal is missing!

if len(zoo_animals) > 3:
	print "El primer animal en el zoológico es el " + zoo_animals[0]
	print "El segundo animal en el zoológico es el " + zoo_animals[1]
	print "El tercer animal en el zoológico es el " + zoo_animals[2]
	print "El cuarto animal del zoo es el " + zoo_animals[3]
```

* 8.1 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

zoo_animals = [ "Halcón", "Búho", "Urraca", "Tucán"];
# One animal is missing!

if len(zoo_animals) > 3:
	print "El primer animal en el zoológico es el " + zoo_animals[0]
	print "El segundo animal en el zoológico es el " + zoo_animals[1]
	print "El tercer animal en el zoológico es el " + zoo_animals[2]
	print "El cuarto animal del zoo es el " + zoo_animals[3]
```

* 8.2 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

numbers = [5, 6, 7, 8]

print "Sumando los números en los índices 0 y 2..."
print numbers[0] + numbers[2]
print "Sumando los números en los índices 1 y 3...."
#¡Tu código aquí!
```

* 8.2 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

numbers = [5, 6, 7, 8]

print "Sumando los números en los índices 0 y 2..."
print numbers[0] + numbers[2]
print "Sumando los números en los índices 1 y 3...."
# tu código aquí
print numbers[1] + numbers[3]
```

* 8.3 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

zoo_animals = ["Cabra", "Jirafa", "perezoso", "tigre"]
# Anoche el perezoso de nuestro zoológico atacó brutalmente brutalmente
# el pobre tigre y se lo comió entero.

# El feroz perezoso ha sido reemplazado por una hiena amistosa.
zoo_animals[2] = "hiena"

# Qué llenará el vacío dejado por nuestro querido tigre difunto?
#¡Tu código aquí!
```

* 8.3 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

zoo_animals = ["Cabra", "Jirafa", "perezoso", "tigre"]
# Anoche el perezoso de nuestro zoológico atacó brutalmente brutalmente
# el pobre tigre y se lo comió entero.

# El feroz perezoso ha sido reemplazado por una hiena amistosa.
zoo_animals[2] = "hiena"

# Qué llenará el vacío dejado por nuestro querido tigre difunto?
#¡Tu código aquí!
zoo_animals[3] = "camello"
```

* 8.4 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

suitcase = [] 
suitcase.append("gafas de sol")

#¡Tu código aquí!




list_length = ________ # Establezca esto en la longitud de la maleta

print "Hay %d elementos en la maleta" % (list_length)
print suitcase
```

* 8.4 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

suitcase = []
suitcase.append("gafas de sol")

#¡Tu código aquí!
suitcase.append("toalla")
suitcase.append("zapatos")
suitcase.append("tapa")


list_length = len(suitcase) # Establezca esto en la longitud de la maleta

print "Hay %d elementos en la maleta" % (list_length)
print suitcase
```

* 8.5 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

suitcase = ["gafas de sol", "sombrero", "pasaporte", "portátil", "traje", "zapatos"]

# El primer y segundo elemento (índice cero y uno)
first = suitcase[0:2]

# Tercer y cuarto elementos (índice dos y tres)
middle = 

# Los dos últimos elementos (índice cuatro y cinco)
last =  
```

* 8.5 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

suitcase = ["gafas de sol", "sombrero", "pasaporte", "portátil", "traje", "zapatos"]

# El primer y segundo elemento (índice cero y uno)
first = suitcase[0:2]

# Tercer y cuarto elementos (índice dos y tres)
middle = suitcase[2:4]

# Los dos últimos elementos (índice cuatro y cinco)
last = suitcase[4:6]
```

* 8.6 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

animals = "catdogfrog"

# Los tres primeros caracteres de los animales
cat = animals[:3]

# Los caracteres cuarto a sexto
dog = 

# Desde el séptimo caractere hasta el final
frog = 
```

* 8.6 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

animals = "catdogfrog"

# Los tres primeros caracteres de los animales
cat = animals[:3]

# Los caracteres cuarto a sexto
dog = animals[3:6]

# Desde el séptimo caractere hasta el final
frog = animals[6:]
```

* 8.7 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

animals = ["aardvark", "tejón", "pato", "emu", "zorro"]
duck_index = # Utilice index() para encontrar "pato"

#¡Tu código aquí!

print(animals) # Observe lo que imprime después de la operación de inserción
```

* 8.7 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

animals = ["aardvark", "tejón", "pato", "emu", "zorro"]
duck_index = animals.index("pato")

animals.insert(0, "Oso hormiguero")
animals.insert(duck_index, "serpiente")

print(animals) # Observe lo que imprime después de la operación de inserción
```

* 8.8
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

my_list = [1,9,3,8,5,7]

for number in my_list:
	#¡Tu código aquí!
	print(number * 2)
```

* 8.9
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

start_list = [5, 3, 1, 2, 4]
square_list = []

for value in start_list:
	square_list.append(value ** 2)

print(square_list.sort())
```

* 8.10
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Asignación de un diccionario con tres pares clave-valor a los residentes:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print(residents['Puffin']) #  Imprime el número de habitación de Puffin
print(residents['Sloth'])
print(residents['Burmese Python'])
```

* 8.11
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

menu = {} # Diccionario vacío
menu['Chicken Alfredo'] = 14.50 # Adición de un nuevo par clave-valor
print menu['Chicken Alfredo']

# Su código aquí: Añadir algunos pares de precio de plato al menú!
menu['Guacamole'] = 17.10
menu['Cochinita pibil'] = 21.60
menu['Quesadilla'] = 11.30
menu['Huevos rancheros'] = 8.00
menu['Chilli'] = 10.50

print("Hay " + str(len(menu)) + "elementos en el menú.")
print(menu)
```

* 8.12
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# clave - animal_name : valor - ubicación  
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# Una declaración de diccionario (o lista) puede romperse en varias líneas

# Eliminación de la entrada 'Unicornio'. (Los unicornios son increíblemente caros.)
del zoo_animals['Unicorn']

# ¡Tu código aquí!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Falkland Islands'

print(zoo_animals)
```

* 8.13
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']

backpack.remove('dagger')
```

* 8.14
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Se ha asignado una nueva lista a la clave 'pouch'
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Añadir una 'bolsa de arpillera' clave y asignarle una lista
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Ordenar la lista que se encuentra debajo de la clave 'bolsa'
inventory['pouch'].sort()

# Su código aquí
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory['backpack'].sort()

inventory['backpack'].remove('dagger')

inventory['gold'] += 50
```

## Mini proyecto: Un día en el supermercado
* 9.1
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

names = ["Adam","Alex","Mariah","Martine","Columbus"]

for nombre in names:
	print(nombre)
```

* 9.2
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# ¡Añade tu código a continuación!
for cada_valor in webster:
	print(webster[cada_valor])
```

* 9.3
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for item in a:
	if(item % 2 == 0):
		print(item)
```

* 9.4
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Escriba una función que cuente cuántas veces aparece la cadena "fizz" en una lista.
def fizz_count(x):
  count = 0
  for item in x:
    if(item == "fizz"):
      count += 1
  return count

x = ['fazz', 'fezz', 'fizz', 'fozz', 'fuzz', 'fizz']

upperX = []
for item in x:
    upperX.append(item.upper())
    
capitalizedX = []
for item in x:
  	capitalizedX.append(item.capitalize())
    
print(upperX)
print(capitalizedX)
print(fizz_count(x))
```

* 9.5
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

for letter in "Codecademy":
	print(letter)
    
# Líneas vacías para que la salida sea bonita
print
print

word = "Programming is fun!"

for letter in word:
	# Sólo imprima la letra i
	if(letter == "i"):
		print(letter)
```

* 9.6
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pea": 3
}
```

* 9.7
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pea": 3
}

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pea": 15
}
```

* 9.8
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
once = {'a': 1, 'b': 2}
twice = {'a': 2, 'b': 4}
for key in once:
  print("Once: %s" % once[key])
  print("Twice: %s" % twice[key])
"""

#Diccionario con información de precios
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pea": 3
}

#Diccionario con información sobre stock
stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pea": 15
}

#Imprime el nombre del producto, su precio y cantidad en stock
# en orden alfabético
for key in sorted(prices):
	print("%s price: %s stock: %s" % (key, prices[key], stock[key]))
```

* 9.9
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

#Diccionario con información de precios
prices = {
  "platano": 4,
  "manzana": 2,
  "naranja": 1.5,
  "guisante": 3
}

#Diccionario con información sobre stock
stock = {
  "platano": 6,
  "manzana": 0,
  "naranja": 32,
  "guisante": 15
}

#Imprime el nombre del producto, su precio y cantidad en stock
# en orden alfabético
for key in sorted(prices):
	print("Fruta: %s - Precio: %s Stock: %s" % (key, prices[key], stock[key]))
print() #una línea en blanco
#Imprime el precio de stock de cada producto y suma el total acumulado
total = 0
for key in sorted(stock):
	result = prices[key] * stock[key]
	total += result
	print("Fruta: %s - Precio en stock: %s" % (key, result))
print("Cantidad de dinero en stock: %s" % total)
```

* 9.10
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

groceries = ["banana", "orange", "apple"]
```

* 9.11
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pea": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pea": 3
}

# ¡Añade tu código a continuación!
def compute_bill(food):
	total = 0
	for item in food:
		total += prices[item]
	return total
```

* 9.12
Has practicado
 Usando for bucles con listas y diccionarios.  
 Funciones de escritura con bucles, listas y diccionarios.  
 Actualización de datos en respuesta a cambios en el medio ambiente (por ejemplo, disminuyendo el número de plátanos en stock en 1 cuando vende uno).  

Aquí está el código final:
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pea": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pea": 3
}

# ¡Añade tu código a continuación!
def compute_bill(food):
	total = 0
	for item in food:
		if stock[item] > 0:
			total += prices[item]
			stock[item] -= 1
	return total
	
print(compute_bill(["banana", "orange", "apple", "pea"]))
```

## Quiz
¿Puedes adivinar lo que hace este programa?

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

address = ["Flat Floor Street", "18", "New York"]
pins = { "Mike": 1123, "Jow": 4468, "Jack Tequila": 0}

print(address[0], address[1])

pin = int(input("Enter your pin: "))

def find_in_file(f):
	myFile = open("sample.txt", "r")
	fruits = myFile.read()
	#fruits = fruits.splitlines()
	if f in fruits:
		return "That fruit is in the list."
	else:
		return "No such fruit found!"

if pin in pins.values():
	fruit = input("Enter a fruit: ")
	print(find_in_file(fruit))
else:
	print("Incorrect pin.")
	print("This info can only be accessed by: ")
	for key in pins.keys():
		print(key)
```
