
from PyObjCTools.TestSupport import *
from PubSub import *

class TestPSEntry (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(PSEntry.isCurrent)
        self.assertResultIsBOOL(PSEntry.isRead)
        self.assertArgIsBOOL(PSEntry.setRead_, 0)
        self.assertResultIsBOOL(PSEntry.isFlagged)
        self.assertArgIsBOOL(PSEntry.setFlagged_, 0)

if __name__ == "__main__":
    main()
