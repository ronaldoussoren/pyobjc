from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import MediaLibrary


class TestMLMediaObject(TestCase):
    @min_os_level("10.9")
    def test_classes(self):
        self.assertIsInstance(MediaLibrary.MLMediaObject, objc.objc_class)
