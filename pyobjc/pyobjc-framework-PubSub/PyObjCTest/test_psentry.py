
from PyObjCTools.TestSupport import *
from PubSub import *

class TestPSEntry (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(PSEntry.isCurrent)
        self.failUnlessResultIsBOOL(PSEntry.isRead)
        self.failUnlessArgIsBOOL(PSEntry.setRead_, 0)
        self.failUnlessResultIsBOOL(PSEntry.isFlagged)
        self.failUnlessArgIsBOOL(PSEntry.setFlagged_, 0)

if __name__ == "__main__":
    main()
