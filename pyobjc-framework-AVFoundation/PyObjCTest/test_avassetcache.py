from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAssetCache (TestCase):
    @min_os_level('10.12')
    def testClasses(self):
        AVFoundation.AVAssetCache

    @min_os_level('10.12')
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetCache.isPlayableOffline)


if __name__ == "__main__":
    main()
