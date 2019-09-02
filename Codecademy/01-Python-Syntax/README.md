# Sintaxis
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

print ("Hola " + 'el macho cabrío')
```

* 1.4 delante
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

print("How do you make a hot dog stand?")
print("You take away its chair!")
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

# float2 = 10. # 10.0
# float4 = 1.5e2 # 150
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
También se puede usar como un comentario de varias líneas.
"""
```

* 1.12
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hola Soy María y vivo en script.py.
# Soy una codificadora experto de Python.
# Tengo 21 años y planeo programar cosas geniales para siempre.

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
