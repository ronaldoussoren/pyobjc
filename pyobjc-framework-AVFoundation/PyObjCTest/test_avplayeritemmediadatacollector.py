from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVPlayerItemMediaDataCollector (TestCase):
    @min_sdk_level('10.13')
    def testProtocols(self):
        objc.protocolNamed('AVPlayerItemMetadataCollectorPushDelegate')

if __name__ == "__main__":
    main()
