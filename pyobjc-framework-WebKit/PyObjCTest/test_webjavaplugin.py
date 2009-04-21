
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebJavaPlugIn (TestCase):
    def testConstants(self):
        self.failUnlessEqual(WebJNIReturnTypeInvalid, 0)
        self.failUnlessEqual(WebJNIReturnTypeVoid, 1)
        self.failUnlessEqual(WebJNIReturnTypeObject, 2)
        self.failUnlessEqual(WebJNIReturnTypeBoolean, 3)
        self.failUnlessEqual(WebJNIReturnTypeByte, 4)
        self.failUnlessEqual(WebJNIReturnTypeChar, 5)
        self.failUnlessEqual(WebJNIReturnTypeShort, 6)
        self.failUnlessEqual(WebJNIReturnTypeInt, 7)
        self.failUnlessEqual(WebJNIReturnTypeLong, 8)
        self.failUnlessEqual(WebJNIReturnTypeFloat, 9)
        self.failUnlessEqual(WebJNIReturnTypeDouble, 10)


if __name__ == "__main__":
    main()
