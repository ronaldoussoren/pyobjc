from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSProxy (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSProxy.respondsToSelector_)

if __name__ == "__main__":
    main()
