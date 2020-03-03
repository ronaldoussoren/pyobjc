import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVMediaSelectionGroup(TestCase):
    @min_os_level("10.8")
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVMediaSelectionGroup.allowsEmptySelection)

        self.assertResultIsBOOL(
            AVFoundation.AVMediaSelectionOption.hasMediaCharacteristic_
        )
        self.assertResultIsBOOL(AVFoundation.AVMediaSelectionOption.isPlayable)
