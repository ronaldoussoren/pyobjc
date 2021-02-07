from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import Photos


class TestPHAdjustmentData(TestCase):
    @min_os_level("10.11")
    def testClasses(self):
        self.assertIsInstance(Photos.PHAdjustmentData, objc.objc_class)
