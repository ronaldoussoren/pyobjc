from PyObjCTools.TestSupport import TestCase, min_os_level
import QTKit


class TestQTCaptureDecompressedVideoOutput(TestCase):
    @min_os_level("10.6")
    def test_methods(self):
        o = QTKit.QTCaptureDecompressedVideoOutput.alloc().init()
        self.assertResultIsBOOL(o.automaticallyDropsLateVideoFrames)
        self.assertArgIsBOOL(o.setAutomaticallyDropsLateVideoFrames_, 0)
