#!/usr/bin/python
# -*- coding: utf-8 -*-

def tax(bill):
	"""Agrega un 8% de impuestos a la factura de un restaurante."""
	bill *= 1.08
	print("Con impuestos: %.2f") % bill
	return bill

def tip(bill):
	"""Agrega un 15% de propina a la factura de un restaurante."""
	bill *= 1.15
	print("Con propina:  %.2f") % bill
	return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)
