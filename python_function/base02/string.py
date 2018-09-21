#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther:Awe H

name = "my name IS alex"
'''
print(1,name.capitalize())
print(2,name.count('a'))
print(3,name.casefold())
print(name.center(50,'-'))
print(name.endswith('ex'))
print(name.expandtabs(tabsize=30))
print(name[name.find('name'):])
print(4,name.format(name='alex',year=23))
print(name.isalnum())
print(name.isalpha())
print(name.isdecimal())
print(name.isdigit())
print(name.isidentifier()) #判断是不是一个合法的标识符
print(name.islower())
print(name.isnumeric())
print(name.isspace())
print(name.istitle())
print(name.isprintable())
print(name.isupper())
'''
print('myNameis'.join('=='))
print('abc'.join(['1','2','3']))
print(name.ljust(50,'&'))
print(name.rjust(50,'#'))
print('ALEX'.lower())
print('alex'.upper())
#print('Alex\n'.strip())
#print('Alex\n'.lstrip())
print('Alex\n'.rstrip())
print('-------')
p = str.maketrans('abcdef','123456')

print('alex li'.translate(p))
print('#############')
print('alex li'.replace('l','L',1))
print('alex li'.rfind('e'))
print('1+2+3+4'.split('+'))
print('1+2\n+3+5'.splitlines())
print('Alex Li'.swapcase())
print('Alex Li'.title())
print('alex li'.zfill(50))
