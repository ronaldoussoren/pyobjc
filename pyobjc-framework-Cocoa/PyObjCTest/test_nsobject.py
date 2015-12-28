from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSObjectHelper (NSObject):
    def copyWithZone_(self, zn): return None
    def mutableCopyWithZone_(self, zn): return None
    def isContentDiscarded(self): return 1
    def beginContentAccess(self): return 1

    @classmethod
    def supportsSecureCoding(self): return 1

    def retainWeakReference(self): return 0
    def allowsWeakReference(self): return 0


class TestNSObjectFunctions (TestCase):
    def testAllocation(self):
        o = NSAllocateObject(NSObject, 0, None)
        self.assertIsInstance(o, NSObject)
        o = NSAllocateObject(NSObject, 50, None)
        self.assertIsInstance(o, NSObject)
        NSDeallocateObject(None)

    def testCopy(self):
        o = NSObject.alloc().init()
        self.assertIsInstance(o, NSObject)
        o2 = NSCopyObject(o, 50, None)
        self.assertIsInstance(o2, NSObject)

    def testShouldRetain(self):
        o = NSObject.alloc().init()
        self.assertIsInstance(o, NSObject)
        v = NSShouldRetainWithZone(o, None)
        self.assertTrue((v is True) or (v is False))

    def testRefCounts(self):
        o = NSObject.alloc().init()

        cnt = NSExtraRefCount(o)
        self.assertIsInstance(cnt, (int, long))
        NSIncrementExtraRefCount(o)
        v = NSExtraRefCount(o)
        self.assertEqual(v, cnt+1)

        v = NSDecrementExtraRefCountWasZero(o)
        self.assertIs(v, False)
        v = NSExtraRefCount(o)
        self.assertEqual(v, cnt)

    @min_os_level('10.7')
    def testFunctions10_7(self):
        # No further testing needed:
        CFBridgingRetain
        CFBridgingRelease


class TestNSObjectInteraction(TestCase):
    def testCallingInstanceMethodWithClassSelf(self):
        self.assertRaises(TypeError, NSObject.description, NSObject)
        self.assertRaises(TypeError, NSObject.description, "hello")

    def testNSObjectClassMethod(self):
        # Check that -class is accesible as 'class__' and 'class' (the latter
        # only through getattr because it is a Python keyword)
        self.assertTrue(hasattr(NSObject, 'class__'))
        self.assertTrue(isinstance(NSObject.class__, objc.selector))
        o = NSObject.alloc().init()
        self.assertTrue(o.class__() is o.__class__)

        self.assertTrue(hasattr(NSObject, 'class'))
        self.assertTrue(isinstance(getattr(NSObject, 'class'), objc.selector))
        self.assertTrue(getattr(o, 'class')() is o.__class__)

    def testNSObjectClass(self):
        self.assertTrue( NSObject.instancesRespondToSelector_( "description" ), "NSObject class claims it doesn't respond to a selector that it does." )
        self.assertTrue( hasattr(NSObject, "description"), "NSObject class claims it doesn't respond to a selector that it does." )
        # self.assertTrue( NSObject.description(), "NSObject class failed to respond to +description selector." )

    def testNSObjectInstance(self):
        instance = NSObject.new()

        self.assertTrue( instance, "Failed to instantiate an instance" )
        self.assertTrue( instance.description(), "NSObject instance didn't respond to -description selector." )
        self.assertTrue( not instance.isProxy(), "Instance of NSObject claimed it was a proxy.   That seems odd." )
        self.assertTrue( isinstance( instance, NSObject ), "Instantiated object not an instance of NSObject." )
        self.assertEqual( instance, instance, "Python identity check failed." )
        self.assertTrue( instance.isEqual_( instance ), "Obj-C identity check failed." )

    def testRepeatedAllocInit(self):
        for i in range(1,1000):
            a = NSObject.alloc().init()

    def testMethods(self):
        self.assertResultIsBOOL(NSObject.isEqual_)
        self.assertResultIsBOOL(NSObject.isProxy)
        self.assertResultIsBOOL(NSObject.isKindOfClass_)
        self.assertResultIsBOOL(NSObject.isMemberOfClass_)
        self.assertResultIsBOOL(NSObject.conformsToProtocol_)
        self.assertResultIsBOOL(NSObject.respondsToSelector_)
        self.assertResultIsBOOL(NSObject.instancesRespondToSelector_)
        self.assertResultIsBOOL(NSObject.isSubclassOfClass_)
        self.assertResultIsBOOL(NSObject.resolveClassMethod_)
        self.assertResultIsBOOL(NSObject.resolveInstanceMethod_)


        o = NSObject.alloc().init()
        self.assertResultIsBOOL(o.isEqual_)
        self.assertResultIsBOOL(o.isProxy)
        self.assertResultIsBOOL(o.isKindOfClass_)
        self.assertResultIsBOOL(o.isMemberOfClass_)
        self.assertResultIsBOOL(o.conformsToProtocol_)
        self.assertResultIsBOOL(o.respondsToSelector_)


        a = TestNSObjectHelper.alloc().init()
        self.assertArgHasType(a.copyWithZone_, 0, b'^{_NSZone=}')
        self.assertArgHasType(a.mutableCopyWithZone_, 0, b'^{_NSZone=}')

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(TestNSObjectHelper.beginContentAccess)
        self.assertResultIsBOOL(TestNSObjectHelper.isContentDiscarded)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(TestNSObjectHelper.allowsWeakReference)
        self.assertResultIsBOOL(TestNSObjectHelper.retainWeakReference)

        self.assertResultIsBOOL(TestNSObjectHelper.supportsSecureCoding)

    def testProtocols(self):
        objc.protocolNamed('NSCopying')
        objc.protocolNamed('NSMutableCopying')
        objc.protocolNamed('NSCoding')

    @min_sdk_level('10.6')
    def testProtocols10_6(self):
        objc.protocolNamed('NSDiscardableContent')

    @min_sdk_level('10.7')
    def testProtocols10_7(self):
        objc.protocolNamed('NSSecureCoding')


if __name__ == '__main__':
    main( )
