#!/usr/bin/python
# -*- coding: utf-8 -*-

def clinic():
    print "¡Acabas de entrar a la clínica!"
    print "¿Tomas la puerta de la izquierda o de la derecha?"
    answer = raw_input("Escriba izquierda o derecha y presione 'Enter'.").lower()
    if answer == "izquierda" or answer == "i":
        print "Esta es la Sala de Abuso Verbal, ¡montón de excrementos de loros!"
    elif answer == "derecha" or answer == "d":
        print ("Por supuesto, esta es la Sala de Argumentos, ¡ya te lo dije!")
    else:
        print ("¡No elegiste izquierda o derecha! Inténtalo de nuevo.")
        clinic()

clinic()
