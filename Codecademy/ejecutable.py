#!/usr/bin/python
# -*- coding: utf-8 -*-

#Diccionario con información de precios
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pea": 3
}

#Diccionario con información sobre stock
stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pea": 15
}

#Imprime el nombre del producto, su precio y cantidad en stock
# en orden alfabético
for key in sorted(prices):
	print("%s price: %s stock: %s" % (key, prices[key], stock[key]))

#Imprime el precio de stock de cada producto y suma el total acumulado
total = 0
for k, v in sorted(prices.items()):
	for values in (sorted(stock)):
		value =  * float(values)
	print(k, value)
	total += value
print("Total: %s" % total)