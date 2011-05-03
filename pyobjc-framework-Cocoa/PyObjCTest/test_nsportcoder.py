from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSPortCoder (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSPortCoder.isBycopy)
        self.assertResultIsBOOL(NSPortCoder.isByref)

if __name__ == "__main__":
    main()
