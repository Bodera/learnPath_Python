# Learn Python 2 [crash Codecademy](https://www.codecademy.com/learn/learn-python)

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
