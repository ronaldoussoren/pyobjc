from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import Photos


class TestPHContentEditingInput(TestCase):
    @min_os_level("10.11")
    def test_classes(self):
        self.assertIsInstance(Photos.PHContentEditingInput, objc.objc_class)
