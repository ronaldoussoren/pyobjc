from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSGarbageCollector (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSGarbageCollector.isCollecting)
        self.failUnlessResultIsBOOL(NSGarbageCollector.isEnabled)


if __name__ == "__main__":
    main()
