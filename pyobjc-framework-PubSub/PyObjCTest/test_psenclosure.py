import PubSub
from PyObjCTools.TestSupport import TestCase


class TestPSEnclosure(TestCase):
    def testConstants(self):
        self.assertEqual(PubSub.PSEnclosureDownloadIsIdle, 0)
        self.assertEqual(PubSub.PSEnclosureDownloadIsQueued, 1)
        self.assertEqual(PubSub.PSEnclosureDownloadIsActive, 2)
        self.assertEqual(PubSub.PSEnclosureDownloadDidFinish, 3)
        self.assertEqual(PubSub.PSEnclosureDownloadDidFail, 4)
        self.assertEqual(PubSub.PSEnclosureDownloadWasDeleted, 5)

        self.assertIsInstance(PubSub.PSEnclosureDownloadStateDidChangeNotification, str)

    def testMethods(self):
        self.assertResultIsBOOL(PubSub.PSEnclosure.download_)
        self.assertArgIsOut(PubSub.PSEnclosure.download_, 0)
