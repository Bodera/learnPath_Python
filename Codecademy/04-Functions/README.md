# Funciones
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
