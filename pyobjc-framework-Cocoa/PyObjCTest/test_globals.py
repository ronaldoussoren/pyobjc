import os
import struct
import sys

import Foundation
from PyObjCTools.TestSupport import TestCase


class GlobalFunctionTest(TestCase):
    if sys.platform == "darwin":

        def testNSFileTypeForHFSTypeCode(self):
            self.assertEqual("'rtfx'", Foundation.NSFileTypeForHFSTypeCode(b"rtfx"))

            # The cannonical representation for four-character-codes in python
            # is a string of 4 characters, but at least some ObjC API's return
            # longs (because these methods haven't been wrapped correctly yet).
            # NSFileTypeForHFSTypeCode therefore also accepts integers.
            fourchar = struct.unpack("i", b"rtfx")[0]
            if sys.byteorder == "little":
                self.assertEqual(
                    "'xftr'", Foundation.NSFileTypeForHFSTypeCode(fourchar)
                )
            else:
                self.assertEqual(
                    "'rtfx'", Foundation.NSFileTypeForHFSTypeCode(fourchar)
                )

        def testNSHFSTypeCodeFromFileType(self):
            self.assertEqual(b"rtfx", Foundation.NSHFSFTypeCodeFromFileType("'rtfx'"))

    def testMakeNSRect(self):
        self.assertHasAttr(Foundation, "NSMakeRect")

        self.assertEqual(
            Foundation.NSMakeRect(1.5, 2.5, 3.5, 4.5), ((1.5, 2.5), (3.5, 4.5))
        )
        self.assertEqual(Foundation.NSMakeRect(1, 2, 3, 4), ((1.0, 2.0), (3.0, 4.0)))
        self.assertIsInstance(Foundation.NSMakeRect(1, 2, 3, 4), Foundation.NSRect)

        self.assertRaises(ValueError, Foundation.NSMakeRect, 1.0, 2.0, 3.0, "4")

    def test_NSDivideRect(self):
        rect1 = Foundation.NSMakeRect(1.0, 2.0, 3.0, 4.0)

        slice_value, rem = Foundation.NSDivideRect(
            rect1, None, None, 0.5, Foundation.NSMinXEdge
        )
        self.assertEqual(slice_value, ((1.0, 2.0), (0.5, 4.0)))
        self.assertEqual(rem, ((1.5, 2.0), (2.5, 4.0)))

        slice_value, rem = Foundation.NSDivideRect(
            rect1, None, None, 0.5, Foundation.NSMinYEdge
        )
        self.assertEqual(slice_value, ((1.0, 2.0), (3.0, 0.5)))
        self.assertEqual(rem, ((1.0, 2.5), (3.0, 3.5)))

    def testMisc(self):
        self.assertHasAttr(Foundation, "NSLogPageSize")
        self.assertHasAttr(Foundation, "NSRangeFromString")
        self.assertHasAttr(Foundation, "NSTemporaryDirectory")
        self.assertHasAttr(Foundation, "NSDecrementExtraRefCountWasZero")


class GlobalVariablesTest(TestCase):
    def testMisc(self):
        # enum
        self.assertHasAttr(Foundation, "NS_LittleEndian")

        # NSString
        self.assertHasAttr(Foundation, "NSConnectionReplyMode")

        # VAR
        self.assertHasAttr(Foundation, "NSFoundationVersionNumber")


class NSLogTest(TestCase):
    def startCaptureStderr(self):
        self.realStderr = os.dup(2)
        self.capturedStderr = open("/tmp/stderr.$$", "wb")
        os.dup2(self.capturedStderr.fileno(), 2)

    def stopCaptureStderr(self):
        os.dup2(self.realStderr, 2)
        self.capturedStderr.close()
        with open("/tmp/stderr.$$", "rb") as fp:
            data = fp.read()
        return data

    def testLogging(self):
        self.startCaptureStderr()
        try:
            Foundation.NSLog("This is a test")
        finally:

            data = self.stopCaptureStderr()
            self.assertIn(b"This is a test", data)

    def testLoggingWithFormattingChars(self):
        self.assertRaises(ValueError, Foundation.NSLog, "This is a test %@")

        self.startCaptureStderr()
        try:
            Foundation.NSLog("This is a test%@", ", ronald")
        finally:

            data = self.stopCaptureStderr()
            self.assertIn(b"This is a test, ronald", data)

    def testSpotlight(self):
        if hasattr(Foundation, "NSMetadataQuery"):
            self.assertHasAttr(
                Foundation, "NSMetadataQueryDidFinishGatheringNotification"
            )
            self.assertIsInstance(
                Foundation.NSMetadataQueryDidFinishGatheringNotification, str
            )
