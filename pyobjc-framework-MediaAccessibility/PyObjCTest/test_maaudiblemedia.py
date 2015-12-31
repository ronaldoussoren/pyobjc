import sys
from PyObjCTools.TestSupport import *


import MediaAccessibility

class TestMAAudibleMedia (TestCase):
    @min_os_level("10.10")
    def testFunctions10_10(self):
        self.assertResultIsCFRetained(MediaAccessibility.MAAudibleMediaCopyPreferredCharacteristics)

        a = MediaAccessibility.MAAudibleMediaCopyPreferredCharacteristics()
        self.assertIsInstance(a, (MediaAccessibility.NSArray, type(None)))

    @expectedFailureIf(os_release() == '10.9')
    @min_os_level("10.9")
    def test_constants(self):
        # Present in headers, but not actually exported?
        self.assertIsInstance(MediaAccessibility.kMAAudibleMediaSettingsChangedNotification, unicode)

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(MediaAccessibility.MAMediaCharacteristicDescribesVideoForAccessibility, unicode)


if __name__ == "__main__":
    main()
