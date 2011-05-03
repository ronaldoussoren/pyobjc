import os
from PyObjCTools.TestSupport import *
from CoreFoundation import *
import sys


class TestURLAccess (TestCase):
    def testConstants(self):
        self.assertEqual(kCFURLUnknownError , -10  )
        self.assertEqual(kCFURLUnknownSchemeError , -11    )
        self.assertEqual(kCFURLResourceNotFoundError , -12 )
        self.assertEqual(kCFURLResourceAccessViolationError , -13  )
        self.assertEqual(kCFURLRemoteHostUnavailableError , -14    )
        self.assertEqual(kCFURLImproperArgumentsError , -15    )
        self.assertEqual(kCFURLUnknownPropertyKeyError , -16   )
        self.assertEqual(kCFURLPropertyKeyUnavailableError , -17   )
        self.assertEqual(kCFURLTimeoutError , -18 )
        self.assertIsInstance( kCFURLFileExists, unicode)
        self.assertIsInstance( kCFURLFileDirectoryContents, unicode)
        self.assertIsInstance( kCFURLFileLength, unicode)
        self.assertIsInstance( kCFURLFileLastModificationTime, unicode)
        self.assertIsInstance( kCFURLFilePOSIXMode, unicode)
        self.assertIsInstance( kCFURLFileOwnerID, unicode)
        self.assertIsInstance( kCFURLHTTPStatusCode, unicode)
        self.assertIsInstance( kCFURLHTTPStatusLine, unicode)
    def testFunctions(self):
        url = CFURLCreateWithFileSystemPath(None, __file__, kCFURLPOSIXPathStyle, False)

        self.assertArgIsOut(CFURLCreatePropertyFromResource, 3)
        val, errorCode = CFURLCreatePropertyFromResource(None, url, kCFURLFileExists, None)
        self.assertIsInstance(errorCode, (int, long))
        self.assertIs(val, True)
        self.assertResultIsBOOL(CFURLCreateDataAndPropertiesFromResource)
        self.assertArgIsOut(CFURLCreateDataAndPropertiesFromResource, 2)
        self.assertArgIsOut(CFURLCreateDataAndPropertiesFromResource, 3)
        self.assertArgIsOut(CFURLCreateDataAndPropertiesFromResource, 5)
        ok, data, properties, errorCode = CFURLCreateDataAndPropertiesFromResource(
                None, url, None, None, None, None)
        self.assertTrue(ok)
        self.assertIsInstance(data, CFDataRef)
        self.assertIsInstance(properties, CFDictionaryRef)
        self.assertIsInstance(errorCode, (int, long))
        self.assertTrue(properties[kCFURLFileExists])

        self.assertResultIsBOOL(CFURLWriteDataAndPropertiesToResource)
        self.assertArgIsOut(CFURLWriteDataAndPropertiesToResource, 3)
        url = CFURLCreateWithFileSystemPath(None, __file__ + "TEST", kCFURLPOSIXPathStyle, False)

        if sys.version_info[0] == 3:
            def buffer(value):
                return value
        else:
            from __builtin__ import buffer

        ok, errorCode = CFURLWriteDataAndPropertiesToResource(
                url, buffer(b"foobar"), None, None)
        self.assertTrue(ok)
        self.assertIsInstance(errorCode, (int, long))
        self.assertTrue(os.path.exists(__file__ + "TEST"))
        data = open(__file__ + "TEST", 'r').read()
        self.assertEqual(data , 'foobar')
        self.assertResultIsBOOL(CFURLDestroyResource)
        self.assertArgIsOut(CFURLDestroyResource, 1)
        ok, errorCode = CFURLDestroyResource(url, None)
        self.assertTrue(ok)
        self.assertIsInstance(errorCode, (int, long))
        self.assertFalse(os.path.exists(__file__ + "TEST"))


            
                
if __name__ == "__main__":
    main()
