from PyObjCTools.TestSupport import TestCase, min_os_level
import ShazamKit


class TestSHMediaItem(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(ShazamKit.SHMediaItemProperty, str)

    def test_constants(self):
        self.assertIsInstance(ShazamKit.SHMediaItemShazamID, str)
        self.assertIsInstance(ShazamKit.SHMediaItemTitle, str)
        self.assertIsInstance(ShazamKit.SHMediaItemSubtitle, str)
        self.assertIsInstance(ShazamKit.SHMediaItemArtist, str)
        self.assertIsInstance(ShazamKit.SHMediaItemWebURL, str)
        self.assertIsInstance(ShazamKit.SHMediaItemAppleMusicID, str)
        self.assertIsInstance(ShazamKit.SHMediaItemAppleMusicURL, str)
        self.assertIsInstance(ShazamKit.SHMediaItemArtworkURL, str)
        self.assertIsInstance(ShazamKit.SHMediaItemVideoURL, str)
        self.assertIsInstance(ShazamKit.SHMediaItemExplicitContent, str)
        self.assertIsInstance(ShazamKit.SHMediaItemGenres, str)
        self.assertIsInstance(ShazamKit.SHMediaItemISRC, str)

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(ShazamKit.SHMediaItemCreationDate, str)

    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(ShazamKit.SHMediaItemTimeRanges, str)
        self.assertIsInstance(ShazamKit.SHMediaItemFrequencySkewRanges, str)

    def test_classes(self):
        ShazamKit.SHMediaItem

    def test_methods(self):
        self.assertArgIsBlock(
            ShazamKit.SHMediaItem.fetchMediaItemWithShazamID_completionHandler_,
            1,
            b"v@@",
        )

        # XXX: Check that __getitem__ is available and works
        # XXX: unavailable: -init, +new
