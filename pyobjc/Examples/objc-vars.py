#!/usr/bin/env python
"""
Using and accessing instance variables.
"""
import objc

NSObject = objc.lookUpClass('NSObject')

class MyClass (NSObject):
	test = objc.ivar('test', '@')
	test2 = objc.ivar('test2', 'd')

	def init_(self, obj):
		print "x", self, obj
		self.test = obj
		self.test2 = 23.4
		print self.test
		print "x"
		self.test = self
		print "x"
		return self

	def __del__(self):
		print "Del of MyClass instance"

x = MyClass.alloc().init_('22')
print x.test
print x.test2
