dl211@soetcse:~$ python
Python 2.7.15rc1 (default, Nov 12 2018, 14:31:15) 
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> a="Hella all"
>>> print a
Hella all
>>> a="hello all"
>>> print()
()
>>> print(a)
hello all
>>> print(a[3])
l
>>> print([2:8])
  File "<stdin>", line 1
    print([2:8])
            ^
SyntaxError: invalid syntax
>>> print([2;8])
  File "<stdin>", line 1
    print([2;8])
            ^
SyntaxError: invalid syntax
>>> python3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python3' is not defined
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
dl211@soetcse:~$ python3
Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a="hello all"
>>> print(a)
hello all
>>> print([2])
[2]
>>> print(a[4])
o
>>> print(a.lower())
hello all
>>> print(a.upper())
HELLO ALL
>>> print(a.strip())
hello all
>>> b="Hello, all"
>>> print(b.strip(","))
Hello, all
>>> a="hello"
>>> a*3
'hellohellohello'
>>> a+b
'helloHello, all'
>>> c="CSE"
>>> print(c.replace("c","I"))
CSE
>>> print(c.replace("C","I"))
ISE
>>> len(c)
3
>>> a="  Hello"
>>> print(a.strip())
Hello
>>> d="Hello,world,how r u"
>>> print(d.split(","))
['Hello', 'world', 'how r u']

