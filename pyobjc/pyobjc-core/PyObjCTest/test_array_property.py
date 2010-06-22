from PyObjCTools.TestSupport import *


class TestArrayProperty (TestCase):
    def testMissing(self):
        self.fail("Implement tests")

    def testGetting(self):
        # Check that default value is an empty value
        # Check that value is a proxy object
        self.fail("todo")

    def testSetting(self):
        # Set value, check that 
        # (1) value gets copied
        # (2) accessing the property result in proxy
        self.fail("todo")

    def testGetSetItem(self):
        # Use __getitem__, __setitem__ interface and check
        # that the correct KVO events get emitted.
        self.fail("todo")

    def testGetSetSlice(self):
        # Same as testGetSetItem, but using slice
        self.fail("todo")

    def testInsert(self):
        # Use insert method and check that the correct
        # KVO events get emitted
        self.fail("todo")

    def testPop(self):
        # Use pop method and check that the correct
        # KVO events get emitted
        self.fail("todo")

    def testDelItem(self):
        # Use __delitem__and check that the correct
        # KVO events get emitted
        self.fail("todo")

    def testDelSlice(self):
        # As testDelItem, but using slices
        self.fail("todo")

    def testSort(self):
        # Use sort method and check that the correct
        # KVO events get emitted
        self.fail("todo")

    def testReverse(self):
        # Use reverse method and check that the correct
        # KVO events get emitted
        self.fail("todo")

    def testKVOFromObjC(self):
        # Check that the right interfaces are implemented
        # to enable accessing and changing the property 
        # from ObjC, using an NSArrayController
        # (Which probably means that a number of KVC methods
        # need to be implemented)
        self.fail("todo")

    # Verify docs and/or implementation to check for other
    # mutating methods

    def testReadingMethods(self):
        # Check that all read-only methods work as well
        self.fail("todo")

    def testMutatingReadonlyProperty(self):
        # Check that trying to mutate a read-only property
        # will raise an exception
        self.fail("todo")

    def testMutatingReadonlyPropertyObjC(self):
        # Check that trying to mutate a read-only property
        # from ObjC will raise an exception
        self.fail("todo")


if __name__ == "__main__":
    main()
