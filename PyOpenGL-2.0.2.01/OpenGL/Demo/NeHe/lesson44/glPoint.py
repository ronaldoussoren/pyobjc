import glVector

class glPoint (list):
	def __init__ (self, first = 0, second = 0, third = 0):
		# Allow creation from a vector
		if (isinstance (first, glVector.glVector)):
			self.x = first.i
			self.y = first.j
			self.z = first.k
		else:
			self.x = first
			self.y = second
			self.z = third

	def __str__ (self):
		return "x=%f y=%f z=%f" % (self.x, self.y, self.z)

	def __iadd__ (self, other):
		self.x += other.x
		self.y += other.y
		self.z += other.z
		return self

	def __add__ (self, other):
		result = glPoint (self.x, self.y, self.z)
		result += other
		return result

	def __sub__ (self, other):
		""" Create a vector from the difference between this point and another point """
		result = glVector.glVector (self.x - other.x, self.y - other.y, self.z - other.z)
		return result
