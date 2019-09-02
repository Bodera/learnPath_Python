# Listas y Funciones

* 11.1
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

n = [1, 3, 5]

# imprimir el segundo elemento de la lista.
print(n[1])
```

* 11.2
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

n = [1, 3, 5]
# seguir practicando
n[1] = n[1] * 5
print(n)
```

* 11.3
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

n = [1, 3, 5] #Añadir el número 4 aquí

n.append(4)
print(n)
# Esto imprime [1, 3, 5, 4]

n.insert(0,4) #list.insert(índice, item)
print(n)
# Esto imprime [4, 1, 3, 5, 4]
```

* 11.4
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

n = [1, 3, 5]

n.pop(1)
# Devuelve 3 (el elemento del índice 1)
print(n)
# Esto imprime [1, 5]

n.remove(1)
# Elimina 1 de la lista,
# NO el elemento en el índice 1
print(n)
# Esto imprime [3, 5]

del(n[1])
#No devuelve nada
print(n)
# Esto imprime [1, 5]
```

* 11.5
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

n = [1, 3, 5]
# Elimine el primer elemento de la lista aquí
del(n[0])
print(n)
```

* 11.6 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

number = 5

def my_function(x):
	return x + 3

print(my_function(number))
```

* 11.6 después
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

number = 5

def my_function(x):
	return x * 3

print(my_function(number))
```

* 11.7
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

m = 5
n = 13
# ¡Añadir add_function aquí!
def add_function(x, y):
	return x + y

print add_function(m, n)
```

* 11.8
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

n = "Hello"
# ¡Añadir su función aquí!
def string_function(s):
	return s + "world"

print string_function(n)
```

* 11.9
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def list_function(x):
	return x

n = [3, 5, 7]
print(list_function(n))
```

* 11.10
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def list_function(x):
	return x[1]

n = [3, 5, 7]
print(list_function(n))
```

* 11.11
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

#Cuando pasamos una lista a una función y modificamos 
# esa lista terminamos modificando la lista original.

def list_function(x):
	x[1] = x[1] + 3
	return x

n = [3, 5, 7]
print(list_function(n))
```

* 11.12
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

n = [3, 5, 7]
# ¡Añadir su función aquí!

def list_extender(lst):
	lst.append(9)
	return lst
  
print(list_extender(n))
```

* 11.13
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

n = [3, 5, 7]

#for i in range(0, len(n)):
#  print n[i]

def print_list(x):
	for stompillo in range(0, len(x)):
		print x[stompillo]
	
print_list([147, 518, 34])
print_list(["Afortunada", "Bonita", "Correcta", "Dulce"])
print_list(n)
```

* 11.14
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

n = [3, 5, 7]

#for i in range(0, len(n)):
#    n[i] = n[i] * 2

def double_list(x):
	for value in range(len(x)):
		x[value] = x[value] * 2
	return x
	
print double_list(n)
```

* 11.15
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
range(6) # => [0, 1, 2, 3, 4, 5]
range(1, 6) # => [1, 2, 3, 4, 5]
range(1, 6, 3) # => [1, 4]

    range(stop)
    range(start, stop)
    range(start, stop, step)

En todos los casos, la función range() devuelve 
 una lista de números desde el inicio hasta
 la parada (pero sin incluir).
Cada elemento aumenta paso a paso.

Si se omite, el valor predeterminado de start 
 es 0 y el valor predeterminado del step es 1.
"""

def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print(my_function(range(3)))
```

* 11.16
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Método 1 - for item in list:
for item in list:
  print item

Método 2 - iterar a través de índices:
for i in range(len(list)):
  print list[i]
  
El método 1 es útil para recorrer la lista, pero
 no es posible modificar la lista de esta manera.

El método 2 utiliza índices para recorrer la lista,
 lo que permite modificar también la lista si es necesario.  
"""

n = [3, 5, 7]

def total(numbers):
	result = 0
	for trompillo in range(len(numbers)):
		result += (numbers[trompillo])
	return result

print(total(n))
```

* 11.17
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
	result = ""
	for string in words:
		result += string + ""
	return result

print join_strings(n)
```

* 11.18
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
a = [1, 2, 3]
b = [4, 5, 6]
print a + b
# Esto imprime [1, 2, 3, 4, 5, 6]
Este ejemplo es solo un recordatorio de cómo concatenar dos listas.
"""

m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x, y):
	return x+y

print join_lists(m, n)
```

* 11.19
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
list_of_lists = [[1, 2, 3], [4, 5, 6]]

for lst in list_of_lists:
  for item in lst:
    print item

Resultado:
1
2
3
4
5
6
"""

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# ¡Añade tu código a continuación!

def flatten(lists):
	results = []
	for numbers in lists:
		for number in numbers:
			results.append(number)
	return results

print flatten(n)
```
