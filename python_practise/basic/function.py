def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('asdfasdf')
	if x>=0:
		return x
	else:
		return -x


# print(my_abs(-4))

import math
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny

x,y = move(100,100,60,math.pi/6)
# print(x,y)

def power(x, n):
	s = 1
	while n>0:
		n = n-1
		s = s * x
	return s
print(power(6,3))

#定义默认参数要牢记一点：默认参数必须指向不变对象！

def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L
#在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n;
	return sum
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
#在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
#但是，调用该函数时，可以传入任意个参数，包括0个参数



#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
#但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


##利用递归函数移动汉诺塔
def move(n,a,b,c):
	if n==1:
		print('move',a,'--->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)
#move(4,'A','B','C')

P = []
n = 1
while(n<=99):
	P.append(n)
	n = n+2
#print(P)

#slice切片
Q = list(range(100))
#前十个数 ，每两个取一个
#print(Q[:10:2])
#所有数，每5个取一个
#print(Q[::5])

from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,34],Iterable))
print(isinstance(123,Iterable))
#Python内置的enumerate函数可以把一个list变成索引-元素对
for i,value in enumerate(['a','b','c']):
	print(i, value)
#简洁强大的列表生成式
m = [x*x for x in range(1,11)]
print(m)
n = [x*x for x in range(1,11) if x % 2 == 0]
print(n)

#生成全排列
a = [m + n for m in '飞笨呆' for n in '笨燕呆']
print(a)

#import os
#[d for d in os.listdir('.')]

g = (x * x for x in range(10))
for n in g:
	print(n)
#杨辉三角
def triangles():
	L = [1]
	while True:
		yield L
		L = [(L + [0])[i] + ([0] + L)[i] for i in range(len(L) + 1)]
		if(len(L)>10):
			break
print (triangles())
for n in triangles():
	print(n)

#高阶函数
def add(x,y,f):
	return f(x) + f(y)
print(add(-5,56,abs))

K = []
def f(x):
	return x * x
r = map(f,[1,2,3,4,5,6,7,8,9])
for i in r:
	print(i)
