from PyObjCTools.TestSupport import *
from Foundation import NSNull

class TestNSNull (TestCase):
    def testBool(self):
        v = NSNull.null()
        self.assert_(not v)
        self.assert_(v is not None)

if __name__ == "__main__":
    main()
