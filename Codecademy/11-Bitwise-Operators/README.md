## Introduction to Bitwise Operators

* 17.1
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

#Al final de esta sección, usted tendrá una mejor comprensión de cómo funcionan los operadores bit a bit.

print (5 >> 4)  # Right Shift
print (5 << 1)  # Left Shift
print (8 & 5)   # Bitwise AND
print (9 | 4)   # Bitwise OR
print (12 ^ 42) # Bitwise XOR
print (~88)     # Bitwise NOT
```

* 17.2
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

#En Python, puede escribir números en formato binario iniciando el número con 0b.

print (0b1, end=", ")    #1
print (0b10, end=", ")   #2
print (0b11, end=", ")   #3
print (0b100, end=", ")  #4
print (0b101, end=", ")  #5
print (0b110, end=", ")  #6
print (0b111, end=", ")  #7
print (0b1000, end=", ") #8
print (0b1001)           #9
print ("******")
print (0b1 + 0b11)
print (0b11 * 0b11)
```

* 17.3
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100
```

* 17.4
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# bin() toma un entero como entrada y devuelve la representación binaria de ese entero en una cadena.
# Tenga en cuenta que después de utilizar la función bin(), ya no puede operar en el valor como un número.
# Python también ofrece otras funciones como oct() y hex().

print (bin(1))
print (bin(2))
print (bin(3))
print (bin(4))
print (bin(5))
```

* 17.5
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Cuando se le da una cadena que contiene un número y la base en la que se encuentra ese número,
#  la función int() devolverá el valor de ese número convertido a base diez.

print (int("1",2))
print (int("10",2))
print (int("111",2))
print (int("0b100",2))
print (int(bin(5),2))
# Imprima el equivalente decimal del binario 11001001.
print (int("0b11001001",2))
```

* 17.6
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Left Bit Shift (<<)  
print (0b000001 << 2 == 0b000100) #(1 << 2 = 4)
print (0b000101 << 3 == 0b101000) #(5 << 3 = 40) 

# Right Bit Shift (>>)
print (0b0010100 >> 3 == 0b000010) #(20 >> 3 = 2)
print (0b0000010 >> 2 == 0b000000) #(2 >> 2 = 0)

# El shift es siempre un entero positivo:
# Sólo se pueden realizar operaciones bit a bit en un entero

shift_right = 0b1100 #12
shift_left = 0b1     #1

# ¡Tu código aquí!
shift_right = shift_right >> 2    #3
shift_left = shift_left << 2      #4

print (bin(shift_right))
print ((shift_left))
```

* 17.7
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# La multiplicación binaria
# 0 & 0 = 0
# 0 & 1 = 0
# 1 & 0 = 0
# 1 & 1 = 1
print (0b111 & 0b1010) #0b10

print ("     a:   00101010   42")
print ("     b:   00001111   15")       
print ("===================")
print (" a & b:   00001010   10")

# El operador & solo da como resultado un número que es menor o igual que el menor de los dos valores.

print (bin(0b1110 & 0b101))
```

* 17.8
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# La suma binaria
# 0 | 0 = 0
# 0 | 1 = 1 
# 1 | 0 = 1
# 1 | 1 = 1
print (0b110 | 0b1010) # 0b1110

print ("    a:  00101010  42")
print ("    b:  00001111  15")       
print ("================")
print ("a | b:  00101111  47")

# El operador | solo da como resultado un número que es mayor o igual que el mayor de los dos valores.

print (bin(0b1110 | 0b101))
```

* 17.9
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

# XOR
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0
print (0b111 ^ 0b1010) #0b1101

print ("    a:  00101010   42")
print ("    b:  00001111   15")       
print ("================")
print ("a ^ b:  00100101   37")

# El operador | solo da como resultado un número que es mayor o igual que el mayor de los dos valores.

print (bin(0b1110 ^ 0b101))
```

* 17.10
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

print (~1)
print (~2)
print (~3)
print (~42)
print (~123)
```

* 17.11
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def check_bit4(input):
    mask = 0b1000
    if input & mask > 0:
        return "on"
    else:
        return "off"

print (check_bit4(0b111))
print (check_bit4(0b1111))
```

* 17.12
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def check_bit4(input):
    mask = 0b100
    if input | mask > 0:
        return "on"
    else:
        return "off"

print (check_bit4(0b1011))
print (check_bit4(0b10111011))
```

* 17.13
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

a = 0b11101110

mask = 0b11111111
desired = a ^ mask

print (bin(desired))
```

* 17.14
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def flip_bit(number, n):
    bit_to_flip = 0b1 << (n -1)
    result = number ^ bit_to_flip
    return bin(result)

print (flip_bit(0b110101, 2))
```