from PyObjCTools.TestSupport import TestCase
import ShazamKit


class TestSHMediaLibrary(TestCase):
    def test_classes(self):
        ShazamKit.SHMediaLibrary

    def test_methods(self):
        self.assertArgIsBlock(
            ShazamKit.SHMediaLibrary.addMediaItems_completionHandler_, 1, b"v@"
        )
        # XXX
        # unavailable: -init, +new
