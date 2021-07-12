import os
import sys

import CoreFoundation
from PyObjCTools.TestSupport import TestCase


class TestURLAccess(TestCase):
    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFURLUnknownError, -10)
        self.assertEqual(CoreFoundation.kCFURLUnknownSchemeError, -11)
        self.assertEqual(CoreFoundation.kCFURLResourceNotFoundError, -12)
        self.assertEqual(CoreFoundation.kCFURLResourceAccessViolationError, -13)
        self.assertEqual(CoreFoundation.kCFURLRemoteHostUnavailableError, -14)
        self.assertEqual(CoreFoundation.kCFURLImproperArgumentsError, -15)
        self.assertEqual(CoreFoundation.kCFURLUnknownPropertyKeyError, -16)
        self.assertEqual(CoreFoundation.kCFURLPropertyKeyUnavailableError, -17)
        self.assertEqual(CoreFoundation.kCFURLTimeoutError, -18)
        self.assertIsInstance(CoreFoundation.kCFURLFileExists, str)
        self.assertIsInstance(CoreFoundation.kCFURLFileDirectoryContents, str)
        self.assertIsInstance(CoreFoundation.kCFURLFileLength, str)
        self.assertIsInstance(CoreFoundation.kCFURLFileLastModificationTime, str)
        self.assertIsInstance(CoreFoundation.kCFURLFilePOSIXMode, str)
        self.assertIsInstance(CoreFoundation.kCFURLFileOwnerID, str)
        self.assertIsInstance(CoreFoundation.kCFURLHTTPStatusCode, str)
        self.assertIsInstance(CoreFoundation.kCFURLHTTPStatusLine, str)

    def testFunctions(self):
        url = CoreFoundation.CFURLCreateWithFileSystemPath(
            None, __file__, CoreFoundation.kCFURLPOSIXPathStyle, False
        )

        self.assertArgIsOut(CoreFoundation.CFURLCreatePropertyFromResource, 3)
        val, errorCode = CoreFoundation.CFURLCreatePropertyFromResource(
            None, url, CoreFoundation.kCFURLFileExists, None
        )
        self.assertIsInstance(errorCode, int)
        self.assertIs(val, True)
        self.assertResultIsBOOL(CoreFoundation.CFURLCreateDataAndPropertiesFromResource)
        self.assertArgIsOut(CoreFoundation.CFURLCreateDataAndPropertiesFromResource, 2)
        self.assertArgIsOut(CoreFoundation.CFURLCreateDataAndPropertiesFromResource, 3)
        self.assertArgIsOut(CoreFoundation.CFURLCreateDataAndPropertiesFromResource, 5)
        (
            ok,
            data,
            properties,
            errorCode,
        ) = CoreFoundation.CFURLCreateDataAndPropertiesFromResource(  # noqa: B950
            None, url, None, None, None, None
        )
        self.assertTrue(ok)
        self.assertIsInstance(data, CoreFoundation.CFDataRef)
        self.assertIsInstance(properties, CoreFoundation.CFDictionaryRef)
        self.assertIsInstance(errorCode, int)
        self.assertTrue(properties[CoreFoundation.kCFURLFileExists])

        self.assertResultIsBOOL(CoreFoundation.CFURLWriteDataAndPropertiesToResource)
        self.assertArgIsOut(CoreFoundation.CFURLWriteDataAndPropertiesToResource, 3)
        url = CoreFoundation.CFURLCreateWithFileSystemPath(
            None, __file__ + "TEST", CoreFoundation.kCFURLPOSIXPathStyle, False
        )

        if sys.version_info[0] == 3:

            def buffer(value):
                return value

        else:
            from __builtin__ import buffer

        ok, errorCode = CoreFoundation.CFURLWriteDataAndPropertiesToResource(
            url, buffer(b"foobar"), None, None
        )
        self.assertTrue(ok)
        self.assertIsInstance(errorCode, int)
        self.assertTrue(os.path.exists(__file__ + "TEST"))
        with open(__file__ + "TEST") as fp:
            data = fp.read()
        self.assertEqual(data, "foobar")
        self.assertResultIsBOOL(CoreFoundation.CFURLDestroyResource)
        self.assertArgIsOut(CoreFoundation.CFURLDestroyResource, 1)
        ok, errorCode = CoreFoundation.CFURLDestroyResource(url, None)
        self.assertTrue(ok)
        self.assertIsInstance(errorCode, int)
        self.assertFalse(os.path.exists(__file__ + "TEST"))
