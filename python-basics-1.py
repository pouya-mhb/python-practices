Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 2
>>> b = 3
>>> a >b
False
>>> a + b
5
>>> type(a)
<class 'int'>
>>> c = '12'
>>> a + c
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a + c
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(a) + c
'212'
>>> print (d=str(a)+c)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print (d=str(a)+c)
TypeError: 'd' is an invalid keyword argument for print()
>>> d=str(a)+c
>>> print(d)
212
>>> print (d, end=' ')
212 
>>> '''
Python Basics :

* Python Key Words
* Python Data Types
* Python Identifiers
* Python Opreators

'''
'\nPython Basics :\n\n* Python Key Words\n* Python Data Types\n* Python Identifiers\n* Python Opreators\n\n'
>>> print('hello world')
hello world
>>> print('helloworld')
helloworld
>>> print('hello\nworld')
hello
world
>>> print('hello-tworld')
hello-tworld
>>> print('hello\tworld')
hello	world
>>> print('helloworld', sep='*')
helloworld
>>> print('hello world','this is a start', sep='*')
hello world*this is a start
>>> print ("{} - {} - {}".format(a,b,c))
2 - 3 - 12
>>> print ("{} - {} - {}".format(a,b,c,d))
2 - 3 - 12
>>> print ("{} - {} - {} and {}".format(a,b,c))
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print ("{} - {} - {} and {}".format(a,b,c))
IndexError: Replacement index 3 out of range for positional args tuple
>>> print ("{} - {} - {} and {}".format(a,b,c,d))
2 - 3 - 12 and 212
>>> print(f"{a},{b},{d}")
2,3,212
>>> e = input ("enter a number : ")
enter a number : 9
>>> e
'9'
>>> type(e)
<class 'str'>
>>> f = int(input())
10
>>> f
10
>>> type(f)
<class 'int'>
>>> 