
from PyObjCTools.TestSupport import *
from PubSub import *

class TestPSEnclosure (TestCase):
    def testConstants(self):
        self.assertEqual(PSEnclosureDownloadIsIdle, 0)
        self.assertEqual(PSEnclosureDownloadIsQueued, 1)
        self.assertEqual(PSEnclosureDownloadIsActive, 2)
        self.assertEqual(PSEnclosureDownloadDidFinish, 3)
        self.assertEqual(PSEnclosureDownloadDidFail, 4)
        self.assertEqual(PSEnclosureDownloadWasDeleted, 5)

        self.assertIsInstance(PSEnclosureDownloadStateDidChangeNotification, unicode)


    def testMethods(self):
        self.assertResultIsBOOL(PSEnclosure.download_)
        self.assertArgIsOut(PSEnclosure.download_, 0)

if __name__ == "__main__":
    main()
