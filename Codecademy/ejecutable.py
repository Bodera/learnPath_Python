#!/usr/bin/python
# -*- coding: utf-8 -*-

phrase = "A bird in the hand..."

#Agregue su bucle for
for char in phrase:
    if char == "A" or char == "a":
        print ("X", end="")
    else:
    	print (char, end="")
#¡No elimine esta declaración print!
print()