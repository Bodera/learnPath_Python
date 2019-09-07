## Advanced topics in Python

* 16.1
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

my_dict = {
    "2:134": "Essa é uma nação que já passou. A ela o que logrou, e a vós, o que lograstes, e não sereis interrogados acerca do que faziam.",
    "7:205": "E invoca teu Senhor, em ti mesmo, humilde e temerosamente, e sem altear a voz, ao amanhecer e ao entardecer, e não sejas dos desatentos.",
    "1:6": "Guia-nos à senda reta,"
}
```

* 16.2
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

my_dict = {
    "2:134": "Essa é uma nação que já passou. A ela o que logrou, e a vós, o que lograstes, e não sereis interrogados acerca do que faziam.",
    "7:205": "E invoca teu Senhor, em ti mesmo, humilde e temerosamente, e sem altear a voz, ao amanhecer e ao entardecer, e não sejas dos desatentos.",
    "1:6": "Guia-nos à senda reta,"
}

print (my_dict.items()) # a tuple
print (my_dict.keys()) # only keys
print (my_dict.values()) # only values
```

* 16.3
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

my_dict = {
    "2:134": "Essa é uma nação que já passou. A ela o que logrou, e a vós, o que lograstes, e não sereis interrogados acerca do que faziam.",
    "7:205": "E invoca teu Senhor, em ti mesmo, humilde e temerosamente, e sem altear a voz, ao amanhecer e ao entardecer, e não sejas dos desatentos.",
    "1:6": "Guia-nos à senda reta,"
}

for key in my_dict:
    print (key,my_dict[key])
```

* 16.4
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

my_list = list(range(51)) #range(0,51,1)
print (my_list)

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print (evens_to_50)
```

* 16.5
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

```