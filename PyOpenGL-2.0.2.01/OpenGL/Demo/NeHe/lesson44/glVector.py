# mirros glVector.cpp - slow no nummarray
import math


# The glVector of lesson 44 has three componenets only
# i j k
class glVector:
	# Need to create from a point?
	def __init__ (self, *args):
		if (len (args) == 3):
			self.i = args [0]
			self.j = args [1]
			self.k = args [2]
			return
		if (len (args) == 1):
			# // Assign this vector to the vector passed in.
			src_v = args [0]
			if (not isinstance (src_v, glVector)):
				raise TypeError, "Invalid ctor argument for glVector"
			self.i = src_v.i
			self.j = src_v.j
			self.k = src_v.k
			return
		elif (len (args) == 0):
			self.i = 0
			self.j = 0
			self.k = 0
			return
		else:
			raise TypeError, "Invalid ctor argument for glVector"

	# def __setattr__ (self, name, value)
	#	""" We want to """
	#	self.name = value

	def Magnitude (self):
		Mag = math.sqrt (self.i * self.i + self.j * self.j + self.k * self.k)
		return Mag

	def Normalize (self):
		mag = self.Magnitude ()
		if (mag != 0.0):
			self.i = self.i / mag
			self.j = self.j / mag
			self.k = self.k / mag
		return

	def __mul__ (self, scalar):
		result = glVector (self)
		result *= scalar
		return result

	def __imul__ (self, other):
		if (type (other) == int):
			scalar = other
			self.i *= scalar
			self.j *= scalar
			self.k *= scalar
		elif (type (other) == float):
			scalar = other
			self.i *= scalar
			self.j *= scalar
			self.k *= scalar
		else:
			raise TypeError, "Invalid type (%s) for multiplication argument" % (str (type (other)))

		return self


	def __add__ (self, v):
		result = copy.copy (self)
		result += v
		return result

	def __iadd__ (self, v):
		self.i += v.i
		self.j += v.j
		self.k += v.k
		return self

	def __sub__ (self, other):
		self.i -= v.i
		self.j -= v.j
		self.k -= v.k
		return self

	def __str__ (self):
		return "i=%f j=%f k=%f, magnitude=%f" % (self.i, self.j, self.k, self.Magnitude ())



# Unit Test harness if this python module is run directly.
if __name__ == "__main__":
	print "testing slow glpoint/vect.\n"
	v = glVector ()
	v.i = 1.1
	v.Magnitude ()
	print v
	print "mult new"
	print (v * 2)
	print "Done"
