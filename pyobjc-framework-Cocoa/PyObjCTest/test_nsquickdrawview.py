
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSQuickDrawView (TestCase):
    @onlyOn32Bit
    def testMethods(self):
        self.fail("qdPort")

if __name__ == "__main__":
    main()
