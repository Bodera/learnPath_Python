#!/usr/bin/python
# -*- coding: utf-8 -*-

def hotel_cost(nights):
	return 140 * nights

def plane_ride_cost(city):
	if city == 'Charlotte':
		return 183
	if city == 'Tampa':
		return 220
	if city == 'Pittsburgh':
		return 222
	if city == "Los Angeles":
		return 475
  
def rental_car_cost(days):
	rental = 40
	if days >= 7:
		rental *= days
		rental -= 50
		return rental
	elif days >= 3 and days < 7:
		rental *= days
		rental -= 20
		return rental
	elif days >= 0 and days <= 2 :
		rental *= days
		return rental
	else:
		return "Nope."

def trip_cost(city, days, spending_money):
	return rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(days - 1) + spending_money

print(trip_cost("Los Angeles", 5, 600))
