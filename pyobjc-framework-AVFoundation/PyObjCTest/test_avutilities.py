import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVUtilities(TestCase):
    @min_os_level("10.7")
    def test_functions(self):
        AVFoundation.AVMakeRectWithAspectRatioInsideRect  # No further testing needed
