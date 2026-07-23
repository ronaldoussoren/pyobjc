import os

import Foundation
from PyObjCTools.TestSupport import TestCase, fourcc


class TestNSHFSFileTypes(TestCase):
    def test_functions(self):
        v = Foundation.NSHFSTypeCodeFromFileType("'rtfd'")
        self.assertIsInstance(v, int)

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 0"):
            Foundation.NSFileTypeForHFSTypeCode()

        w = Foundation.NSFileTypeForHFSTypeCode(v)
        self.assertIsInstance(w, str)
        self.assertEqual(w, "'rtfd'")

        with self.assertRaises(OverflowError):
            Foundation.NSFileTypeForHFSTypeCode(2**128)

        with self.assertRaisesRegex(
            TypeError, "OSType arg must be byte string of 4 chars"
        ):
            Foundation.NSFileTypeForHFSTypeCode("pypi")

        w = Foundation.NSFileTypeForHFSTypeCode(fourcc(b"pypi"))
        self.assertEqual(w, "'pypi'")

        w = Foundation.NSFileTypeForHFSTypeCode(b"pypi")
        self.assertEqual(w, "'pypi'")

        fname = "/Library/Documentation/Acknowledgements.rtf"
        if not os.path.exists(fname):
            fname = "/Library/Documentation/AirPort Acknowledgements.rtf"
        if not os.path.exists(fname):
            fname = "/Library/Documentation//iPod/Acknowledgements.rtf"

        if not os.path.exists(fname):
            self.fail("test file doesn't exist")

        v = Foundation.NSHFSTypeOfFile(fname)
        self.assertIsInstance(v, str)
