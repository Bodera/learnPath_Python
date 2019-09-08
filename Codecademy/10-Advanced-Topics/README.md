# Advanced topics in Python

## Dictionaries

* 16.1
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

my_dict = {
    "2:134": "Essa é uma nação que já passou. A ela o que logrou, e a vós, o que lograstes, e não sereis interrogados acerca do que faziam.",
    "7:205": "E invoca teu Senhor, em ti mesmo, humilde e temerosamente, e sem altear a voz, ao amanhecer e ao entardecer, e não sejas dos desatentos.",
    "1:6": "Guia-nos à senda reta,"
}
```

* 16.2
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

my_dict = {
    "2:134": "Essa é uma nação que já passou. A ela o que logrou, e a vós, o que lograstes, e não sereis interrogados acerca do que faziam.",
    "7:205": "E invoca teu Senhor, em ti mesmo, humilde e temerosamente, e sem altear a voz, ao amanhecer e ao entardecer, e não sejas dos desatentos.",
    "1:6": "Guia-nos à senda reta,"
}

print (my_dict.items()) # a tuple
print (my_dict.keys()) # only keys
print (my_dict.values()) # only values
```

* 16.3
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

my_dict = {
    "2:134": "Essa é uma nação que já passou. A ela o que logrou, e a vós, o que lograstes, e não sereis interrogados acerca do que faziam.",
    "7:205": "E invoca teu Senhor, em ti mesmo, humilde e temerosamente, e sem altear a voz, ao amanhecer e ao entardecer, e não sejas dos desatentos.",
    "1:6": "Guia-nos à senda reta,"
}

for key in my_dict:
    print (key,my_dict[key])
```

## List comprehension

* 16.4
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

my_list = list(range(51)) #range(0,51,1)
print (my_list)

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print (evens_to_50)
```

* 16.5
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Completa la siguiente línea. Use la línea de arriba para obtener ayuda.
even_squares = [x * x for x in range (1,11) if (x * x) % 2 == 0]

print (even_squares)
```

* 16.6
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Esto es para tu conocimiento
c = ['C' for x in range(5) if x < 4]
print (c)

# Esto si de verdad
cubes_by_four = [pow(x,3) for x in range(1,11) if pow(x,3) % 4 == 0]
print (cubes_by_four)
```

## List slicing

* 16.7
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

my_list = [i ** 2 for i in range(1, 11)] #range(1,11) es de 1 a 10.
# Deberia ser [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print (my_list[2:9:2]) 
# Comenzamos en el elemento 2 de nuestra lista (inclusivo), hasta llegar al elemento 9 en él (exclusivo). Por cada 2 elementos lo agregamos a una lista nueva.
# Deberia ser [9, 25, 49, 81]
```

* 16.8
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

my_list = list(range(1, 11)) # Lista de números del 1 al 10

# Al rebanar listas debes recordar
# El índice inicial predeterminado es 0.
# El índice final predeterminado es el final de la lista.
# El paso predeterminado es 1.

# ¡Agregue su código a continuación!
print (my_list[::2])
```

## Reversing a List

* 16.9
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

my_list = list(range(1, 11)) 
reversed_odds = (my_list[8::-2])
print (reversed_odds)
```

* 16.10
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

to_one_hundred = list(range(101))
backwards_by_tens = to_one_hundred[::-10]
print (backwards_by_tens)
```

* 16.11
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

to_21 = list(range(1,22))

#odds = [x for x in to_21 if x % 2 != 0]
odds = to_21[::2]

middle_third = to_21[7:14:1]

print (to_21)
print (odds)
print (middle_third)
```

## Functional programming, *lambda*, and anonymous functions

* 16.12
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
```