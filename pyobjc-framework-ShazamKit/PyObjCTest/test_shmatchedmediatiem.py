from PyObjCTools.TestSupport import TestCase, min_os_level
import ShazamKit


class TestSHMatchedMediaItem(TestCase):
    def test_constants(self):
        self.assertIsInstance(ShazamKit.SHMediaItemMatchOffset, str)
        self.assertIsInstance(ShazamKit.SHMediaItemFrequencySkew, str)

    @min_os_level("15.4")
    def test_constants15_4(self):
        self.assertIsInstance(ShazamKit.SHMediaItemConfidence, str)

    def test_classes(self):
        ShazamKit.SHMatchedMediaItem
