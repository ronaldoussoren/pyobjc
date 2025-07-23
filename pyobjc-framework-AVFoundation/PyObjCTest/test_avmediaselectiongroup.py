import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVMediaSelectionGroup(TestCase):
    @min_os_level("10.8")
    def test_methods(self):
        self.assertResultIsBOOL(AVFoundation.AVMediaSelectionGroup.allowsEmptySelection)

        self.assertResultIsBOOL(
            AVFoundation.AVMediaSelectionOption.hasMediaCharacteristic_
        )
        self.assertResultIsBOOL(AVFoundation.AVMediaSelectionOption.isPlayable)

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCustomMediaSelectionScheme.shouldOfferLanguageSelection
        )
