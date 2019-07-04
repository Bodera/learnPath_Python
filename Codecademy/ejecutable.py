#!/usr/bin/python
# -*- coding: utf-8 -*-

shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pea": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pea": 3
}

# ¡Añade tu código a continuación!
def compute_bill(food):
	total = 0
	for item in food:
		if stock[item] > 0:
			total += prices[item]
			stock[item] -= 1
	return total
	
print(compute_bill(["banana", "orange", "apple", "pea"]))