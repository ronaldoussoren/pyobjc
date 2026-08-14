import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVTimedMetadataGroup(TestCase):
    @min_os_level("10.10")
    def test_methods(self):
        self.assertResultIsCFRetained(
            AVFoundation.AVTimedMetadataGroup.copyFormatDescription
        )
