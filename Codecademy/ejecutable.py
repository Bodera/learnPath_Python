#!/usr/bin/python
# -*- coding: utf-8 -*-

def distance_from_zero(arg):
	if(type(arg) ==  int or type(arg) == float):
		return abs(arg)
	else:
		return 'Nope'
