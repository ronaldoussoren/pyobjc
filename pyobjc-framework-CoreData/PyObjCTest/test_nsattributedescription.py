
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSAttributeDescription (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSUndefinedAttributeType, 0)
        self.failUnlessEqual(NSInteger16AttributeType, 100)
        self.failUnlessEqual(NSInteger32AttributeType, 200)
        self.failUnlessEqual(NSInteger64AttributeType, 300)
        self.failUnlessEqual(NSDecimalAttributeType, 400)
        self.failUnlessEqual(NSDoubleAttributeType, 500)
        self.failUnlessEqual(NSFloatAttributeType, 600)
        self.failUnlessEqual(NSStringAttributeType, 700)
        self.failUnlessEqual(NSBooleanAttributeType, 800)
        self.failUnlessEqual(NSDateAttributeType, 900)
        self.failUnlessEqual(NSBinaryDataAttributeType, 1000)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.failUnlessEqual(NSTransformableAttributeType, 1800)


if __name__ == "__main__":
    main()
