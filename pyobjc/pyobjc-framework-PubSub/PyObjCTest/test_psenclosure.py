
from PyObjCTools.TestSupport import *
from PubSub import *

class TestPSEnclosure (TestCase):
    def testConstants(self):
        self.failUnlessEqual(PSEnclosureDownloadIsIdle, 0)
        self.failUnlessEqual(PSEnclosureDownloadIsQueued, 1)
        self.failUnlessEqual(PSEnclosureDownloadIsActive, 2)
        self.failUnlessEqual(PSEnclosureDownloadDidFinish, 3)
        self.failUnlessEqual(PSEnclosureDownloadDidFail, 4)
        self.failUnlessEqual(PSEnclosureDownloadWasDeleted, 5)

        self.failUnlessIsInstance(PSEnclosureDownloadStateDidChangeNotification, unicode)


    def testMethods(self):
        self.failUnlessResultIsBOOL(PSEnclosure.download_)
        self.failUnlessArgIsOut(PSEnclosure.download_, 0)

if __name__ == "__main__":
    main()
