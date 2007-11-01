'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import LaunchServices

class TestLaunchServices (unittest.TestCase):
    def testValues(self):
        # Use this to test for a number of enum and #define values
        self.assert_( hasattr(LaunchServices, 'kLSRequestAllInfo') )
        self.assert_( isinstance(LaunchServices.kLSRequestAllInfo, (int, long)) )
        # Note: the header file seems to indicate otherwise but the value 
        # really is a signed integer!
        #self.assertEquals(LaunchServices.kLSRequestAllInfo, 0xffffffff)
        self.assertEquals(LaunchServices.kLSRequestAllInfo, -1)

        self.assert_( hasattr(LaunchServices, 'kLSLaunchInProgressErr') )
        self.assert_( isinstance(LaunchServices.kLSLaunchInProgressErr, (int, long)) )
        self.assertEquals(LaunchServices.kLSLaunchInProgressErr, -10818)


        self.assert_( hasattr(LaunchServices, 'kLSInvalidExtensionIndex') )
        self.assert_( isinstance(LaunchServices.kLSInvalidExtensionIndex, (int, long)) )


    def testVariables(self):
        self.assert_( hasattr(LaunchServices, 'kUTTypeItem') )
        self.assert_( isinstance(LaunchServices.kUTTypeItem, unicode) )

        self.assert_( hasattr(LaunchServices, 'kUTTypeApplication') )
        self.assert_( isinstance(LaunchServices.kUTTypeApplication, unicode) )

        self.assert_( hasattr(LaunchServices, 'kUTExportedTypeDeclarationsKey') )
        self.assert_( isinstance(LaunchServices.kUTExportedTypeDeclarationsKey, unicode) )

    def testFunctions(self):
        self.assert_( hasattr(LaunchServices, 'UTTypeEqual') )
        self.assert_( isinstance(LaunchServices.UTTypeEqual, objc.function) )

        self.assert_( hasattr(LaunchServices, 'UTCreateStringForOSType') )
        self.assert_( isinstance(LaunchServices.UTCreateStringForOSType, objc.function) )

        self.assert_( hasattr(LaunchServices, 'LSSetDefaultHandlerForURLScheme') )
        self.assert_( isinstance(LaunchServices.LSSetDefaultHandlerForURLScheme, objc.function) )

        self.assert_( hasattr(LaunchServices, '_LSCopyAllApplicationURLs') )
        self.assert_( isinstance(LaunchServices._LSCopyAllApplicationURLs, objc.function) )

        arr = LaunchServices._LSCopyAllApplicationURLs(None)
        self.assert_( isinstance(arr, objc.lookUpClass('NSArray') ) )
        for a in arr:
            if str(a) == 'file://localhost/Applications/Calculator.app/':
                break
        else:
            self.fail("No Calculator.app?")

        fn = LaunchServices.LSGetExtensionInfo
        self.assertEquals( fn(10, u'hello.text', None), (0, 6) )
        self.assertEquals( fn(10, 'hello.text', None), (0, 6) )

if __name__ == "__main__":
    unittest.main()

