import PubSub
from PyObjCTools.TestSupport import TestCase


class TestPSClient(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(PubSub.PSClient.addFeed_)
        self.assertResultIsBOOL(PubSub.PSClient.removeFeed_)
        self.assertResultIsBOOL(PubSub.PSClient.isPrivate)
        self.assertArgIsBOOL(PubSub.PSClient.setPrivate_, 0)
