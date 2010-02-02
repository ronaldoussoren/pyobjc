from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSGarbageCollector (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSGarbageCollector.isCollecting)
        self.assertResultIsBOOL(NSGarbageCollector.isEnabled)


if __name__ == "__main__":
    main()
