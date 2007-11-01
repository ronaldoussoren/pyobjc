import unittest
import sys
import struct

import Foundation
import os

class GlobalFunctionTest (unittest.TestCase):
    if sys.platform == 'darwin':
        def testNSFileTypeForHFSTypeCode(self):
            self.assertEquals("'rtfx'",
                    Foundation.NSFileTypeForHFSTypeCode('rtfx'))

            # The cannonical representation for four-character-codes in python
            # is a string of 4 characters, but at least some ObjC API's return
            # longs (because these methods haven't been wrapped correctly yet).
            # NSFileTypeForHFSTypeCode therefore also accepts integers.
            fourchar = struct.unpack('i', 'rtfx')[0]
            if sys.byteorder == 'little':
		    self.assertEquals("'xftr'",
			    Foundation.NSFileTypeForHFSTypeCode(fourchar))
            else:
		    self.assertEquals("'rtfx'",
			    Foundation.NSFileTypeForHFSTypeCode(fourchar))

        def testNSHFSTypeCodeFromFileType(self):
            self.assertEquals(u"rtfx",
                    Foundation.NSHFSFTypeCodeFromFileType(u"'rtfx'"))


    def testMakeNSRect(self):
        self.assert_(hasattr(Foundation, 'NSMakeRect'))

        self.assertEquals(
                Foundation.NSMakeRect(1.5, 2.5, 3.5, 4.5),
                ((1.5, 2.5), (3.5, 4.5))
        )
        self.assertEquals(
                Foundation.NSMakeRect(1, 2, 3, 4),
                ((1.0, 2.0), (3.0, 4.0))
        )

        self.assertRaises(ValueError, Foundation.NSMakeRect, 1.0, 2.0, 3.0, '4')

    def test_NSDivideRect(self):
        rect1 = Foundation.NSMakeRect(1.0, 2.0, 3.0, 4.0)

        slice, rem = Foundation.NSDivideRect(rect1, None, None, 0.5, Foundation.NSMinXEdge)
        self.assertEquals(slice, ((1.0, 2.0), (0.5, 4.0)))
        self.assertEquals(rem,   ((1.5, 2.0), (2.5, 4.0)))

        slice, rem = Foundation.NSDivideRect(rect1, None, None, 0.5, Foundation.NSMinYEdge)
        self.assertEquals(slice, ((1.0, 2.0), (3.0, 0.5)))
        self.assertEquals(rem,   ((1.0, 2.5), (3.0, 3.5)))

    def testMisc(self):
        self.assert_(hasattr(Foundation, 'NSLogPageSize'))
        self.assert_(hasattr(Foundation, 'NSRangeFromString'))
        self.assert_(hasattr(Foundation, 'NSTemporaryDirectory'))
        self.assert_(hasattr(Foundation, 'NSDecrementExtraRefCountWasZero'))

class GlobalVariablesTest (unittest.TestCase):
    def testMisc(self):
        # enum
        self.assert_(hasattr(Foundation, 'NS_LittleEndian'))

        # NSString
        self.assert_(hasattr(Foundation, 'NSConnectionReplyMode'))

        # VAR
        if sys.platform == 'darwin':
            self.assert_(hasattr(Foundation, 'NSFoundationVersionNumber'))

class NSLogTest (unittest.TestCase):
    def startCaptureStderr(self):
        self.realStderr = os.dup(2)
        self.capturedStderr = open("/tmp/stderr.$$", "wb")
        os.dup2(self.capturedStderr.fileno(), 2)

    def stopCaptureStderr(self):
        os.dup2(self.realStderr, 2)
        self.capturedStderr.close()
        data = open("/tmp/stderr.$$", "rb").read()
        return data

    def testLogging(self):
        self.startCaptureStderr()
        try:
            Foundation.NSLog("This is a test")
        finally:

            data = self.stopCaptureStderr()
            self.assert_("This is a test" in data)

    def testLoggingWithFormattingChars(self):
        self.assertRaises(ValueError, Foundation.NSLog, "This is a test %@")

        self.startCaptureStderr()
        try:
            Foundation.NSLog("This is a test%@", ", ronald")
        finally:

            data = self.stopCaptureStderr()
            self.assert_("This is a test, ronald" in data, data)

    def testSpotlight(self):
        if hasattr(Foundation, 'NSMetadataQuery'):
            self.assert_(hasattr(Foundation, 'NSMetadataQueryDidFinishGatheringNotification'))
            self.assert_(isinstance(Foundation.NSMetadataQueryDidFinishGatheringNotification, unicode))


if __name__ == "__main__":
    unittest.main()
