from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSHFSFileTypes (TestCase):
    def testFunctions(self):
        v = NSHFSTypeCodeFromFileType("'rtfd'")
        self.failUnless(isinstance(v, (int, long)))

        w = NSFileTypeForHFSTypeCode(v)
        self.failUnless(isinstance(w, unicode))
        self.assertEquals(w, u"'rtfd'")
           
        v = NSHFSTypeOfFile('/Library/Documentation/Acknowledgements.rtf')
        self.failUnless(isinstance(v, unicode))


if __name__ == "__main__":
    main()
