#!/usr/bin/python
# -*- coding: utf-8 -*-
"""comprobando si cerramos el archivo"""
with open("text.txt", "w") as my_file:
  my_file.write("No confundas lo verdadero con lo falso, ni escondas la verdad tal como la conoces.")

if(my_file.closed == False):
  my_file.close()
  
print(my_file.closed)