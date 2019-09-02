#!/usr/bin/python
# -*- coding: utf-8 -*-

address = ["Flat Floor Street", "18", "New York"]
pins = { "Mike": 1123, "Jow": 4468, "Jack Tequila": 0}

print(address[0], address[1])

pin = int(input("Enter your pin: "))

def find_in_file(f):
	myFile = open("sample.txt", "r")
	fruits = myFile.read()
	#fruits = fruits.splitlines()
	if f in fruits:
		return "That fruit is in the list."
	else:
		return "No such fruit found!"

if pin in pins.values():
	fruit = input("Enter a fruit: ")
	print(find_in_file(fruit))
else:
	print("Incorrect pin.")
	print("This info can only be accessed by: ")
	for key in pins.keys():
		print(key)
