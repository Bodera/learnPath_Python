# Introduction to classes
Python es un lenguaje de programación orientado a objetos, lo que significa que manipula construcciones de programación llamadas objetos. Puede pensar en un objeto como una estructura de datos única que contiene datos y funciones; Las funciones de un objeto se denominan sus métodos. Por ejemplo, cada vez que llama a `len("Juan")` Python está verificando si el objeto de cadena que pasó tiene una longitud y, si lo tiene, devuelve el valor asociado con ese atributo.

Cuando llama a `my_dict.items()` Python comprueba si `my_dict` tiene un método` items()` (que tienen todos los diccionarios) y ejecuta ese método si lo encuentra.

Pero, ¿qué hace que `"Juan"` sea una cadena y `my_dict` un diccionario? El hecho de que son instancias de las clases str y dict, respectivamente. Una clase es solo una forma de organizar y producir objetos con atributos y métodos similares.

* 18.1
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Fruit(object):
    """Una clase que hace varias frutas sabrosas."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print(f"I'm a {self.color} {self.name} and I taste {self.flavor}.")

    def is_edible(self):
        if not self.poisonous:
            print("Yep! I'm edible.")
        else:
            print("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()
```

Una clase básica consta solo de la palabra clave de clase, el nombre de la clase y la clase de la cual la nueva clase __hereda__ entre paréntesis. (Pronto llegaremos a la herencia). Por ahora, nuestras clases heredarán de la clase de `object`, así:

```python
class NewClass(objeto):
  # Magia de clase aquí
```

Esto les da los poderes y habilidades de un objeto Python. Por convención, los nombres de clase Python definidos por el usuario comienzan con una letra mayúscula.

* 18.2
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Animal(object):
    pass
```

Queremos que nuestras clases hagan más que ... bueno, nada, así que tendremos que reemplazar nuestro `pass` con algo más.

Puede haber notado en nuestro ejemplo en el primer ejercicio que comenzamos nuestra definición de clase con una función de aspecto extraño: `__init__()`. Esta función es necesaria para las clases y se usa para inicializar los objetos que crea. `__init__()` siempre toma al menos un argumento, `self`, que se refiere al objeto que se está creando. Puede pensar en `__init__()` como la función que "inicia" cada objeto que crea la clase.

* 18.3
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Animal(object):
    def __init__(self):
        pass
```
Hagamos un ajuste más a nuestra definición de clase, luego avancemos e instanciaremos (creemos) nuestro primer objeto.

La parte mágica es el hecho de que self es el primer parámetro pasado a `__init__()`. Python usará el primer parámetro que `__init__()` recibe para referirse al objeto que se está creando; Es por eso que a menudo se llama `self`, ya que este parámetro le da al objeto que está siendo creado su identidad.

* 18.4
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Animal(object):
    def __init__(self,name):
        self.name = name
```

Mira este código

```python
class Square(object):
  def __init__(self):
    self.sides = 4

my_shape = Square()
print (my_shape.sides)
```

Primero creamos una clase llamada `Square` con un atributo `sides`.
Fuera de la definición de clase, creamos una nueva __instancia__ de `Square` llamada `my_shape` y accedemos a ese atributo usando `my_shape.sides`.

* 18.5
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Animal(object):
    def __init__(self,name):
        self.name = name

zebra = Animal("Osvaldo")
print(zebra.name)
```

El primer argumento que obtiene `__init__()` se usa para referirse al objeto de instancia, y por convención, ese argumento se llama `self`. Si agrega argumentos adicionales, por ejemplo, un nombre y edad para su animal, establecer cada uno de esos iguales a `self.name` y `self.age` en el cuerpo de `__init__()` lo hará de modo que cuando cree un objeto de instancia de su Clase animal, debe asignar a cada instancia un nombre y una edad, y se asociarán con la instancia particular que cree.

* 18.6
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Class definition
class Animal(object):
  """Makes cute animals."""
  # For initializing our instance objects
  def __init__(self, name, age, is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print (zebra.name, zebra.age, zebra.is_hungry)
print (giraffe.name, giraffe.age, giraffe.is_hungry)
print (panda.name, panda.age, panda.is_hungry)
```

Otro aspecto importante de las clases de Python es el `alcance` o `scope`. El `alcance` de una variable es el contexto en el que es visible para el programa.

Puede sorprenderle saber que no todas las variables son accesibles a todas las partes de un programa Python en todo momento. Cuando se trata de clases, puede tener variables que están disponibles en todas partes (variables globales), variables que solo están disponibles para miembros de una determinada clase (variables miembro) y variables que solo están disponibles para instancias particulares de una clase (variables de instancia).

Lo mismo ocurre con las funciones: algunas están disponibles en todas partes, algunas solo están disponibles para miembros de una determinada clase y otras solo están disponibles para objetos de instancia particulares.

* 18.7
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Tenga en cuenta que cada animal individual tiene su propio nombre y edad (ya que todos se inicializan individualmente), pero todos tienen acceso a la variable miembro is_alive, ya que todos son miembros de la clase Animal.
"""

class Animal(object):
    """Hace animales lindos."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

zebra = Animal("Cebra", 2)
giraffe = Animal("Jirafa", 1)
panda = Animal("Oso panda", 7)

print (zebra.name, zebra.age, zebra.is_alive)
print (giraffe.name, giraffe.age, giraffe.is_alive)
print (panda.name, panda.age, panda.is_alive)
```

* 18.8
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #¡Agrega tu método aquí!
    def description(self):
        print(self.name)
        print(self.age)

hippo = Animal("Olga", 12)
hippo.description()
```

* 18.9
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #¡Agrega tu método aquí!
    def description(self):
        print(self.name)
        print(self.age)

hippo = Animal("Olga", 12)
sloth = Animal("Ortiz", 8)
ocelot = Animal("Helena", 6)

print(hippo.health)
print(sloth.health)
print(ocelot.health)
```

* 18.10
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items_in_cart = {}
    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print (product + " added.")
        else:
            print (product + " is already in the cart.")

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print (product + " removed.")
        else:
            print (product + " is not in the cart.")

my_cart = ShoppingCart("Bodera")
my_cart.add_item("Tamborim", 23)
my_cart.add_item("Ice cream", 5)
my_cart.add_item("Broche", 102)
```

La __herencia__ es el proceso mediante el cual una clase adquiere los atributos y métodos de otra, y se utiliza para expresar una relación `es-una`. Por ejemplo, un panda es un oso, por lo que una clase Panda podría heredar de una clase Bear. Sin embargo, un Toyota no es un Tractor, por lo que no debería heredar de la clase Tractor (incluso si tienen muchos atributos y métodos en común). En cambio, tanto Toyota como Tractor podrían finalmente heredar de la misma clase de Vehículo.

* 18.11
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Hemos definido una clase, Cliente, así como una clase de Devolución de Cliente que hereda del Cliente. Tenga en cuenta que no definimos el método display_cart en el cuerpo de ReturningCustomer, pero aún tendrá acceso a ese método a través de la herencia.
"""

class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print ("I'm a string that stands in for the contents of your shopping cart!")

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print ("I'm a string that stands in for your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print ("I'm a string that stands in for the contents of your shopping cart!")

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print ("I'm a string that stands in for your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()
```

En Python, la herencia funciona así:

```python
clase DerivedClass (BaseClass):
  # código va aquí
```

donde `DerivedClass` es la nueva clase que está creando y `BaseClass` es la clase de la que hereda esa nueva clase.

* 18.12
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Shape(object):
  """Hace formas!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

# ¡Agregue su clase de triángulo a continuación!
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
```

Algunas veces querrás que una clase que hereda de otra no solo tome los métodos y atributos de su padre, sino que __anule__ uno o más de ellos.

```python
class Employee(object):
  def __init__(self, name):
    self.name = name
  def greet(self, other):
    print (f"Hello, {other.name}")

class CEO(Employee):
  def greet(self, other):
    print (f"Get back to work, {other.name}!")

ceo = CEO("Emily")
emp = Employee("Steve")

emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!
```

En lugar de tener un método separado `greet_underling` para nuestro CEO, anulamos (o recreamos) el método `greet` encima del método base `Employee.greet`. De esta manera, no necesitamos saber qué tipo de empleado tenemos antes de saludar a otro empleado.

* 18.13
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Employee(object):
  """¡Modelos de empleados de la vida real!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# ¡Agregue su código a continuación!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        #porque anulamos el método, aún necesitamos establecerlo
        self.hours = hours
        return hours * 12.00
```

Por otro lado, a veces trabajará con una clase derivada (o subclase) y se dará cuenta de que ha sobrescrito un método o atributo definido en la clase base de esa clase (también llamada padre o superclase) que realmente necesita. ¡No tener miedo! Puede acceder directamente a los atributos o métodos de una superclase con la `super` llamada incorporada de Python.

The syntax looks like this:

```python
class Derived(Base):
  def m(self):
    return super(Derived, self).m()
```
Where `m()` is a method from the base class.

* 18.14
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Employee(object):
  """¡Modelos de empleados de la vida real!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# ¡Agregue su código a continuación!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        #porque anulamos el método, aún necesitamos establecerlo
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee("Milton")

print(milton.full_time_wage(10))
```

* 18.15
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
```

* 18.16
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    
    number_of_sides = 3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False
```

* 18.17
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    
    number_of_sides = 3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False

my_triangle = Triangle(60, 60, 60)
print(my_triangle.check_angles())
print(my_triangle.number_of_sides)
```

* 18.18
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    
    number_of_sides = 3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False

my_triangle = Triangle(60, 60, 60)
print(my_triangle.check_angles())
print(my_triangle.number_of_sides)

class Equilateral(Triangle):
    angle = 60

    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle
```