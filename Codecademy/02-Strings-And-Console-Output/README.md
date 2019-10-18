# Cadenas

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

print (caesar)
print (praline)
print (viking)
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

print (caesar)
print (praline)
print (viking)
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

print (fifth_letter)
```

* 2.5
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

parrot = "Norwegian Blue"
print (len(parrot)) # Comience a contar desde 1. Los espacios en blanco también cuentan.
```

* 2.6
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

parrot = "Norwegian Blue"
print (parrot.lower()) #Or "Norwegian Blue".lower()
```

* 2.7
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

parrot = "Norwegian Blue"
print (parrot.upper())
```

* 2.8
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

pi = 3.14159265359
print (str(pi))
```

* 2.9
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

ministry = "The Ministry of Silly Walks"

print (len(ministry))
print (ministry.upper())
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
