from PyObjCTools.TestSupport import *

import DiscRecording

class TestDRErase (TestCase):
    def testConstants(self):
        self.assertIsInstance(DiscRecording.DREraseTypeKey, unicode)
        self.assertIsInstance(DiscRecording.DREraseTypeQuick, unicode)
        self.assertIsInstance(DiscRecording.DREraseTypeComplete, unicode)
        self.assertIsInstance(DiscRecording.DREraseStatusChangedNotification, unicode)


if __name__ == "__main__":
    main()
