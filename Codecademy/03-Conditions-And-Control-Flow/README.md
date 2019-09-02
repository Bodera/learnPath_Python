# Condiciones y flujo de control
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

print (using_control_once())
print (using_control_again())
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

print (using_control_once())
print (using_control_again())
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
        
print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))

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
        
print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))

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
print (grade_converter(92))

# Esto debería imprimir un "C"
print (grade_converter(70))

# Esto debería imprimir un "F"
print (grade_converter(61))
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
