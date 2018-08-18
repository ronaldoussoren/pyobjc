'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
import CoreServices

class TestLaunchServices (TestCase):
    def testValues(self):
        # Use this to test for a number of enum and #define values
        self.assert_( hasattr(CoreServices, 'kLSRequestAllInfo') )
        self.assert_( isinstance(CoreServices.kLSRequestAllInfo, (int, long)) )
        # Note: the header file seems to indicate otherwise but the value
        # really is a signed integer!
        self.assertEquals(CoreServices.kLSRequestAllInfo, 0xffffffff)

        self.assert_( hasattr(CoreServices, 'kLSLaunchInProgressErr') )
        self.assert_( isinstance(CoreServices.kLSLaunchInProgressErr, (int, long)) )
        self.assertEquals(CoreServices.kLSLaunchInProgressErr, -10818)


        self.assert_( hasattr(CoreServices, 'kLSInvalidExtensionIndex') )
        self.assert_( isinstance(CoreServices.kLSInvalidExtensionIndex, (int, long)) )


    def testVariables(self):
        self.assert_( hasattr(CoreServices, 'kUTTypeItem') )
        self.assert_( isinstance(CoreServices.kUTTypeItem, unicode) )

        self.assert_( hasattr(CoreServices, 'kUTTypeApplication') )
        self.assert_( isinstance(CoreServices.kUTTypeApplication, unicode) )

        self.assert_( hasattr(CoreServices, 'kUTExportedTypeDeclarationsKey') )
        self.assert_( isinstance(CoreServices.kUTExportedTypeDeclarationsKey, unicode) )

    def testFunctions(self):
        self.assert_( hasattr(CoreServices, 'UTTypeEqual') )
        self.assert_( isinstance(CoreServices.UTTypeEqual, objc.function) )

        self.assert_( hasattr(CoreServices, 'UTCreateStringForOSType') )
        self.assert_( isinstance(CoreServices.UTCreateStringForOSType, objc.function) )

        self.assert_( hasattr(CoreServices, 'LSSetDefaultHandlerForURLScheme') )
        self.assert_( isinstance(CoreServices.LSSetDefaultHandlerForURLScheme, objc.function) )

        self.assert_( hasattr(CoreServices, '_LSCopyAllApplicationURLs') )
        self.assert_( isinstance(CoreServices._LSCopyAllApplicationURLs, objc.function) )

        arr = CoreServices._LSCopyAllApplicationURLs(None)
        self.assert_( isinstance(arr, objc.lookUpClass('NSArray') ) )
        for a in arr:
            if str(a) == 'file://localhost/Applications/Calculator.app/':
                break
            elif str(a) == 'file:///Applications/Calculator.app/':
                break
        else:
            self.fail("No Calculator.app?")

        fn = CoreServices.LSGetExtensionInfo
        self.assertEquals( fn(10, b'hello.text'.decode('latin1'), None), (0, 6) )
        self.assertEquals( fn(10, 'hello.text', None), (0, 6) )

if __name__ == "__main__":
    main()
