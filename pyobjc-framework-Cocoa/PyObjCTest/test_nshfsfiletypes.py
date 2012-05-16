from PyObjCTools.TestSupport import *
import os

from Foundation import *


class TestNSHFSFileTypes (TestCase):
    def testFunctions(self):
        v = NSHFSTypeCodeFromFileType("'rtfd'")
        self.assertIsInstance(v, (int, long))
        w = NSFileTypeForHFSTypeCode(v)
        self.assertIsInstance(w, unicode)
        self.assertEqual(w, u"'rtfd'")
           
        fname = '/Library/Documentation/Acknowledgements.rtf'
        if not os.path.exists(fname):
            fname = '/Library/Documentation/AirPort Acknowledgements.rtf'

        if not os.path.exists(fname):
            self.fail("test file doesn't exist")

        v = NSHFSTypeOfFile(fname)
        self.assertIsInstance(v, unicode)

if __name__ == "__main__":
    main()
