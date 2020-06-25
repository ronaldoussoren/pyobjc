import os

import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSHFSFileTypes(TestCase):
    def testFunctions(self):
        v = Foundation.NSHFSTypeCodeFromFileType("'rtfd'")
        self.assertIsInstance(v, int)
        w = Foundation.NSFileTypeForHFSTypeCode(v)
        self.assertIsInstance(w, str)
        self.assertEqual(w, "'rtfd'")

        fname = "/Library/Documentation/Acknowledgements.rtf"
        if not os.path.exists(fname):
            fname = "/Library/Documentation/AirPort Acknowledgements.rtf"
        if not os.path.exists(fname):
            fname = "/Library/Documentation//iPod/Acknowledgements.rtf"

        if not os.path.exists(fname):
            self.fail("test file doesn't exist")

        v = Foundation.NSHFSTypeOfFile(fname)
        self.assertIsInstance(v, str)
