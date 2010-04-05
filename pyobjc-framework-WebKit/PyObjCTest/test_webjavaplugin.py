
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebJavaPlugIn (TestCase):
    def testConstants(self):
        self.assertEqual(WebJNIReturnTypeInvalid, 0)
        self.assertEqual(WebJNIReturnTypeVoid, 1)
        self.assertEqual(WebJNIReturnTypeObject, 2)
        self.assertEqual(WebJNIReturnTypeBoolean, 3)
        self.assertEqual(WebJNIReturnTypeByte, 4)
        self.assertEqual(WebJNIReturnTypeChar, 5)
        self.assertEqual(WebJNIReturnTypeShort, 6)
        self.assertEqual(WebJNIReturnTypeInt, 7)
        self.assertEqual(WebJNIReturnTypeLong, 8)
        self.assertEqual(WebJNIReturnTypeFloat, 9)
        self.assertEqual(WebJNIReturnTypeDouble, 10)


if __name__ == "__main__":
    main()
