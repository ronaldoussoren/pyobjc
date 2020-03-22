import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSObjectHelper(Foundation.NSObject):
    def copyWithZone_(self, zn):
        return None

    def mutableCopyWithZone_(self, zn):
        return None

    def isContentDiscarded(self):
        return 1

    def beginContentAccess(self):
        return 1

    @classmethod
    def supportsSecureCoding(self):
        return 1

    def retainWeakReference(self):
        return 0

    def allowsWeakReference(self):
        return 0


class TestNSObjectFunctions(TestCase):
    def testAllocation(self):
        o = Foundation.NSAllocateObject(Foundation.NSObject, 0, None)
        self.assertIsInstance(o, Foundation.NSObject)
        o = Foundation.NSAllocateObject(Foundation.NSObject, 50, None)
        self.assertIsInstance(o, Foundation.NSObject)
        Foundation.NSDeallocateObject(None)

    def testCopy(self):
        o = Foundation.NSObject.alloc().init()
        self.assertIsInstance(o, Foundation.NSObject)
        o2 = Foundation.NSCopyObject(o, 50, None)
        self.assertIsInstance(o2, Foundation.NSObject)

    def testShouldRetain(self):
        o = Foundation.NSObject.alloc().init()
        self.assertIsInstance(o, Foundation.NSObject)
        v = Foundation.NSShouldRetainWithZone(o, None)
        self.assertTrue((v is True) or (v is False))

    def testRefCounts(self):
        o = Foundation.NSObject.alloc().init()

        cnt = Foundation.NSExtraRefCount(o)
        self.assertIsInstance(cnt, int)
        Foundation.NSIncrementExtraRefCount(o)
        v = Foundation.NSExtraRefCount(o)
        self.assertEqual(v, cnt + 1)

        v = Foundation.NSDecrementExtraRefCountWasZero(o)
        self.assertIs(v, False)
        v = Foundation.NSExtraRefCount(o)
        self.assertEqual(v, cnt)

    @min_os_level("10.7")
    def testFunctions10_7(self):
        # No further testing needed:
        Foundation.CFBridgingRetain
        Foundation.CFBridgingRelease


class TestNSObjectInteraction(TestCase):
    def testCallingInstanceMethodWithClassSelf(self):
        self.assertRaises(
            TypeError, Foundation.NSObject.description, Foundation.NSObject
        )
        self.assertRaises(TypeError, Foundation.NSObject.description, "hello")

    def testNSObjectClassMethod(self):
        # Check that -class is accesible as 'class__' and 'class' (the latter
        # only through getattr because it is a Python keyword)
        self.assertTrue(hasattr(Foundation.NSObject, "class__"))
        self.assertTrue(isinstance(Foundation.NSObject.class__, objc.selector))
        o = Foundation.NSObject.alloc().init()
        self.assertTrue(o.class__() is o.__class__)

        self.assertTrue(hasattr(Foundation.NSObject, "class"))
        self.assertTrue(
            isinstance(getattr(Foundation.NSObject, "class"), objc.selector)
        )
        self.assertTrue(getattr(o, "class")() is o.__class__)

    def testNSObjectClass(self):
        self.assertTrue(
            Foundation.NSObject.instancesRespondToSelector_("description"),
            "NSObject class claims it doesn't respond to a selector that it does.",
        )
        self.assertTrue(
            hasattr(Foundation.NSObject, "description"),
            "NSObject class claims it doesn't respond to a selector that it does.",
        )
        self.assertTrue(
            Foundation.NSObject.description(),
            "NSObject class failed to respond to +description selector.",
        )

    def testNSObjectInstance(self):
        instance = Foundation.NSObject.new()

        self.assertTrue(instance, "Failed to instantiate an instance")
        self.assertTrue(
            instance.description(),
            "NSObject instance didn't respond to -description selector.",
        )
        self.assertTrue(
            not instance.isProxy(),
            "Instance of Foundation.NSObject claimed it was a proxy.   That seems odd.",
        )
        self.assertTrue(
            isinstance(instance, Foundation.NSObject),
            "Instantiated object not an instance of Foundation.NSObject.",
        )
        self.assertEqual(instance, instance, "Python identity check failed.")
        self.assertTrue(instance.isEqual_(instance), "Obj-C identity check failed.")

    def testRepeatedAllocInit(self):
        for _ in range(1, 1000):
            _ = Foundation.NSObject.alloc().init()

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSObject.isEqual_)
        self.assertResultIsBOOL(Foundation.NSObject.isProxy)
        self.assertResultIsBOOL(Foundation.NSObject.isKindOfClass_)
        self.assertResultIsBOOL(Foundation.NSObject.isMemberOfClass_)
        self.assertResultIsBOOL(Foundation.NSObject.conformsToProtocol_)
        self.assertResultIsBOOL(Foundation.NSObject.respondsToSelector_)
        self.assertResultIsBOOL(Foundation.NSObject.instancesRespondToSelector_)
        self.assertResultIsBOOL(Foundation.NSObject.isSubclassOfClass_)
        self.assertResultIsBOOL(Foundation.NSObject.resolveClassMethod_)
        self.assertResultIsBOOL(Foundation.NSObject.resolveInstanceMethod_)

        o = Foundation.NSObject.alloc().init()
        self.assertResultIsBOOL(o.isEqual_)
        self.assertResultIsBOOL(o.isProxy)
        self.assertResultIsBOOL(o.isKindOfClass_)
        self.assertResultIsBOOL(o.isMemberOfClass_)
        self.assertResultIsBOOL(o.conformsToProtocol_)
        self.assertResultIsBOOL(o.respondsToSelector_)

        a = TestNSObjectHelper.alloc().init()
        self.assertArgHasType(a.copyWithZone_, 0, b"^{_NSZone=}")
        self.assertArgHasType(a.mutableCopyWithZone_, 0, b"^{_NSZone=}")

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(TestNSObjectHelper.beginContentAccess)
        self.assertResultIsBOOL(TestNSObjectHelper.isContentDiscarded)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(TestNSObjectHelper.allowsWeakReference)
        self.assertResultIsBOOL(TestNSObjectHelper.retainWeakReference)

        self.assertResultIsBOOL(TestNSObjectHelper.supportsSecureCoding)

    def testProtocols(self):
        objc.protocolNamed("NSCopying")
        objc.protocolNamed("NSMutableCopying")
        objc.protocolNamed("NSCoding")

    @min_sdk_level("10.6")
    def testProtocols10_6(self):
        objc.protocolNamed("NSDiscardableContent")

    @min_sdk_level("10.7")
    def testProtocols10_7(self):
        objc.protocolNamed("NSSecureCoding")
