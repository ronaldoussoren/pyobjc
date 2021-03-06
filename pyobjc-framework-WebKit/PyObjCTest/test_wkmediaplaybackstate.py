from PyObjCTools.TestSupport import TestCase
import WebKit


class TestWKMediaPlaybackStat(TestCase):
    def test_constants(self):
        self.assertEqual(WebKit.WKMediaPlaybackStateNone, 0)
        self.assertEqual(WebKit.WKMediaPlaybackStatePaused, 1)
        self.assertEqual(WebKit.WKMediaPlaybackStateSuspended, 2)
        self.assertEqual(WebKit.WKMediaPlaybackStatePlaying, 3)
