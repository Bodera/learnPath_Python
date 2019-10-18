#!/usr/bin/python
# -*- coding: utf-8 -*-

def flip_bit(number, n):
    bit_to_flip = 0b1 << (n -1)
    result = number ^ bit_to_flip
    return bin(result)

print (flip_bit(0b110101, 2))