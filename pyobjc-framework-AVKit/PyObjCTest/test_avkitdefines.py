from PyObjCTools.TestSupport import TestCase

import AVKit


class TestAVKitDefines(TestCase):
    def test_aliases(self):
        self.assertIs(AVKit.AVKitPlatformViewClass, AVKit.NSView)
        self.assertIs(AVKit.AVKitPlatformColorClass, AVKit.NSColor)
