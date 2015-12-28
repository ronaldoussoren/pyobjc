
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTCaptureDecompressedVideoOutput (TestCase):

    @min_os_level('10.6')
    def test_methods(self):
        o = QTCaptureDecompressedVideoOutput.alloc().init()
        self.assertResultIsBOOL(o.automaticallyDropsLateVideoFrames)
        self.assertArgIsBOOL(o.setAutomaticallyDropsLateVideoFrames_, 0)

if __name__ == "__main__":
    main()
