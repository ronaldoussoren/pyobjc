import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVMetadataItem(TestCase):
    @min_os_level("10.7")
    def test_methods(self):
        self.assertArgIsOut(AVFoundation.AVMetadataItem.statusOfValueForKey_error_, 1)

        self.assertArgIsBlock(
            AVFoundation.AVMetadataItem.loadValuesAsynchronouslyForKeys_completionHandler_,  # noqa: B950
            1,
            b"v",
        )

    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertArgIsBlock(
            AVFoundation.AVMetadataItem.metadataItemWithPropertiesOfMetadataItem_valueLoadingHandler_,  # noqa: B950
            1,
            b"v@",
        )
