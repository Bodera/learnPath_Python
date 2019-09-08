#!/usr/bin/python
# -*- coding: utf-8 -*-

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = ''.join(filter(lambda x: x != 'X', garbled))
print (message)