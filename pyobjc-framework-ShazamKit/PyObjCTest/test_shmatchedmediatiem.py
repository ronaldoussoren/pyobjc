from PyObjCTools.TestSupport import TestCase
import ShazamKit


class TestSHMatchedMediaItem(TestCase):
    def test_constants(self):
        self.assertIsInstance(ShazamKit.SHMediaItemMatchOffset, str)
        self.assertIsInstance(ShazamKit.SHMediaItemFrequencySkew, str)

    def test_classes(self):
        ShazamKit.SHMatchedMediaItem
