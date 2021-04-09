"""
Some simple tests to check that the framework is properly wrapped.
"""
import CoreServices
from PyObjCTools.TestSupport import TestCase
import objc


class TestLaunchServices(TestCase):
    def testValues(self):
        # Use this to test for a number of enum and #define values
        self.assertTrue(hasattr(CoreServices, "kLSRequestAllInfo"))
        self.assertTrue(isinstance(CoreServices.kLSRequestAllInfo, int))
        # Note: the header file seems to indicate otherwise but the value
        # really is a signed integer!
        self.assertEqual(CoreServices.kLSRequestAllInfo, 0xFFFFFFFF)

        self.assertTrue(hasattr(CoreServices, "kLSLaunchInProgressErr"))
        self.assertTrue(isinstance(CoreServices.kLSLaunchInProgressErr, int))
        self.assertEqual(CoreServices.kLSLaunchInProgressErr, -10818)

        self.assertTrue(hasattr(CoreServices, "kLSInvalidExtensionIndex"))
        self.assertTrue(isinstance(CoreServices.kLSInvalidExtensionIndex, int))

    def testVariables(self):
        self.assertTrue(hasattr(CoreServices, "kUTTypeItem"))
        self.assertTrue(isinstance(CoreServices.kUTTypeItem, str))

        self.assertTrue(hasattr(CoreServices, "kUTTypeApplication"))
        self.assertTrue(isinstance(CoreServices.kUTTypeApplication, str))

        self.assertTrue(hasattr(CoreServices, "kUTExportedTypeDeclarationsKey"))
        self.assertTrue(isinstance(CoreServices.kUTExportedTypeDeclarationsKey, str))

    def testFunctions(self):
        self.assertTrue(hasattr(CoreServices, "UTTypeEqual"))
        self.assertTrue(isinstance(CoreServices.UTTypeEqual, objc.function))

        self.assertTrue(hasattr(CoreServices, "UTCreateStringForOSType"))
        self.assertTrue(isinstance(CoreServices.UTCreateStringForOSType, objc.function))

        self.assertTrue(hasattr(CoreServices, "LSSetDefaultHandlerForURLScheme"))
        self.assertTrue(
            isinstance(CoreServices.LSSetDefaultHandlerForURLScheme, objc.function)
        )

        self.assertTrue(hasattr(CoreServices, "_LSCopyAllApplicationURLs"))
        self.assertTrue(
            isinstance(CoreServices._LSCopyAllApplicationURLs, objc.function)
        )

        fn = CoreServices.LSGetExtensionInfo
        self.assertEqual(fn(10, "hello.text", None), (0, 6))
        self.assertEqual(fn(10, "hello.text", None), (0, 6))

        arr = CoreServices._LSCopyAllApplicationURLs(None)
        self.assertTrue(isinstance(arr, objc.lookUpClass("NSArray")))
        for a in arr:
            if str(a) == "file://localhost/Applications/Calculator.app/":
                break
            elif str(a) == "file:///Applications/Calculator.app/":
                break
            elif str(a) == "file:///System/Applications/Calculator.app/":
                break
        else:
            self.fail("No Calculator.app?")
