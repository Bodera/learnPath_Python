#!/usr/bin/python
# -*- coding: utf-8 -*-
"""recapitulando"""
class Point3D(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return F"({self.x}, {self.y}, {self.z})"

my_point = Point3D(2, 4, 6)
print(my_point)
print(my_point.__repr__())