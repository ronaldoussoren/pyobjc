from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVPlayerItemMediaDataCollector (TestCase):
    def testProtocols(self):
        objc.protocolNamed('AVPlayerItemMetadataCollectorPushDelegate')

if __name__ == "__main__":
    main()
