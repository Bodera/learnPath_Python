#!/usr/bin/python
# -*- coding: utf-8 -*-

my_list = range(16)
#print (filter(lambda x: x % 3 == 0, my_list))

def by_three(x):
  return x % 3 == 0
by_three(my_list)