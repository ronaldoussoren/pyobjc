from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import MediaLibrary


class TestMLMediaSource(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(MediaLibrary.MLMediaSource, objc.objc_class)
