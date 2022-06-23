import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVGeometry(TestCase):
    @min_os_level("13.0")
    def test_funcdtions(self):
        AVFoundation.AVMakeRectWithAspectRatioInsideRect
