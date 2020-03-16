from PyObjCTools.TestSupport import TestCase
import WebKit


class TestWebKitErrors(TestCase):
    def testConstants(self):
        self.assertIsInstance(WebKit.WebKitErrorDomain, str)
        self.assertIsInstance(WebKit.WebKitErrorMIMETypeKey, str)
        self.assertIsInstance(WebKit.WebKitErrorPlugInNameKey, str)
        self.assertIsInstance(WebKit.WebKitErrorPlugInPageURLStringKey, str)

        self.assertEqual(WebKit.WebKitErrorCannotShowMIMEType, 100)
        self.assertEqual(WebKit.WebKitErrorCannotShowURL, 101)
        self.assertEqual(WebKit.WebKitErrorFrameLoadInterruptedByPolicyChange, 102)
        self.assertEqual(WebKit.WebKitErrorCannotFindPlugIn, 200)
        self.assertEqual(WebKit.WebKitErrorCannotLoadPlugIn, 201)
        self.assertEqual(WebKit.WebKitErrorJavaUnavailable, 202)
        self.assertEqual(WebKit.WebKitErrorBlockedPlugInVersion, 203)
