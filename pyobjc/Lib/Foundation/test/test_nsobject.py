import unittest
import objc

from Foundation import *

class TestNSObjectInteraction(unittest.TestCase):
    def testCallingInstanceMethodWithClassSelf(self):
        self.assertRaises(TypeError, NSObject.description, NSObject)
        self.assertRaises(TypeError, NSObject.description, "hello")

    def testNSObjectClassMethod(self):
        # Check that -class is accesible as 'class__' and 'class' (the latter
        # only through getattr because it is a Python keyword)
        self.assert_(hasattr(NSObject, 'class__'))
        self.assert_(isinstance(NSObject.class__, objc.selector))
        o = NSObject.alloc().init()
        self.assert_(o.class__() is o.__class__)

        self.assert_(hasattr(NSObject, 'class'))
        self.assert_(isinstance(getattr(NSObject, 'class'), objc.selector))
        self.assert_(getattr(o, 'class')() is o.__class__)

    def testNSObjectClass(self):
        self.assert_( NSObject.instancesRespondToSelector_( "description" ), "NSObject class claims it doesn't respond to a selector that it does." )
        self.assert_( hasattr(NSObject, "description"), "NSObject class claims it doesn't respond to a selector that it does." )
        # self.assert_( NSObject.description(), "NSObject class failed to respond to +description selector." )

    def testNSObjectInstance(self):
        instance = NSObject.new()

        self.assert_( instance, "Failed to instantiate an instance" )
        self.assert_( instance.description(), "NSObject instance didn't respond to -description selector." )
        self.assert_( not instance.isProxy(), "Instance of NSObject claimed it was a proxy.   That seems odd." )
        self.assert_( isinstance( instance, NSObject ), "Instantiated object not an instance of NSObject." )
        self.assertEqual( instance, instance, "Python identity check failed." )
        self.assert_( instance.isEqual_( instance ), "Obj-C identity check failed." )

    def testRepeatedAllocInit(self):
        for i in range(1,1000):
            a = NSObject.alloc().init()

if __name__ == '__main__':
    unittest.main( )
