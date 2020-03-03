import AVFoundation  # noqa: F401
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestAVPlayerItemMediaDataCollector(TestCase):
    @min_sdk_level("10.13")
    def testProtocols(self):
        objc.protocolNamed("AVPlayerItemMetadataCollectorPushDelegate")
