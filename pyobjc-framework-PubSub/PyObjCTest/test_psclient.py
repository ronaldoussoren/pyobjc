
from PyObjCTools.TestSupport import *
from PubSub import *

class TestPSClient (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(PSClient.addFeed_)
        self.assertResultIsBOOL(PSClient.removeFeed_)
        self.assertResultIsBOOL(PSClient.isPrivate)
        self.assertArgIsBOOL(PSClient.setPrivate_, 0)

if __name__ == "__main__":
    main()
