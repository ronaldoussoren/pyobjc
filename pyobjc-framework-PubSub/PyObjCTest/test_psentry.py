import PubSub
from PyObjCTools.TestSupport import TestCase


class TestPSEntry(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(PubSub.PSEntry.isCurrent)
        self.assertResultIsBOOL(PubSub.PSEntry.isRead)
        self.assertArgIsBOOL(PubSub.PSEntry.setRead_, 0)
        self.assertResultIsBOOL(PubSub.PSEntry.isFlagged)
        self.assertArgIsBOOL(PubSub.PSEntry.setFlagged_, 0)
