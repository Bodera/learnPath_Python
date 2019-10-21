# Proving your abilities

* 19.1
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""entrada y salida de archivos"""
my_list = [i ** 2 for i in range(1, 11)]
# Genera una lista de cuadrados de los números del 1 al 10.

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()
```

Ese pedazo de código `f = open("output.txt", "w")` indica a Python que abra un archivo de texto llamado output en modo de escritura (la `w` significa write). Entonces, al concluir la operación, el resultado se almacena en un objeto de archivo llamado `f`.

* 19.2
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
my_file = open("output.txt", "r+")
```

Puede abrir archivos en cualquiera de los siguientes modos:

1. modo de solo escritura ("w")
2. modo de solo lectura ("r")
3. modo de lectura y escritura ("r +")
4. modo anexar ("a"), que agrega cualquier dato nuevo que escriba al archivo al final del archivo.

* 19.3
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

for x in my_list:
  my_file.write(str(x) + "\n")

my_file.close()
```

* 19.4
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
my_file = open("output.txt", "r")

print(my_file.read())

my_file.close()
```

* 19.5
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
my_file = open("output.txt", "r")

print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

my_file.close()
```

Durante el proceso de E/S, los datos se almacenan en el búfer: esto significa que se guardan en una ubicación temporal antes de escribirse en el archivo.

Python no vacía el búfer, es decir, escribe datos en el archivo, hasta que esté seguro de que ha terminado de escribir. Una forma de hacerlo es cerrar el archivo. Si escribe en un archivo sin cerrar, los datos no llegarán al archivo de destino.

* 19.6
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""entrada y salida de archivos"""
# Use a file handler to open a file for writing
write_file = open("output.txt", "w")
# Open the file for reading
read_file = open("output.txt", "r")
# Write to the file
write_file.write("Not closing files is VERY BAD.")
write_file.close()
# Try to read from the file
print(read_file.read())
read_file.close()
```

Puede que no lo sepas, pero los objetos de archivo contienen un par especial de métodos integrados: `__enter __()` y `__exit __()`. Los detalles no son importantes, pero lo importante es que cuando se invoca el método `__exit __()` de un objeto de archivo, cierra automáticamente el archivo. ¿Cómo invocamos este método? Con `with .. as`.

* 19.7
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""with .. as code block"""
with open("text.txt", "w") as textfile:
  textfile.write("Success!")
```

* 19.8
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
with open("text.txt", "w") as my_file:
  my_file.write("No confundas lo verdadero con lo falso, ni escondas la verdad tal como la conoces.")
```

* 19.9
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
with open("text.txt", "w") as my_file:
  my_file.write("No confundas lo verdadero con lo falso, ni escondas la verdad tal como la conoces.")

if(my_file.closed == False):
  my_file.close()
  
print(my_file.closed)
```