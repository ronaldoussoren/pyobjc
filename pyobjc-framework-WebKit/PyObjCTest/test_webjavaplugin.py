from PyObjCTools.TestSupport import TestCase
import WebKit


class TestWebJavaPlugIn(TestCase):
    def testConstants(self):
        self.assertEqual(WebKit.WebJNIReturnTypeInvalid, 0)
        self.assertEqual(WebKit.WebJNIReturnTypeVoid, 1)
        self.assertEqual(WebKit.WebJNIReturnTypeObject, 2)
        self.assertEqual(WebKit.WebJNIReturnTypeBoolean, 3)
        self.assertEqual(WebKit.WebJNIReturnTypeByte, 4)
        self.assertEqual(WebKit.WebJNIReturnTypeChar, 5)
        self.assertEqual(WebKit.WebJNIReturnTypeShort, 6)
        self.assertEqual(WebKit.WebJNIReturnTypeInt, 7)
        self.assertEqual(WebKit.WebJNIReturnTypeLong, 8)
        self.assertEqual(WebKit.WebJNIReturnTypeFloat, 9)
        self.assertEqual(WebKit.WebJNIReturnTypeDouble, 10)
