from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSDistributedLock (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSDistributedLock.tryLock)

if __name__ == "__main__":
    main()
