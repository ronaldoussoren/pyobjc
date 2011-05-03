from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSProxy (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSProxy.respondsToSelector_)

if __name__ == "__main__":
    main()
