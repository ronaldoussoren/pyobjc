import math
from OpenGL.quaternion import *

__doc__ = '''A module which implements a trackball class.'''


class Trackball:
	'''A trackball object.  This is deformed trackball which is a hyperbolic
	   sheet of rotation away from the center. This particular function was chosen
	   after trying out several variations.  The current transformation matrix
	   can be retrieved using the "matrix" attribute.'''
	

	def __init__(self, size = 0.8, scale = 2.0, renorm = 97):
		'''Create a Trackball object.  "size" is the radius of the inner trackball
		   sphere.  "scale" is a multiplier applied to the mouse coordinates before
		   mapping into the viewport.  "renorm" is not currently used.'''
		
		self.size = size
		self.scale = scale
		self.renorm = renorm
		self.quat = quaternion(1, 0, 0, 0)
			

	def __track_project_to_sphere(self, px, py):
		d2 = px**2 + py**2
		d = math.sqrt(d2)
		if d < self.size * 0.70710678118654752440:
			# Inside sphere
			return math.sqrt(self.size**2 - d2)

		# On hyperbola
		t = self.size/1.41421356237309504880
		return t**2/d


	def update(self, p1x, p1y, p2x, p2y, width, height, mat = 0):
		'''Update the quaterion with a new rotation position derived
		   from the first point (p1) and the second point (p2).  The
		   the mat parameter is not currently used.'''
		
		if p1x == p2x and p1y == p2y:
			self.quat = quaternion(1, 0, 0, 0)
		else:
			# First, figure out z-coordinates for projection of p1 and p2 to
			# deformed sphere
			p1x_u = self.scale*p1x/width - 1.0
			p1y_u = 1.0 - self.scale*p1y/height
			p2x_u = self.scale*p2x/width - 1.0
			p2y_u = 1.0 - self.scale*p2y/height

			P1 = (p1x_u,p1y_u,self.__track_project_to_sphere(p1x_u, p1y_u)) 
			P2 = (p2x_u,p2y_u,self.__track_project_to_sphere(p2x_u, p2y_u))

			a = [(P2[1]*P1[2]) - (P2[2]*P1[1]),
			     (P2[2]*P1[0]) - (P2[0]*P1[2]),
			     (P2[0]*P1[1]) - (P2[1]*P1[0])]
			
			# Figure out how much to rotate around that axis.
			d = map(lambda x, y: x - y, P1, P2)
			t = math.sqrt(d[0]**2 + d[1]**2 + d[2]**2) / (2.0 * self.size)

			# Avoid problems with out-of-control values...
			t = max(min(t, 1.0), -1.0)

			scale = t*math.sqrt(a[0]**2 + a[1]**2 + a[2]**2)
			q = map(lambda x, y: x*y, a, [scale]*3) + [math.sqrt(1.0-t**2)]
			self.quat = quaternion(q[0], q[1], q[2], q[3])


	def __getattr__(self, name):
		if name != 'matrix':
			raise AttributeError, 'No attribute named "%s"' % name
		return self.quat.matrix4

	

glTrackball = Trackball
