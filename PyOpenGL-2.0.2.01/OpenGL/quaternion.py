import math, types

try:
	import Numeric
	NUMERIC = 1
except ImportError:
	NUMERIC = 0
	

class quaternion:

	def __init__(self, a = 0.0, b = 0.0, c = 0.0, d = 0.0, real = None, i = None, imag = None, j = None, k = None):
		if real is not None:
			a = real
		if imag is not None:
			b = imag
		if i is not None:
			b = i
		if j is not None:
			c = j
		if k is not None:
			d = k
			
		if isinstance(a, quaternion):
			self.__dict__['a'] = a.a
			self.__dict__['b'] = a.b
			self.__dict__['c'] = a.c
			self.__dict__['d'] = a.d
		elif type(a) is types.ComplexType:
			self.__dict__['a'] = a.real
			self.__dict__['b'] = a.imag
			self.__dict__['c'] = 0.0
			self.__dict__['d'] = 0.0
		else:
			self.__dict__['a'] = float(a)
			self.__dict__['b'] = 0.0
			self.__dict__['c'] = 0.0
			self.__dict__['d'] = 0.0
		
		if isinstance(b, quaternion):
			self.__dict__['a'] = self.a - b.b
			self.__dict__['b'] = self.b + b.a
			self.__dict__['c'] = self.c - b.d
			self.__dict__['d'] = self.d + b.c
		elif type(b) is types.ComplexType:
			self.__dict__['a'] = self.a - b.imag
			self.__dict__['b'] = self.b + b.real
		else:
			self.__dict__['b'] = self.b + float(b)
			
		if isinstance(c, quaternion):
			self.__dict__['a'] = self.a - c.c
			self.__dict__['b'] = self.b + c.d
			self.__dict__['c'] = self.c + c.a
			self.__dict__['d'] = self.d - c.b
		elif type(c) is types.ComplexType:
			self.__dict__['c'] = self.c + c.real
			self.__dict__['d'] = self.d - c.imag
		else:
			self.__dict__['c'] = self.c + float(c)
			
		if isinstance(d, quaternion):
			self.__dict__['a'] = self.a - d.d
			self.__dict__['b'] = self.b - d.c
			self.__dict__['c'] = self.c + d.b
			self.__dict__['d'] = self.d + d.a
		elif type(d) is types.ComplexType:
			self.__dict__['c'] = self.c + d.imag
			self.__dict__['d'] = self.d + d.real
		else:
			self.__dict__['d'] = self.d + float(d)


	def __getattr__(self, name):
		global NUMERIC

		if name == 'real':
			return self.a
		elif name in ('imag', 'i'):
			return self.b
		elif name == 'j':
			return self.c
		elif name == 'k':
			return self.d
		elif name == 'matrix3':
			self.__dict__['matrix3'] = [[1.0 - 2.0*(self.c**2 + self.d**2),
			                             2.0*(self.b*self.c - self.d*self.a),
			                             2.0*(self.d*self.b + self.c*self.a)],
			                            [2.0*(self.b*self.c + self.d*self.a),
			                             1.0 - 2.0*(self.d**2 + self.b**2),
			                             2.0*(self.c*self.d - self.b*self.a)],
			                            [2.0*(self.d*self.b - self.c*self.a),
			                             2.0*(self.c*self.d + self.b*self.a),
			                             1.0 - 2.0 * (self.c**2 + self.b**2)]]
			if NUMERIC:
				self.__dict__['matrix3'] = Numeric.array(self.__dict__['matrix3'])
			return self.__dict__['matrix3']
		elif name == 'matrix4':
			self.__dict__['matrix4'] = [[1.0 - 2.0*(self.c**2 + self.d**2),
			                             2.0*(self.b*self.c - self.d*self.a),
			                             2.0*(self.d*self.b + self.c*self.a),
			                             0.0],
			                            [2.0*(self.b*self.c + self.d*self.a),
			                             1.0 - 2.0*(self.d**2 + self.b**2),
			                             2.0*(self.c*self.d - self.b*self.a),
			                             0.0],
			                            [2.0*(self.d*self.b - self.c*self.a),
			                             2.0*(self.c*self.d + self.b*self.a),
			                             1.0 - 2.0 * (self.c**2 + self.b**2),
			                             0.0],
									    [0.0,
			                             0.0,
			                             0.0,
			                             1.0]]
			if NUMERIC:
				self.__dict__['matrix4'] = Numeric.array(self.__dict__['matrix4'])
			return self.__dict__['matrix4']
		else:
			raise AttributeError, 'Attribute "%s" not found' % name


	def __reset(self):
		if self.__dict__.has_key('matrix3'):
			del self.__dict__['matrix3']
		if self.__dict__.has_key('matrix4'):
			del self.__dict__['matrix4']


	def __setattr__(self, name, value):
		if name in ('a', 'real'):
			self.__reset()
			if isinstance(value, quaternion):
				self.__dict__['a'] = value.a
				self.__dict__['b'] = self.b + value.b
				self.__dict__['c'] = self.c + value.c
				self.__dict__['d'] = self.d + value.d
			elif type(value) is types.ComplexType:
				self.__dict__['a'] = value.real
				self.__dict__['b'] = self.b + value.imag
			else:
				self.__dict__['a'] = float(value)
		elif name in ('b', 'imag', 'i'):
			self.__reset()
			if isinstance(value, quaternion):
				self.__dict__['a'] = self.a - value.b
				self.__dict__['b'] = value.a
				self.__dict__['c'] = self.c - value.d
				self.__dict__['d'] = self.d + value.c
			elif type(value) is types.ComplexType:
				self.__dict__['a'] = self.a - value.imag
				self.__dict__['b'] = value.real
			else:
				self.__dict__['b'] = float(value)
		elif name in ('c', 'j'):
			self.__reset()
			if isinstance(value, quaternion):
				self.__dict__['a'] = self.a - value.c
				self.__dict__['b'] = self.b + value.d
				self.__dict__['c'] = value.a
				self.__dict__['d'] = self.d - value.b
			elif type(value) is types.ComplexType:
				self.__dict__['c'] = value.real
				self.__dict__['d'] = self.d - value.imag
			else:
				self.__dict__['c'] = float(value)
		elif name in ('d', 'k'):
			self.__reset()
			if isinstance(value, quaternion):
				self.__dict__['a'] = self.a - value.d
				self.__dict__['b'] = self.b - value.c
				self.__dict__['c'] = self.c + value.b
				self.__dict__['d'] = value.a
			elif type(value) is types.ComplexType:
				self.__dict__['c'] = self.c + value.imag
				self.__dict__['d'] = value.real
			else:
				self.__dict__['d'] = float(value)
		elif name in ('matrix3', 'matrix4'):
			raise AttributeError, 'Attribute "%s" is read-only.' % name
		else:
			self.__dict__[name] = value


	def __len__(self):
		return 4


	def __setitem__(self, index, value):
		if index == 0:
			self.a = value
		elif index == 1:
			self.b = value
		elif index == 2:
			self.c = value
		elif index == 3:
			self.d = value
		else:
			raise IndexError, 'Index %s out of range' % index


	def __getitem__(self, index):
		if index == 0:
			return self.a
		elif index == 1:
			return self.b
		elif index == 2:
			return self.c
		elif index == 3:
			return self.d
		else:
			raise IndexError, 'Index %s out of range' % index


	def __coerce__(self, x):
		if isinstance(x, quaternion):
			return (self, x)
		x = complex(x)
		return (self, quaternion(x.real, x.imag))


	def __add__(self, x):
		return quaternion(self.a + x.a, self.b + x.b, self.c + x.c, self.d + x.d)


	def __sub__(self, x):
		return quaternion(self.a - x.a, self.b - x.b, self.c - x.c, self.d - x.d)


	def __mul__(self, x):
		return quaternion(self.a*x.a - self.b*x.b - self.c*x.c - self.d*x.d,
						  self.a*x.b + self.b*x.a + self.c*x.d - self.d*x.c,
						  self.a*x.c + self.c*x.a + self.d*x.b - self.b*x.d,
						  self.a*x.d + self.d*x.a + self.b*x.c - self.c*x.b)


	def __div__(self, x):
		return self*x.conj()*(1.0/(x*x.conj()).a)


	def __repr__(self):
		return 'quaternion(%g, %g, %g, %g)' % (self.a, self.b, self.c, self.d)


	def __str__(self):
		m = []
		for value, post in [(self.a, ''), (self.b, 'i'), (self.c, 'j'), (self.d, 'k')]:
			if value:
				m.append((value, post))
		if len(m):
			if m[0][0] == 1 and len(m[0][1]):
				x = m[0][1]
			else:
				x = '%g%s' % m[0]
			for value, post in m[1:]:
				if value < 0:
					x = x + ' - '
				else:
					x = x + ' + '
				if value == 1:
					x = x + post
				else:
					x = '%s%g%s' % (x, abs(value), post)
			return x
		return '0'


	def __abs__(self):
		return math.sqrt(self.a**2 + self.b**2 + self.c**2 + self.d**2)


	def __pos__(self):
		return quaternion(self.a, self.b, self.c, self.d)


	def __neg__(self):
		return quaternion(-self.a, -self.b, -self.c, -self.d)


	def conj(self):
		return quaternion(self.a, -self.b, -self.c, -self.d)


	def normalize(self):
		length = abs(self)
		if length:
			return self/length
		else:
			return self
