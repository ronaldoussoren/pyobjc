from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSHFSFileTypes (TestCase):
    def testFunctions(self):
        v = NSHFSTypeCodeFromFileType("'rtfd'")
        self.assertIsInstance(v, (int, long))
        w = NSFileTypeForHFSTypeCode(v)
        self.assertIsInstance(w, unicode)
        self.assertEqual(w, u"'rtfd'")
           
        v = NSHFSTypeOfFile('/Library/Documentation/Acknowledgements.rtf')
        self.assertIsInstance(v, unicode)
if __name__ == "__main__":
    main()
