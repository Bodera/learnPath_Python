# Bucles

#### For

* 12.1
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

#range(5) es un acceso directo para range(0, 5)
board = [] #crea una cuadrícula de 5x5 con todos los "O"s, para "océano".

for O in range(5): #horizontal 
	board.append(5 * ["O"]) #vertical
	#board.append(5 * " O  ")

for value in board: 
	print(value) #proba

print()
print(board)
```

* 12.2
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

#range(5) es un acceso directo para range(0, 5)
board = [] #crea una cuadricula de 5x5 con todos los "O"s, para "océano".

for value in range(5): #horizontal 
	board.append(5 * ["O"]) #vertical
	#board.append(5 * " O  ")

for value in board: 
	print(value) #proba

#print(board) #proba
def print_board(board_in):
	for row in board:
		print(value)
```

* 12.3
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

#range(5) es un acceso directo para range(0, 5)
board = [] #crea una cuadricula de 5x5 con todos los "O"s, para "ocano".

for O in range(5): #horizontal 
	board.append(5 * ["O"]) #vertical

#descomentar la línea para ver la prueba
#for value in board: 
	#print(value) 

#print(board)
def print_board(board_in):
	for row in board:
		print(" ".join(row))

print_board(board)
```

* 12.4
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint 

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

# ¡Añada su código abajo!
def random_row(board_in):
  return randint(0, len(board_in) - 1)

def random_col(board_in):
  return randint(0, len(board_in) - 1)

random_row(board)
random_col(board)
```

* 12.5
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# ¡Añada su código abajo!
print(ship_row) #fines de depuración
print(ship_col) #fines de depuración

guess_row = int(input("Adivina Row: "))
guess_col = int(input("Adivina Col: "))
```

* 12.6
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row) #fines de depuración
print(ship_col) #fines de depuración

guess_row = int(input("Adivina Row: "))
guess_col = int(input("Adivina Col: "))

# ¡Añada su código abajo!
if guess_row == ship_row and guess_col == ship_col:
  print("¡Felicidades! ¡Tú hundiste mi acorazado!")
```

* 12.7
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row) #fines de depuración
print(ship_col) #fines de depuración

guess_row = int(input("Adivina Row: "))
guess_col = int(input("Adivina Col: "))

# ¡Añada su código abajo!
if guess_row == ship_row and guess_col == ship_col:
  print("¡Felicidades! ¡Tú hundiste mi acorazado!")
else:
  print("¡Te perdiste mi acorazado!")
  board[guess_row][guess_col] = "X"
 
print_board(board)
```

* 12.8
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row) #fines de depuración
print(ship_col) #fines de depuración

guess_row = int(input("Adivina Row: "))
guess_col = int(input("Adivina Col: "))

# La función range() solo acepta números enteros como argumento.
if guess_row == ship_row and guess_col == ship_col:
	print("¡Felicidades! ¡Tú hundiste mi acorazado!")
elif guess_row not in range(5) or guess_col not in range(5):
	print("Ooops, eso ni siquiera está en el océano.")
else:
	print("¡Te perdiste mi acorazado!")
	board[guess_row][guess_col] = "X"
 
print_board(board)
```

* 12.9
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row) #fines de depuración
print(ship_col) #fines de depuración

guess_row = int(input("Adivina Row: "))
guess_col = int(input("Adivina Col: "))

# ¡Añada su código abajo!
if guess_row == ship_row and guess_col == ship_col:
	print("¡Felicidades! ¡Tú hundiste mi acorazado!")
elif guess_row not in range(5) or guess_col not in range(5):
	print("Ooops, eso ni siquiera está en el océano.")
elif board[guess_row][guess_col] == "X":
	print("Ya lo has adivinado.")
else:
	print("¡Te perdiste mi acorazado!")
	board[guess_row][guess_col] = "X"
 
print_board(board)
```

* 12.10
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)

#Podemos usar un bucle for para iterar a través de un rango. Cada iteración será un turno.
# ¡Todo de aquí en adelante debe ir en tu bucle for!
for turn in range(4): # 0,1,2,3.
	guess_row = int(input("Adivina Row: "))
	guess_col = int(input("Adivina Col: "))

	if guess_row == ship_row and guess_col == ship_col:
		print ("¡Felicidades! ¡Tú hundiste mi acorazado!")
	else:
		if guess_row not in range(5) or guess_col not in range(5):
			print ("Ooops, eso ni siquiera está en el océano.")
		elif board[guess_row][guess_col] == "X":
			print( "Ya lo has adivinado." )
		else:
			print ("¡Te perdiste mi acorazado!")
			board[guess_row][guess_col] = "X"
	print_board(board)
	# imprimir turno + 1 aquí
	print("Turno", turn + 1)
```

* 12.11
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)

#Podemos usar un bucle for para iterar a travs de un rango. Cada iteracin ser un turno.
# Todo de aqu en adelante debe ir en tu bucle for!
for turn in range(4): # 0,1,2,3.
	guess_row = int(input("Adivina Row: "))
	guess_col = int(input("Adivina Col: "))

	if guess_row == ship_row and guess_col == ship_col:
		print ("¡Felicidades! ¡Tú hundiste mi acorazado!")
	else:
		if turn == 3:
			print("Juego terminado")
		if guess_row not in range(5) or guess_col not in range(5):
			print ("Ooops, eso ni siquiera está en el océano.")
		elif board[guess_row][guess_col] == "X":
			print( "Ya lo has adivinado." )
		else:
			print ("¡Te perdiste mi acorazado!")
			board[guess_row][guess_col] = "X"
	print_board(board)
	# imprimir turno + 1 aquí
	print("Turno", turn + 1)
```

* 12.12
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print (ship_row)
#print (ship_col)

#Podemos usar un bucle for para iterar a travs de un rango. Cada iteracin ser un turno.
# Todo de aqu en adelante debe ir en tu bucle for!
for turn in range(4): # 0,1,2,3.
	guess_row = int(input("Adivina Row: "))
	guess_col = int(input("Adivina Col: "))

	if guess_row == ship_row and guess_col == ship_col:
		print ("¡Felicidades! ¡Tú hundiste mi acorazado!")
		break
	else:
		if turn == 3:
			print("Juego terminado")
		if guess_row not in range(5) or guess_col not in range(5):
			print ("Ooops, eso ni siquiera está en el océano.")
		elif board[guess_row][guess_col] == "X":
			print( "Ya lo has adivinado." )
		else:
			print ("¡Te perdiste mi acorazado!")
			board[guess_row][guess_col] = "X"
	print_board(board)
	# imprimir turno + 1 aquí
	print("Turno", turn + 1)
```

## Próximos pasos
1. Crea múltiples acorazados: deberás tener cuidado porque debes asegurarte de no colocarlos encima del otro en el tablero de juego. También querrás asegurarte de equilibrar el tamaño del tablero con la cantidad de barcos, por lo que el juego sigue siendo desafiante y divertido de jugar.

2. Crea acorazados de diferentes tamaños: esto es más complicado de lo que parece. Todas las partes del acorazado deben estar en contacto vertical u horizontal y debes asegurarte de no colocar accidentalmente parte de un barco fuera del costado del tablero.

3. Haz de tu juego un juego para dos jugadores.

4. ¡Usa las funciones para permitir que tu juego tenga más funciones como revanchas, estadísticas y más!

#### While

* 13.1 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

#El bucle while
#En lugar de ejecutar si algo es verdadero, se ejecuta mientras esa cosa es verdadera.

count = 0

if count < 5:
	print("Hello, I am an if statement and count is", count)

while count < 5:
	print("Hello, I am a while and count is", count)
	count += 1
```

* 13.1 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

count = 0

if count < 5:
	print("Hello, I am an if statement and count is", count)

while count < 10:
	print("Hello, I am a while and count is", count)
	count += 1
```

* 13.2
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

#La variable loop_condition se establece en True
loop_condition = True 

#El ciclo while comprueba si loop_condition es True. Es así que se ingresa al bucle.
while loop_condition:
	#La declaración de impresión se ejecuta.
	print("I am a loop")
	#La variable loop_condition se establece en False.
	loop_condition = False

#El ciclo while vuelve a comprobar si loop_condition es True.
#No lo es, por lo que el bucle no se ejecuta por segunda vez.
```

* 13.3 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

num = 1

while _______:  #Rellene la condición
  #Imprimir num al cuadrado
  #Incremento num (¡asegúrese de hacer esto!)
```

* 13.3 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

num = 1

while num <= 10:  #Rellene la condición
    #Imprimir num al cuadrado
    print(num ** 2)
    #Incremento num (¡asegúrese de hacer esto!)
    num += 1
```

* 13.4 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

choice = input("¿Disfrutas de Python? (y/n)")

while ________:  #Rellene la condición (antes de los dos puntos)
	choice = input("Lo siento, no entendí eso. Entre de Nuevo: ")
```

* 13.4 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

choice = input("¿Disfrutas de Python? (y/n)")

while choice != 'y' and choice != 'Y' and choice != 'n' and choice != 'N':  #Rellene la condición (antes de los dos puntos)
	choice = input("Lo siento, no entendí eso. Entre de nuevo: ")
```

* 13.5 delante
```python
#Un bucle infinito es un bucle que nunca sale. Esto puede suceder por algunas razones:

#La condición de bucle no puede ser falsa (por ejemplo, mientras 1 != 2)

#La lógica del bucle evita que la condición del bucle se vuelva falsa.

count = 0

while count < 10
    print (count)

```

* 13.5 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
count = 0

while count < 10:
    print (count)
    count += 1
```

* 13.6
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

#El break es una declaración de una línea que significa "salir del bucle actual".
#Se garantiza que el bucle se ejecute al menos una vez.
count = 0

while True:
    print (count)
    count += 1
    if count >= 10:
        break
```

* 13.7
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

#Algo completamente diferente sobre Python es la construcción while/else. while/else es similar a if/else, pero hay una diferencia: el bloque else se ejecutará cada vez que la condición del bucle se evalúe como False. Esto significa que se ejecutará si el ciclo nunca se ingresa o si el ciclo sale normalmente. Si el ciclo sale como resultado de un break, el resto no se ejecutará.
#En este ejemplo, el bucle se romperá si se genera un 5 y el resto no se ejecutará. De lo contrario, después de que se generen 3 números, la condición del bucle se convertirá en falsa y el resto se ejecutará.

import random

print ("¡Números de la suerte! Se generarán 3 números.")
print ("Si uno de ellos es un '5', ¡pierdes!")

count = 0
while count < 3:
  	num = random.randint(1, 6)
  	print (num)
  	if num == 5:
	    print ("Lo siento, ¡pierdes!")
	    break
  	count += 1
else:
  	print ("¡Ganaste!")
```

* 13.8 delante
```python
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!

```

* 13.8 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

#Del módulo random solo importamos la función randint
from random import randint 

#Genera un número del 1 al 10 inclusive
random_number = randint(1, 10)

guesses_left = 3

#¡Comienza tu juego!
print("¡Bienvenido a mi juego de azar!")
print("Tienes tres oportunidades para acertar en el misterioso número. 1 a 10")

while guesses_left != 0:
	guess = int(input("Dime qué número crees que és.\n"))
	if (guess == random_number):
		print("¡Ganaste!")
		break
	guesses_left -= 1
else:
	print("Perdíste.")
```

* 13.9 delante
```python
print ("Contando...")

for i in range(10):
  print (i)
```

* 13.9 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

print ("Contando...")

for i in range(20):
  print (i)
```

* 13.10 delante
```python
hobbies = []

#¡Agregue su código a continuación!
```

* 13.10 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

hobbies = []

# ¡Agregue su código a continuación!
for i in range(3):
	hobby = input("Tell me your hobbies: ")
	hobbies.append(hobby)

print(hobbies)
```

* 13.11 delante
```python
thing = "spam!"

for c in thing:
    print (c)

word = "eggs!"

#¡Agregue su código a continuación!
```

* 13.11 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

thing = "spam!"

for c in thing:
  	print (c)

word = "eggs!"

#¡Agregue su código a continuación!
for char in word:
    print(char)
```

* 13.12 delante
```python
phrase = "A bird in the hand..."

#Agregue su bucle for





#¡No elimine esta declaración print!
print
```

* 13.12 después
```python
#Filtremos la letra "A" de nuestra cadena.
phrase = "A bird in the hand..."

#Agregue su bucle for
#!/usr/bin/python
# -*- coding: utf-8 -*-

phrase = "A bird in the hand..."

#Agregue su bucle for
for char in phrase:
    if char == "A" or char == "a":
        print ("X", end="")
    else:
    	print (char, end="")

#¡No elimine esta declaración print!
print()
```

* 13.13 delante
```python
#Quizás el uso más útil (y más común) de for bucles es revisar una lista
#En cada iteración, la variable num será el siguiente valor en la lista. Entonces, la primera vez, será 7, la segunda será 9, luego 12, 54, 99, y luego el bucle saldrá cuando no haya más valores en la lista.
numbers  = [7, 9, 12, 54, 99]

print ("Esta lista contiene: ")

for num in numbers:
	print (num)

#¡Agrega tu bucle a continuación!
```
* 13.13 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

numbers  = [7, 9, 12, 54, 99]

print ("Esta lista contiene: ")

for num in numbers:
	print (num)

#¡Agrega tu bucle a continuación!
for number in numbers:
    print(pow(number,2))
```

* 13.14
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    #¡Tu código aquí!
    print(key + " " + d[key])
```

* 13.15 delante
```python
choices = ['pizza', 'pasta', 'salad', 'nachos']

print ('Sus elecciones son:')
for index, item in enumerate(choices):
  print (index, item)
```

* 13.15 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

choices = ['pizza', 'pasta', 'salad', 'nachos']

print ('Sus elecciones son:')
for index, item in enumerate(choices):
    index += 1
    print (index, item)
```

* 13.16 delante
```python
#También es común tener que repetir dos listas a la vez. Aquí es donde la función zip incorporada es útil.
#zip creará pares de elementos cuando pasen dos listas, y se detendrá al final de la lista más corta.
#¡zip también puede manejar tres o más listas!

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
#Salida: (3,2), (9,4), (17,8), (15,10), (19,30)
```

* 13.16 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    #¡Agrega tu código aquí!
    if a > b:
        print (a)
    else:
        print (b)
```

* 13.17
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

#En este caso, la instrucción else se ejecuta después de for, pero solo si for for finaliza normalmente, no con una instrucción break. Este código se romperá cuando llegue a 'tomate', por lo que el bloque else no se ejecutará.

#Juega con este código para cambiar su salida.

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print ('You have...')
for f in fruits:
    if f == 'tomato':
        print ('A tomato is not a fruit!') # (De hecho lo es.)
        break
    print ('A', f)
else:
    print ('A fine selection of fruits!')
```

* 13.18
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

#Cree su propia declaración for/else desde cero

from time import perf_counter 

time_start = perf_counter()

personas = ["Benjamín", "Maite", "Gaspar", "Elena", "Mabel"]
edad = [27, 52, 18, 34, 40]
sexo = ["Hombre", "Mujer", "Hombre", "Mujer", "Periodista"]

mas_viejo = max(edad)

for a, b, c in zip(personas, edad, sexo):
    if (c == 'Mujer'):
        print(a, "tiene", b, "años y es una", c)
    elif (c == 'Hombre'):
        print(a, "tiene", b, "años y es un", c)
    else:
        print(a, "tiene", b, "años pero no sé lo qué es", c)
else:
    for a, b in zip(personas, edad):
        if (b == mas_viejo):
            print(a, "es la persona más vieja.")

time_stop = perf_counter()

print("Elapsed time:", time_stop - time_start)
```

## Practicando lo que aprendiste

* 14.1 
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

print(is_even(19))
```

* 14.2
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def is_int(x):
    if (x == int(x)):
        return True
    else:
        return False

print(is_int(-19.0000))
```

* 14.3
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
def digit_sum(n):
    a = 0
    if n < 0:
        n = n * -1
        while n > 0:
            a += int(n % 10) #incremento de la variable auxiliar
            n = n // 10 #efectuando división entera
        return a
    elif n == 0:
        return n
    else:
        while n > 0:
            a += int(n % 10)
            n = n // 10
        return a

print(digit_sum(212))
```

* 14.4
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
def factorial(x):
    if x > 0:
        return x * factorial(x - 1) #función recursiva
    elif x == 0:
        return 1
    else:
        return False

print(factorial(6))
```

* 14.5
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
def is_prime(x):
    if x <= 1: #Los números primos también deben ser mayores que 1
        return False
    elif x == 2:
        return True
    else:
        for value in range(2, x): #range(start, stop)
            if not x % value:
                return False
        return True
print(is_prime(9))
```

* 14.6
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
def reverse(text):
    reversed_text = ""
    #print(lent(text))
    text_length = len(text) - 1
    #print(text[text_length])
    while text_length >= 0:
        reversed_text += text[text_length]
        text_length -= 1
    return reversed_text
print (reverse("»»B²A¹««"))
```

* 14.7
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def anti_vowel(text):
    new_text = ""
    for char in text:
        if char.lower() not in "aeiou":
            new_text += char
    return new_text
print (anti_vowel("Buenos días!"))
```

* 14.8
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    word = word.lower()
    total_points = 0
    for letter in word:
        if letter in score:
            total_points += score.get(letter)
    return total_points
print(scrabble_score("Oponopono"))
```

* 14.9
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def censor(text, word):
    words = text.split()
    print(words)
    result = ''
    stars = '*' * len(word)
    count = 0
    for match in words:
        if match == word:
            words[count] = stars
        count += 1
    result = ' '.join(words)
    return result
print(censor('lala Opa opa opa', 'opa'))
```

* 14.10
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def count(sequence, item):
    #return sequence.count(item) #esta manera es hacer trampa
    total = 0
    for value in range(len(sequence)): #de cero a len(sequence)-1
        if sequence[value] == item:
            total+=1
    return total
print (count([['0',1,0,1,1]], ['0',1,0,1,1]))
"""
Alternativa
def count(sequence, item):
    count = 0
    for i in sequence:
        if sequence[i] == item:
            count += 1
    return count
  
print count([[1,1]], [1])
"""
```

* 14.11
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def purify(integer_list):
    purified_list = []
    for value in integer_list:
        if value % 2 == 0:
            purified_list.append(value)
    return purified_list
print(purify([1,2,3,4,5,6,7,8,9,10]))
```

* 14.12
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def product(integer_list):
    total = 1
    for value in integer_list:
        if len(integer_list) < 1:
            return 0
            break
        total *= value
    return total
print (product([1,2,1,2,5]))
```

* 14.13
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def remove_duplicates(user_list):
    #los diccionarios no pueden tener claves duplicadas
    processed_list = list(dict.fromkeys(user_list))
    return processed_list
print (remove_duplicates([1,2,3,1,3]))
"""
Alternativa

def remove_duplicates(user_list):
    processed_list = []
    for value in user_list:
        if value not in processed_list:
            processed_list.append(value)
    return processed_list
print (remove_duplicates([1,2,3,1,3]))
"""
```

* 14.14
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

#Thanks to Er CEO Vora Mayur
#https://stackoverflow.com/questions/45003783/how-do-i-find-the-median-of-a-list-in-python
def median(user_list):
    ordered_list = sorted(user_list)
    if len(ordered_list) % 2 == 1:
        return ordered_list[(len(ordered_list)+1)//2-1]
    else:
        lower = ordered_list[(len(ordered_list)+1)//2-1]
        upper = ordered_list[(len(ordered_list)+1)//2]
        print(lower, upper)
        return (lower+upper) / 2.0 
        #return float(lower+upper) / 2
print (median([1,2,3,4,5,6,7,8,9,10]))
```
