from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSObjectHelper (NSObject):
    def copyWithZone_(self, zn): return None
    def mutableCopyWithZone_(self, zn): return None
    def isContentDiscarded(self): return 1
    def beginContentAccess(self): return 1

class TestNSObjectFunctions (TestCase):
    def testAllocation(self):
        o = NSAllocateObject(NSObject, 0, None)
        self.failUnless(isinstance(o, NSObject))

        o = NSAllocateObject(NSObject, 50, None)
        self.failUnless(isinstance(o, NSObject))

        NSDeallocateObject(None)

    def testCopy(self):
        o = NSObject.alloc().init()
        self.failUnless(isinstance(o, NSObject))
        o2 = NSCopyObject(o, 50, None)
        self.failUnless(isinstance(o2, NSObject))

    def testShouldRetain(self):
        o = NSObject.alloc().init()
        self.failUnless(isinstance(o, NSObject))

        v = NSShouldRetainWithZone(o, None)
        self.failUnless((v is True) or (v is False))

    def testRefCounts(self):
        o = NSObject.alloc().init()

        cnt = NSExtraRefCount(o)
        self.failUnless(isinstance(cnt, (int, long)))

        NSIncrementExtraRefCount(o)
        v = NSExtraRefCount(o)
        self.assertEquals(v, cnt+1)

        v = NSDecrementExtraRefCountWasZero(o)
        self.failUnless(v is False)

        v = NSExtraRefCount(o)
        self.assertEquals(v, cnt)






class TestNSObjectInteraction(TestCase):
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

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSObject.isEqual_)
        self.failUnlessResultIsBOOL(NSObject.isProxy)
        self.failUnlessResultIsBOOL(NSObject.isKindOfClass_)
        self.failUnlessResultIsBOOL(NSObject.isMemberOfClass_)
        self.failUnlessResultIsBOOL(NSObject.conformsToProtocol_)
        self.failUnlessResultIsBOOL(NSObject.respondsToSelector_)
        self.failUnlessResultIsBOOL(NSObject.instancesRespondToSelector_)
        self.failUnlessResultIsBOOL(NSObject.isSubclassOfClass_)
        self.failUnlessResultIsBOOL(NSObject.resolveClassMethod_)
        self.failUnlessResultIsBOOL(NSObject.resolveInstanceMethod_)

        o = NSObject.alloc().init()
        self.failUnlessResultIsBOOL(o.isEqual_)
        self.failUnlessResultIsBOOL(o.isProxy)
        self.failUnlessResultIsBOOL(o.isKindOfClass_)
        self.failUnlessResultIsBOOL(o.isMemberOfClass_)
        self.failUnlessResultIsBOOL(o.conformsToProtocol_)
        self.failUnlessResultIsBOOL(o.respondsToSelector_)


        a = TestNSObjectHelper.alloc().init()
        self.failUnlessArgHasType(a.copyWithZone_, 0, '^{_NSZone=}')
        self.failUnlessArgHasType(a.mutableCopyWithZone_, 0, '^{_NSZone=}')

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(TestNSObjectHelper.beginContentAccess)
        self.failUnlessResultIsBOOL(TestNSObjectHelper.isContentDiscarded)


if __name__ == '__main__':
    main( )
