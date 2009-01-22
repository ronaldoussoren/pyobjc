
from PyObjCTools.TestSupport import *
from XgridFoundation import *

class TestXGFile (TestCase):
    def testConstants(self):
        self.failUnlessEqual(XGFileTypeNone, 0)
        self.failUnlessEqual(XGFileTypeRegular, 1)
        self.failUnlessEqual(XGFileTypeStream, 2)
        self.failUnlessIsInstance(XGFileStandardOutputPath, unicode)
        self.failUnlessIsInstance(XGFileStandardErrorPath, unicode)

if __name__ == "__main__":
    main()
