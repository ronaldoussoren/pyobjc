#
# Subclassing an objective-C class from python.
#
# This shows that we can override a method in an objective-C class, and have
# it called from objective-C. 
#
import sys
import objc

NSEnumerator = objc.lookup_class('NSEnumerator')

class Demo (NSEnumerator):
	__slots__ = ('cnt',)

	def init(self):
		self.cnt = 10
		return self

	def nextObject(self):
		print "nextObject" ,  self.retainCount()
		if self.cnt == 0:
			return None
		self.cnt -= 1
		return self.cnt

	def __del__(self):
		print "Bye from Demo instance"

print Demo.alloc
obj = Demo.alloc()
print "->", obj.retainCount();

obj = obj.init()
print "->", obj.retainCount();
print "next->", obj.nextObject();
print "->", obj.retainCount();

x = obj.allObjects()
print '->', obj.retainCount()
print "all->", x.description()
x=None

obj = None
print "Done"

objc.recycle_autorelease_pool()
