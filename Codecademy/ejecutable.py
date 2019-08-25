#!/usr/bin/python
# -*- coding: utf-8 -*-

def censor(text, word):
    words = text.split()
    print(words)
    result = ''
    stars = '*' * len(word)
    count = 0
    for match in words:
        if match == word:
            words[count] = stars
        count += 1
    result = ' '.join(words)
    return result
print(censor('lala Opa opa opa', 'opa'))