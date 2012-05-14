from PyObjCTools.TestSupport import *
import objc

NSObject = objc.lookUpClass("NSObject")

class OC_AssocSneakyCopy (NSObject):
    def copy(self):
        return "<copy!>"

    def copyWithZone_(self, zone):
        return "<copy!>"

class TestAssocations (TestCase):

    @min_os_level("10.6")
    def testKeysAreIdentityBased(self):
        o = NSObject.alloc().init()

        key1 = "key1"
        key2 = "key11"[:-1]
        self.assertIsNot(key1, key2)

        self.assertEqual(objc.getAssociatedObject(o, key1), None)
        self.assertEqual(objc.getAssociatedObject(o, key2), None)

        objc.setAssociatedObject(o, key1, "foo")

        self.assertEqual(objc.getAssociatedObject(o, key1), "foo")
        self.assertEqual(objc.getAssociatedObject(o, key2), None)

    @min_os_level("10.6")
    def testGetSet(self):
        o = NSObject.alloc().init()

        key1 = "key1"
        self.assertEqual(objc.getAssociatedObject(o, key1), None)
        objc.setAssociatedObject(o, key1, "foo")
        self.assertEqual(objc.getAssociatedObject(o, key1), "foo")
        objc.setAssociatedObject(o, key1, None)
        self.assertEqual(objc.getAssociatedObject(o, key1), None)

    @min_os_level("10.6")
    def testClearing(self):

        o = NSObject.alloc().init()

        key1 = "key1"
        key2 = "key11"[:-1]
        self.assertIsNot(key1, key2)

        self.assertEqual(objc.getAssociatedObject(o, key1), None)
        self.assertEqual(objc.getAssociatedObject(o, key2), None)

        objc.setAssociatedObject(o, key1, "foo")
        objc.setAssociatedObject(o, key2, "bar")

        self.assertEqual(objc.getAssociatedObject(o, key1), "foo")
        self.assertEqual(objc.getAssociatedObject(o, key2), "bar")

        objc.removeAssociatedObjects(o)

        self.assertEqual(objc.getAssociatedObject(o, key1), None)
        self.assertEqual(objc.getAssociatedObject(o, key2), None)

    @min_os_level("10.6")
    def testPolicy(self):
        o = NSObject.alloc().init()
        key1 = "key1"
        key2 = "key11"[:-1]
        self.assertIsNot(key1, key2)

        value = OC_AssocSneakyCopy.alloc().init()

        self.assertEqual(objc.getAssociatedObject(o, key1), None)
        self.assertEqual(objc.getAssociatedObject(o, key2), None)

        objc.setAssociatedObject(o, key1, value, objc.OBJC_ASSOCIATION_RETAIN)
        objc.setAssociatedObject(o, key2, value, objc.OBJC_ASSOCIATION_COPY)

        self.assertEqual(objc.getAssociatedObject(o, key1), value)
        self.assertEqual(objc.getAssociatedObject(o, key2),  "<copy!>")


if __name__ == "__main__":
    main()
