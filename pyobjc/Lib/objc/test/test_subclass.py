import unittest

import objc

# Most usefull systems will at least have 'NSObject'.
NSObject = objc.lookup_class('NSObject')



class TestSubclassing(unittest.TestCase):

	def testSubclassOfSubclass(self):
		class Level1Class (NSObject):
			def hello(self):
				return "level1"

		class Level2Class (Level1Class):
			def hello(self):
				return "level2"

		obj = Level1Class.alloc().init()
		v = obj.hello()
		self.assert_(v == "level1")

		obj = Level2Class.alloc().init()
		v = obj.hello()
		self.assert_(v == "level2")
	
	def testUniqueNames(self):
		class SomeClass (NSObject): pass

		try:
			class SomeClass (NSObject): pass

			assert_(0)
		except objc.error, msg:
			assert(str(msg) == "Class already exists in Objective-C runtime")



	


def suite():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite( TestInstantiation ) )

if __name__ == '__main__':
    unittest.main( )
