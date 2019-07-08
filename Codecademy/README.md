# Learn Python 2 [crash Codecademy](https://www.codecademy.com/learn/learn-python)

## Atención
El soporte para Python 2 ha terminado. En enero, 01 de 2020 [este reloj](https://pythonclock.org/) han alcanzado el 0. Los ejemplos expuestos aquí fueron probados y ejecutados de forma sin pudoras en Python 3.6

__[Debes estudiar chicx](https://docs.python.org/3/)__

## Sintaxis
* 1.1
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
print('Hola')
```

* 1.2
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
print('Guaco')
print('Marijuana')
print('Muerte')
```

* 1.3
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
print "Hola " + 'el macho cabrío'
```

* 1.4 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
print("How do you make a hot dog stand?')
print(You take away its chair!)
```

* 1.4 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
print('How do you make a hot dog stand?')
print("You take away its chair!")
```

* 1.5
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
todays_date = '2019/06/24'
```

* 1.6
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
product = 45 * 3
remainder = 1398 % 11
print(remainder)
```

* 1.7 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06
```

* 1.7 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
annual_rainfall += september_rainfall

october_rainfall = 7.20
annual_rainfall += october_rainfall

november_rainfall = 5.06
annual_rainfall += november_rainfall

december_rainfall = 4.06
annual_rainfall += december_rainfall
```

* 1.8
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
city_name = "St. Potatosburg"
# la siguiente variable contiene un número entero que representa la suma de ciudadanos
city_pop = 340000
```

* 1.9
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
cucumbers = 6 #Número de pepinos que me gustaría comprar.
price_per_cucumber = 3.25
total_cost = cucumbers * price_per_cucumber
print(total_cost)
print(type(total_cost))

### float2 = 10. ### 10.0
### float4 = 1.5e2 ### 150
```

* 1.10
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
cucumbers = 100
num_people = 6

whole_cucumbers_per_person = cucumbers / num_people
print(whole_cucumbers_per_person)

float_cucumbers_per_person = cucumbers / float(num_people)
print(float_cucumbers_per_person)
```

* 1.11
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
haiku = """Você pode crer
O pior cego
É o que quer ver."""
print(haiku)
"""
It can also be used as a multi-line comment
"""
```

* 1.12
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Hi! I'm Maria and I live in script.py.
# I'm an expert Python coder.
# I'm 21 years old and I plan to program cool stuff forever.
age_is_12 = False
print(int(age_is_12))

name_is_maria = True
print(int(name_is_maria))
```

* 1.13
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
float_1 = 0.25
float_2 = 40.0

product = float_1 * float_2
big_string = "The product was " + str(product)

print(big_string)
```

* 1.14
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
skill_completed = 'Python Syntax'
exercises_completed = 13
# la siguiente variable contiene la cantidad de puntos para cada ejercicio puede cambiar, porque los puntos aún no existen
points_per_exercise = 5 # float would be 5.
point_total = 100
point_total += exercises_completed * points_per_exercise

print("Tengo "+str(point_total)+" puntos!")
```

## Cadenas
* 2.1
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
brian = "Hola vida!"
```

* 2.2 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Assign your variables below, each on its own line!


# Put your variables above this line

print caesar
print praline
print viking
```

* 2.2 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Assign your variables below, each on its own line!

caesar = "Graham"
praline = "John"
viking = "Teresa"

# Put your variables above this line

print caesar
print praline
print viking
```

* 2.3 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
# The string below is broken. Fix it using the escape backslash!

print('This isn't flying, this is falling with style!')
```

* 2.3 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
# The string below is broken. Fix it using the escape backslash!

print('This isn\'t flying, this is falling with style!')
```

* 2.4
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""

word = "MONTY"
fifth_letter = word[4]

print fifth_letter
```

* 2.5
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
parrot = "Norwegian Blue"
print( len(parrot)) # Comience a contar desde 1. Los espacios en blanco también cuentan.
```

* 2.6
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
parrot = "Norwegian Blue"
print( parrot.lower()) # Or "Norwegian Blue".lower()
```

* 2.7
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
parrot = "Norwegian Blue"
print( parrot.upper())
```

* 2.8
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
pi = 3.14159265359
print( str(pi))
```

* 2.9
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
ministry = "The Ministry of Silly Walks"

print (len(ministry))
print ministry.upper()
```

* 2.10
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Dile a Python que imprima "Monty Python"
a la linea de consola 4!"""

print ("Monty Python")
```

* 2.11
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Asigna la cadena "Ping!" a
la variable the_machine_goes on
línea 5, luego imprímela en la línea 6!"""

the_machine_goes = "Ping!"
print (the_machine_goes)
```

* 2.12
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Imprima la concatenación de "Spam y huevos" en la línea 3!

print("Spam " + "y " + "huevos")
```

* 2.13 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
print "El valor de pi está alrededor " + 3.1415
```

* 2.13 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
print "El valor de pi está alrededor " + str(3.1415)
```

* 2.14
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
string_1 = "Camelot"
string_2 = "lugar"

print "No vamos a %s. Este es un %s tonto." % (string_1, string_2)
# Salida: No vamos a Camelot. Este es un lugar tonto.

day = 6
print "03 - %s - 2019" %  (day)
# 03 - 6 - 2019
print "03 - %02d - 2019" % (day)
# 03 - 06 - 2019
```

* 2.15 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
name = raw_input("¿Cuál es su nombre?")
quest = raw_input("¿Cuál es tu búsqueda?")
color = raw_input("¿Cuál es tu color favorito?")

print "Ah, entonces tu nombre es ___, tu búsqueda es ___, " \
"y tu color favorito es ___." ___ (name, quest, color)
```

* 2.15 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
name = raw_input("¿Cuál es su nombre?")
quest = raw_input("¿Cuál es tu búsqueda?")
color = raw_input("¿Cuál es tu color favorito?")

print "Ah, entonces tu nombre es %s, tu búsqueda es %s, " \
"y tu color favorito es %s." %s (name, quest, color)
```

* 2.16
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
# tres formas de crear cadenas
str_1 = 'Alpha'
str_2 = "Bravo"
str_3 = str(3)

# métodos de cadena
len("Charlie")
"Delta".upper()
"Echo".lower()

# imprimiendo una cadena
print "Foxtrot"

# tecnicas avanzadas de impresion
g = "Golf"
h = "Hotel"
print "%s, %s" % (g, h)

my_string = """El gato,
sólo el gato
apareció completo
y orgulloso:
nació completamente terminado,
camina solo y sabe lo que quiere."""
print ( len(my_string) )
print (my_string.upper())
```

## Fecha y hora
* 3.1
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
```

* 3.2
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime

now = datetime.now()
print(now)
```

* 3.3
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime

now = datetime.now()

print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
```

* 3.4
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
now = datetime.now()

print('%02d/%02d/%04d') % (now.day, now.month, now.year)
# como resultado tenemos dd-mm-yyyy
```

* 3.5
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
now = datetime.now()

print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)
```

* 3.6
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
now = datetime.now()

print ('%02d/%02d/%04d' + ' ' '%02d:%02d:%02d') % (now.month, now.day, now.year, now.hour, now.minute, now.second)
```

## Condiciones y flujo de control
* 4.1
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def clinic():
    print "¡Acabas de entrar a la clínica!"
    print "¿Tomas la puerta de la izquierda o de la derecha?"
    answer = raw_input("Escriba izquierda o derecha y presione 'Enter'.").lower()
    if answer == "izquierda" or answer == "i":
        print "Esta es la Sala de Abuso Verbal, ¡montón de excrementos de loros!"
    elif answer == "derecha" or answer == "d":
        print ("Por supuesto, esta es la Sala de Argumentos, ¡ya te lo dije!")
    else:
        print ("¡No elegiste izquierda o derecha! Inténtalo de nuevo.")
        clinic()

clinic()
```

* 4.2
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Comparar de cerca!
Comencemos con el aspecto más simple del flujo de control: comparadores. Hay seis:

Igual a (==)
>>> 2 == 2
Cierto
>>> 2 == 5
Falso

No es igual a (! =)
>>> 2! = 5
Cierto
>>> 2! = 2
Falso

Menos que (<)
>>> 2 < 5
Cierto
>>> 5 < 2
Falso

Menor o igual que (<=)
>>> 2 <= 2
Cierto
>>> 5 <= 2
Falso

Mayor que (>)
>>> 5 > 2
Cierto
>>> 2 > 5
Falso

Mayor o igual que (> =)
>>> 5 >= 5
Cierto
>>> 2 >= 5
Falso

Los comparadores verifican si un valor es (o no es) igual a, mayor que (o igual a), o menor que (o igual a) otro valor.

Tenga en cuenta que == compara si dos cosas son iguales, y = asigna un valor a una variable.
"""

#¡Asigne Verdadero o Falso según corresponda en las líneas de abajo!

# Establézcalo en Verdadero si 17 < 328 o en Falso si no lo es.
bool_one = True   # ¡Hicimos esto por ti!

# Establézcalo en Verdadero si 100 == (2 * 50) o en Falso en caso contrario.
bool_two = True

# Establézcalo en Verdadero si 19 <= 19 o en Falso si no lo es.
bool_three = True

# Establézcalo en Verdadero si -22 >= -18 o en Falso si no lo es.
bool_four = False

# Establézcalo en Verdadero si 99 != (98 + 1) o en Falso en caso contrario.
bool_five = False
```

* 4.3
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# ¡Asigne Verdadero o Falso según corresponda en las líneas de abajo!

# (20 - 10)> 15
bool_one = Falso # ¡Hicimos esto por ti!

# (10 + 17) == 3 ** 16
# Recuerde que ** se puede leer como 'al poder de'. 3 ** 16 es de unos 43 millones.
bool_two = Falso

# 1 ** 2 <= -1
bool_three = Falso

# 40 * 4> = -4
bool_four = Verdadero

# 100! = 10 ** 2
bool_five = Falso
```

* 4.4
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# ¡Cree declaraciones comparativas según corresponda en las siguientes líneas!

# ¡Hazme Verdadero!
bool_one = 3 < 5 # ¡Ya hicimos esto por ti!

# ¡Hazme falso!
bool_two = 'S' == 's'

# ¡Hazme Verdadero!
bool_three = 16 % 2 == 0

# ¡Hazme falso!
bool_four = 9999 != 10000 - 1

# ¡Hazme Verdadero!
bool_five = 2 ** 50 >= 1125899906842624
```

* 4.5
Los operadores booleanos comparan sentencias y dan como resultado valores booleanos.
Hay tres operadores booleanos:

Y, que comprueba si ambas afirmaciones son verdaderas;
O, que verifica si al menos una de las afirmaciones es Verdadera;
No, lo que da lo contrario de la afirmación.

* 4.6
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

bool_one = False and False

bool_two = -(-(-(-2))) == -2 and 4 >= 16 ** 0.5

bool_three = 19 % 4 != 300 / 10 / 10 and False

bool_four = -(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2

bool_five = True and True
```

* 4.7
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

bool_one = 2 ** 3 == 108 % 100 or 'Cleese' == 'King Arthur'

bool_two = True or False

bool_three = 100 ** 0.5 >= 50 or False

bool_four = True or True

bool_five = 1 ** 100 == 100 ** 1 or 3 * 2 * 1 != 3 + 2 + 1
```

* 4.8
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

bool_one = not True

bool_two = not 3 ** 4 < 4 ** 3

bool_three = not 10 % 3 <= 10 % 2

bool_four = not 3 ** 2 + 4 ** 2 != 5 ** 2

bool_five = not not False

```

* 4.9
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
No se evalúa primero;
Y se evalúa a continuación;
O se evalúa en último lugar.

Los paréntesis () aseguran que sus expresiones se evalúen en el orden que desee.
Cualquier cosa entre paréntesis se evalúa como su propia unidad.
"""

bool_one = False or not True and True

bool_two = False and not True or True

bool_three = True and not (False or False)

bool_four = not not True or False and not True

bool_five = False or not (True and True)
```

* 4.10
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# ¡Use expresiones booleanas según corresponda en las líneas de abajo!

# ¡Hazme falso!
bool_one = (2 <= 2) y "Alpha" == "Bravo" # ¡Hicimos esto por ti!

# ¡Hazme Verdadero!
bool_two = no Falso o no Verdadero

# ¡Hazme falso!
bool_three = (1 ** 0) == 0 y (0 ** 2) == 0

# ¡Hazme Verdadero!
bool_four = (1 ** 0)> = 1 y (0 ** 2) <2

# ¡Hazme Verdadero!
bool_five = 'ç' == 'ç' y 109! = 190
```

* 4.11 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

answer =

answer = "Izquierda"
if respuesta == "Izquierda":
     print ("Esta es la Sala del Abuso Verbal, ¡montón de excrementos de loros!")
    
# ¿Se imprimirá la declaración de impresión anterior en la consola?
# Ajuste la respuesta a 'Y' si lo cree, y 'N' si no lo cree.

```

* 4.11 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

answer = Y

answer = "Izquierda"
if respuesta == "Izquierda":
     print ("Esta es la Sala del Abuso Verbal, ¡montón de excrementos de loros!")
```

Preste atención a la sangría antes de la declaración de impresión.
Este espacio, llamado espacio en blanco, es cómo Python sabe que estamos ingresando un nuevo bloque de código.
Python acepta muchos tipos diferentes de sangría para indicar bloques.
En esta lección, usamos cuatro espacios, pero en otros lugares puede encontrar 
sangrías o tabulaciones de dos espacios (que Python verá como diferentes de los espacios).

Si la sangría de una línea a la siguiente es diferente y no hay un comando (como si) que indique un bloque entrante,
Python generará un error de sangría. Estos errores podrían significar, por ejemplo, 
que una línea tenía dos espacios, pero la siguiente tenía tres. Python intenta indicar dónde 
ocurrió este error imprimiendo la línea de código que no pudo analizar y usando un `^` para señalar 
donde la sangría era diferente de lo que esperaba.

* 4.12 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def using_control_once():
    if _______:
        return "Success #1"

def using_control_again():
    if _______:
        return "Success #2"

print using_control_once()
print using_control_again()
```

* 4.12 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def using_control_once():
	if (0 > -1):
		return "Success #1"

def using_control_again():
	if ('55' != 55):
		return "Success #2"

print using_control_once()
print using_control_again()
```

Mirando el ejemplo anterior, en el caso de que some_function() devuelva True,
se ejecutará el bloque de código con sangría.
 En el caso de que devuelva False, se omitirá el bloque con sangría.

* 4.13
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

answer = "¡Es solo un rasguño!"

def black_knight ():
	if (answer == "¡Es solo un rasguño!"):
		return True
	else:
		return False # Asegúrate de que devuelve False

def french_soldier ():
	if (answer == "¡Vete o te burlaré de ti por segunda vez!"):
		return True
	else:
		return False # Asegúrate de que devuelve False
```

* 4.14 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def greater_less_equal_5(answer):
    if ________:
        return 1
    elif ________:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

```

* 4.14 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def greater_less_equal_5(answer):
    if (answer > 5):
        return 1
    elif (answer < 5):          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

```

* 4.15
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

## Completa las declaraciones if y elif!
def grade_converter(grade):
    if (grade >= 90):
        return "A"
    elif (grade >= 80 and grade <= 89):
        return "B"
    elif (grade >= 70 and grade <= 79):
        return "C"
    elif (grade >= 65 and grade <= 69):
        return "D"
    else:
        return "F"
      
# Esto debería imprimir un "A     
print grade_converter(92)

# Esto debería imprimir un "C"
print grade_converter(70)

# Esto debería imprimir un "F"
print grade_converter(61)
```

## Mini proyecto
1. Pídale al usuario que ingrese una palabra en inglés.  
2. Asegúrese de que el usuario ingresó una palabra válida.  
3. Convierte la palabra del inglés al cerdo latino.  
4. Muestra el resultado de la traducción.  

* 5.1
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

print("Pig Latin")
```

* 5.2
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
print("¡Bienvenido al traductor de cerdo latino!")

# ¡Comience a codificar aquí!
original = raw_input ("Ingrese una palabra en inglés: ")
```

* 5.3
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
print("¡Bienvenido al traductor de cerdo latino!")

# ¡Comience a codificar aquí!
original = raw_input ("Ingrese una palabra en inglés: ")

# comprobando entradas válidas
if len(original) > 0:
	print(original)
else:
	print("vacío")
```

* 5.4
¡Puedes usar `.isalpha()` para verificar que una cadena no contenga caracteres que no sean letras!
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
print("¡Bienvenido al traductor de cerdo latino!")

# ¡Comience a codificar aquí!
original = raw_input ("Ingrese una palabra en inglés: ")

# comprobando entradas válidas
if len(original) > 0 and original.isalpha():
	print(original)
else:
	print("vacío")
```

* 5.5
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

pyg = 'ay'
```

* 5.6
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

pyg = 'ay'

original = raw_input("Ingrese una palabra en inglés: ")

if len(original) > 0 and original.isalpha():
	print original
	word = original.lower()
	first = word[0]
else:
	print("vacío")
```

* 5.7
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

pyg = 'ay'

original = raw_input("Ingrese una palabra en inglés: ")

if len(original) > 0 and original.isalpha():
  print original
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
else:
  print print("vacío")
```

* 5.8
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
s = "Charlie"

print s[0]
#"C"

print s[1:4]
#"har"
"""

pyg = 'ay'

original = raw_input("Ingrese una palabra en inglés: ")

if len(original) > 0 and original.isalpha():
	print original
	word = original.lower()
	first = word[0]
	new_word = word + first + pyg
	new_word = new_word[1:len(new_word)]
else:
	print("vacío")
```

* 5.9
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

pyg = 'ay'

original = raw_input("Ingrese una palabra en inglés: ")

if len(original) > 0 and original.isalpha():
	word = original.lower()
	first = word[0]
	new_word = word + first + pyg
	new_word = new_word[1:len(new_word)]
	print(new_word)
else:
	print("vacío")
```

## Funciones
* 6.1
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def tax(bill):
	"""Agrega un 8% de impuestos a la factura de un restaurante."""
	bill *= 1.08
	print("Con impuestos: %.2f") % bill
	return bill

def tip(bill):
	"""Agrega un 15% de propina a la factura de un restaurante."""
	bill *= 1.15
	print("Con propina:  %.2f") % bill
	return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)
```

* 6.2
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Defina su función de spam comenzando en la línea 5. Usted
# puede dejar el código en la línea 10 solo por ahora.
# ¡Explícalo pronto!
def spam():
	"""Imprime un mensaje en la consola"""
	print("Huevos!")


# Definir la función de spam por encima de esta línea.
spam()
```

* 6.3
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def square(n):
	"""Devuelve el cuadrado de un número."""
	squared = n ** 2
	print("%d al cuadrado es %d.") % (n, squared)
	return squared

# ¡Llama a la función square en la línea 13! Asegurate que
# incluir el número 10 entre los paréntesis.

square(10)
```

* 6.4
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def power(base, exponente): # ¡Añade tus parámetros aquí!
	resultado = base ** exponente
	print("%d a la potencia de %d es %d.") % (base, exponente, resultado)

power(37, 4) # ¡Añade tus argumentos aquí!
```

* 6.5 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def one_good_turn(n):
	return n + 1
    
def deserves_another(n):
	return n + 2
```

* 6.5 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def one_good_turn(n):
	return n + 1
    
def deserves_another(n):
	n = one_good_turn(n)
	return n + 2
```

* 6.6
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def cube(number):
	return number ** 3

def by_three(number):
	if (number % 3 == 0):
		return cube(number)
	else:
		return False
```

* 6.7
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Pídale a Python que imprima sqrt(25) en la línea 3.

print(sqrt(25))
```

* 6.8
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import math # importación genérica
print(math.sqrt(25))
```

* 6.9
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importar * solo * la función sqrt de matemáticas en la línea 3!

from math import sqrt # importación de función
```

* 6.10
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importar todo desde el módulo de matemáticas en la línea 3!

from math import * # importacion universal
```

* 6.11
Las importaciones universales pueden parecer óptimas en la superficie,
pero no son una buena idea por una razón muy importante: ellas llenan su programa 
con una tonelada de nombres de variables y de funciones sin la seguridad
de esos nombres todavía asociados al módulo o módulos (s) ellos vinieron de.

Si usted tiene una función de su propio dominio nombrado `sqrt` y usted importa `math`,
su función es segura: existe su `sqrt` y existe el `math.sqrt`. Si hace a partir de la
importación de `math *`, sin embargo, usted tiene un problema: a saber, dos funciones diferentes con el mismo nombre.

Incluso si sus propias configuraciones no entran en conflicto directo con los
nombres de los módulos importados, si importa `*` de varios módulos a 
la vez, no podrá averiguar qué variable o función viene de dónde.

Por estos motivos, es mejor utilizar el módulo de importación y escribir
`module.name` o sólo importar variables y funciones específicas de varios módulos, según sea necesario.

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importar todo desde el módulo de matemáticas en la línea 3!

import math # importa el módulo de matemáticas
everything = dir(math) # Lo establece todo en una lista de cosas de math
print(everything) # ¡Imprímelos todo!
```

* 6.12
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def biggest_number(*args):
  print max(args)
  return max(args)
    
def smallest_number(*args):
  print min(args)
  return min(args)

def distance_from_zero(arg):
  print abs(arg)
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)
```

* 6.13
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# ¡Establezca el máximo al valor máximo de cualquier conjunto de números en la línea 3!

maximum = max(1500, 103 * 32, 2 ** 16)

print(maximum)
```

* 6.14
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# ¡Establezca el mínimo en el valor mínimo de cualquier conjunto de números en la línea 3!

minimum = min(9/5., abs(-5109), 11/4.)

print(minimum)
```

* 6.15
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

absolute = abs(-42)

print absolute
```

* 6.16
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imprima los tipos de un entero, un flotante,
# y una cadena en líneas separadas debajo.

print(type(1999))
print(type(3.1415))
print(type('Cadena'))

test = True if type(1999) == int else False #Operador ternario :)

print(test)
```

* 6.17
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def shut_down(s):
  if (s == 'yes' or s == 'y'):
    return "Shutting down"
  elif (s == 'no' or s == 'n'):
    return "Shutdown aborted"
  else:
    return 'Sorry'
```

* 6.18
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import sqrt

print(math.sqrt(13689))
```

* 6.19
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def distance_from_zero(arg):
	if(type(arg) ==  int or type(arg) == float):
		return abs(arg)
	else:
		return 'Nope'
```

## Mini proyecto: tomando unas vacaciones
* 7.1
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def answer():
	return 42
```

* 7.2
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def hotel_cost(nights):
	return 140 * nights
```

* 7.3
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def hotel_cost(nights):
	return 140 * nights

def plane_ride_cost(city):
	if city == 'Charlotte':
		return 183
	if city == 'Tampa':
		return 220
	if city == 'Pittsburgh':
		return 222
	if city == "Los Angeles":
		return 475
```

* 7.4
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def hotel_cost(nights):
	return 140 * nights

def plane_ride_cost(city):
	if city == 'Charlotte':
		return 183
	if city == 'Tampa':
		return 220
	if city == 'Pittsburgh':
		return 222
	if city == "Los Angeles":
		return 475
  
def rental_car_cost(days):
	rental = 40
	if days >= 7:
		rental *= days
		rental -= 50
		return rental
	elif days >= 3 and days < 7:
		rental *= days
		rental -= 20
		return rental
	elif days >= 0 and days <= 2 :
		rental *= days
		return rental
	else:
		return "Nope."
```

* 7.5
Como queremos que el costo del viaje dependa solo de dos parámetros, 
tenemos que convertir las noches variables en días. Si va a quedarse en algún lugar,
la cantidad de noches que se hospede allí será inferior a la cantidad de días 
que estuvo allí (imagine un viaje de fin de semana para visitar a su familia, 
se va de sábado y regresa el domingo, de modo que la visita por dos días, 
Pero solo se queda una noche).
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def hotel_cost(nights):
	return 140 * nights

def plane_ride_cost(city):
	if city == 'Charlotte':
		return 183
	if city == 'Tampa':
		return 220
	if city == 'Pittsburgh':
		return 222
	if city == "Los Angeles":
		return 475
  
def rental_car_cost(days):
	rental = 40
	if days >= 7:
		rental *= days
		rental -= 50
		return rental
	elif days >= 3 and days < 7:
		rental *= days
		rental -= 20
		return rental
	elif days >= 0 and days <= 2 :
		rental *= days
		return rental
	else:
		return "Nope."

def trip_cost(city, days):
	return rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(days - 1)
```

* 7.6
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def hotel_cost(nights):
	return 140 * nights

def plane_ride_cost(city):
	if city == 'Charlotte':
		return 183
	if city == 'Tampa':
		return 220
	if city == 'Pittsburgh':
		return 222
	if city == "Los Angeles":
		return 475
  
def rental_car_cost(days):
	rental = 40
	if days >= 7:
		rental *= days
		rental -= 50
		return rental
	elif days >= 3 and days < 7:
		rental *= days
		rental -= 20
		return rental
	elif days >= 0 and days <= 2 :
		rental *= days
		return rental
	else:
		return "Nope."

def trip_cost(city, days, spending_money):
	return rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(days - 1) + spending_money
```

* 7.7
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def hotel_cost(nights):
	return 140 * nights

def plane_ride_cost(city):
	if city == 'Charlotte':
		return 183
	if city == 'Tampa':
		return 220
	if city == 'Pittsburgh':
		return 222
	if city == "Los Angeles":
		return 475
  
def rental_car_cost(days):
	rental = 40
	if days >= 7:
		rental *= days
		rental -= 50
		return rental
	elif days >= 3 and days < 7:
		rental *= days
		rental -= 20
		return rental
	elif days >= 0 and days <= 2 :
		rental *= days
		return rental
	else:
		return "Nope."

def trip_cost(city, days, spending_money):
	return rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(days - 1) + spending_money

print(trip_cost("Los Angeles", 5, 600))
```

## Listas y Diccionarios
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

## Desafío

* 10.1