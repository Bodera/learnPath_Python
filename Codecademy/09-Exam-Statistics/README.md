* 15.1
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

print("Grades:", grades)
```

* 15.2
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print (grade)

print_grades(grades)
```

* 15.3
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

print ("¡Vamos a calcular algunas estadísticas!")
```

* 15.4
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total = 0
    for grade in scores:
        total += grade
    return total

print (grades_sum(grades))
```

* 15.5
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total = 0
    for grade in scores:
        total += grade
    return total

def grades_average(grades_input):
    total = grades_sum(grades_input)
    average = total / len(grades_input)
    return average

print (round(grades_average(grades),2))
```

* 15.6
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
print("¡Hora de conquistar la varianza!")
```

* 15.7
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total = 0
    for grade in scores:
        total += grade
    return total

def grades_average(grades_input):
    total = grades_sum(grades_input)
    average = total / len(grades_input)
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    variance /= len(scores)
    return variance

print (round(grades_variance(grades),2))
```

* 15.8
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total = 0
    for grade in scores:
        total += grade
    return total

def grades_average(grades_input):
    total = grades_sum(grades_input)
    average = total / len(grades_input)
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    variance /= len(scores)
    return variance

def grades_std_deviation(variance):
    return variance ** 0.5

print (round(grades_std_deviation(grades_variance(grades)),2))
```

* 15.9
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print (grade)

def grades_sum(scores):
    total = 0
    for grade in scores:
        total += grade
    return total

def grades_average(grades_input):
    total = grades_sum(grades_input)
    average = total / len(grades_input)
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    variance /= len(scores)
    return variance

def grades_std_deviation(variance):
    return variance ** 0.5

print_grades(grades)
print()
print (grades_sum(grades))
print()
print (grades_average(grades))
print()
print (grades_variance(grades))
print()
print (grades_std_deviation(grades_variance(grades)))
```