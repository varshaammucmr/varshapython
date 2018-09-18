Python 2.7.15rc1 (default, Apr 15 2018, 21:51:34) 
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> a=24
>>> b=23
>>> c=12
>>> a>b and A>c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'A' is not defined
>>> a>b and a>c
True
>>> python 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python' is not defined
>>> a=67
>>> b=56
>>> c=45
>>> a.b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'b'
>>> a>b
True
>>> b>c
True
>>> a>c
True

