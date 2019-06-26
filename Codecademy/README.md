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
```

* 4.2
```python

```

* 4.3
```python

```

* 4.4
```python

```

* 4.5
```python

```

* 4.6
```python

```

* 4.7
```python

```

* 4.8
```python

```

* 4.9
```python

```

* 4.10
```python

```

* 4.11
```python

```

* 4.12
```python

```

* 4.13
```python

```

* 4.14
```python

```

* 4.15
```python

```
