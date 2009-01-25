
from PyObjCTools.TestSupport import *
from PubSub import *

class TestPSClient (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(PSClient.addFeed_)
        self.failUnlessResultIsBOOL(PSClient.removeFeed_)
        self.failUnlessResultIsBOOL(PSClient.isPrivate)
        self.failUnlessArgIsBOOL(PSClient.setPrivate_, 0)

if __name__ == "__main__":
    main()
