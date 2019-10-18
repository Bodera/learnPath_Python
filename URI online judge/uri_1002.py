#Autor> Rafael, el 18 de Enero de 2019.
"""
Á R E A   D E L   C Í R C U L O

La fórmula para calcular el área de un círculo se define como:
 area = pi . radio². Para este problema consideramos pi = 3.14159.
Calcule el área usando la fórmula dada en la descripción del problema.

Entrada:
La entrada consiste de un valor de punto flotante (doble precisión),
 que es la variable radio.
100.64

Salida:
Mostrar el mensaje "A=" seguido del valor del área, como en los ejemplos, con cuatro lugares después del punto decimal. Use variables de doble precisión.
A=31819.3103

No se olvida de saltar a línea después del final del programa.
"""
#Python does not have constants 
CONST_PI = 3.14159
#Declarando las variables.
radio = float(input())
radio *= radio
area = radio * CONST_PI
#Podemos convertir el tipo de variable sólo pasando el valor de entrada, como argumento del método.

print("A=""{0:.4f}".format(area))