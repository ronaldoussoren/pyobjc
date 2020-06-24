import MediaAccessibility
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMAAudibleMedia(TestCase):
    @min_os_level("10.10")
    def testFunctions10_10(self):
        self.assertResultIsCFRetained(
            MediaAccessibility.MAAudibleMediaCopyPreferredCharacteristics
        )

        a = MediaAccessibility.MAAudibleMediaCopyPreferredCharacteristics()
        self.assertIsInstance(a, (MediaAccessibility.NSArray, type(None)))

    @min_os_level("10.10")
    def test_constants(self):
        self.assertIsInstance(
            MediaAccessibility.kMAAudibleMediaSettingsChangedNotification, str
        )

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(
            MediaAccessibility.MAMediaCharacteristicDescribesVideoForAccessibility, str
        )
