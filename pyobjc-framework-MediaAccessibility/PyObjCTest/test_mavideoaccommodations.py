import MediaAccessibility
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMAVideoAccommodations(TestCase):
    @min_os_level("13.3")
    def test_constants(self):
        self.assertIsInstance(
            MediaAccessibility.kMADimFlashingLightsChangedNotification, str
        )

    @min_os_level("13.3")
    def test_functions(self):
        MediaAccessibility.MADimFlashingLightsEnabled
