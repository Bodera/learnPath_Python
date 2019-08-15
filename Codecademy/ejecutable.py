#!/usr/bin/python
# -*- coding: utf-8 -*-

#Cree su propia declaración for/else desde cero

from time import perf_counter 

time_start = perf_counter()

personas = ["Benjamín", "Maite", "Gaspar", "Elena", "Mabel"]
edad = [27, 52, 18, 34, 40]
sexo = ["Hombre", "Mujer", "Hombre", "Mujer", "Periodista"]

mas_viejo = max(edad)

for a, b, c in zip(personas, edad, sexo):
    if (c == 'Mujer'):
        print(a, "tiene", b, "años y es una", c)
    elif (c == 'Hombre'):
        print(a, "tiene", b, "años y es un", c)
    else:
        print(a, "tiene", b, "años pero no sé lo qué es", c)
else:
    for a, b, c in zip(personas, edad, sexo):
        if (b == mas_viejo):
            print(a, "es la persona más vieja.")

time_stop = perf_counter()

print("Elapsed time:", time_stop - time_start)