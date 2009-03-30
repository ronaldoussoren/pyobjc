from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSPortCoder (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSPortCoder.isBycopy)
        self.failUnlessResultIsBOOL(NSPortCoder.isByref)

if __name__ == "__main__":
    main()
