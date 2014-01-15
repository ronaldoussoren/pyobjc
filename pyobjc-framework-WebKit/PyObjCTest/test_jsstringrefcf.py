from PyObjCTools.TestSupport import *

import JavaScriptCore

try:
    unicode
except NameError:
    unicode = str


class TestJSStrintRefCF (TestCase):

    def testFunctions(self):
        v = JavaScriptCore.JSStringCreateWithCFString("hello world")
        self.assertIsInstance(v, JavaScriptCore.JSStringRef)

        o = JavaScriptCore.JSStringCopyCFString(None, v)
        self.assertEqual(o, "hello world")
        self.assertIsInstance(o, unicode)
        self.assertResultIsCFRetained(JavaScriptCore.JSStringCopyCFString)

        JavaScriptCore.JSStringRelease(v)


if __name__ == "__main__":
    main()
