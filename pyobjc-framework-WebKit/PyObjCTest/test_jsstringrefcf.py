import JavaScriptCore
from PyObjCTools.TestSupport import TestCase


class TestJSStrintRefCF(TestCase):
    def testFunctions(self):
        v = JavaScriptCore.JSStringCreateWithCFString("hello world")
        self.assertIsInstance(v, JavaScriptCore.JSStringRef)

        o = JavaScriptCore.JSStringCopyCFString(None, v)
        self.assertEqual(o, "hello world")
        self.assertIsInstance(o, str)
        self.assertResultIsCFRetained(JavaScriptCore.JSStringCopyCFString)

        JavaScriptCore.JSStringRelease(v)
