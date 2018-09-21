class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1

	def __iter__(self):
		return self

	def __next__(self):
		self.a,self.b = self.b,self.a + self.b
		if self.a > 10000:
			raise StopIteration()
		return self.a

#for n in Fib():
#	print(n)

class Fibs(object):
	def __getitem__(self,n):
		a,b=1,1
		for x in range(n):
			a,b = b,a+b
		return a
f=Fibs()
print(f[0],f[1],f[2])

class Fibes(object):
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a
		if isinstance(n,slice):
			start = n.start
			end = n.end
			if start is None:
				start = 0
			a,b = 1,1
			L = []
			for x in range(stop):
				if x>=start:
					L.append(a)
				a,b = b, a+b
			return L

class Chain(object):
	def __init__(self,path=''):
		self._path = path
	def __getattr__(self,path):
		return Chain('%s\%s' % (self._path,path))
	def __str__(self):
		return self._path
	
	__repr__ = __str__

print(Chain().status.user.timeline.list)
