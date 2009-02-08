
from PyObjCTools.TestSupport import *
from CoreText import *

class TestCoreText (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kCTVersionNumber10_5, 0x00020000)

    def testFunctions(self):
        v = CTGetCoreTextVersion()
        self.failUnlessIsInstance(v, (int, long))

if __name__ == "__main__":
    main()
