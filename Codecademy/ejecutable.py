#!/usr/bin/python
# -*- coding: utf-8 -*-

#Thanks to Er CEO Vora Mayur
#https://stackoverflow.com/questions/45003783/how-do-i-find-the-median-of-a-list-in-python
def median(user_list):
    ordered_list = sorted(user_list)
    if len(ordered_list) % 2 == 1:
        return ordered_list[(len(ordered_list)+1)//2-1]
    else:
        lower = ordered_list[(len(ordered_list)+1)//2-1]
        upper = ordered_list[(len(ordered_list)+1)//2]
        print(lower, upper)
        return (lower+upper) / 2.0 
        #return float(lower+upper) / 2
print (median([1,2,3,4,5,6,7,8,9,10]))