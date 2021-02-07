from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import MediaLibrary


class TestMLMediaGroup(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(MediaLibrary.MLMediaGroup, objc.objc_class)
