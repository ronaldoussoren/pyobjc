
from PyObjCTools.TestSupport import *
from WebKit import *

try:
    unicode
except NameError:
    unicode = str

class TestWebKitErrors (TestCase):
    def testConstants(self):
        self.assertIsInstance(WebKitErrorDomain, unicode)
        self.assertIsInstance(WebKitErrorMIMETypeKey, unicode)
        self.assertIsInstance(WebKitErrorPlugInNameKey, unicode)
        self.assertIsInstance(WebKitErrorPlugInPageURLStringKey, unicode)

        self.assertEqual(WebKitErrorCannotShowMIMEType, 100)
        self.assertEqual(WebKitErrorCannotShowURL, 101)
        self.assertEqual(WebKitErrorFrameLoadInterruptedByPolicyChange, 102)
        self.assertEqual(WebKitErrorCannotFindPlugIn, 200)
        self.assertEqual(WebKitErrorCannotLoadPlugIn, 201)
        self.assertEqual(WebKitErrorJavaUnavailable, 202)




if __name__ == "__main__":
    main()
