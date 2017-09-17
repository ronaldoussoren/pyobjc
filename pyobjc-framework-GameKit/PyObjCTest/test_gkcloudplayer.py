from PyObjCTools.TestSupport import *

import GameKit

class TestGKCloudPlayer (TestCase):
    @min_os_level('10.12')
    def testMethods(self):
        self.assertArgIsBlock(GameKit.GKCloudPlayer.getCurrentSignedInPlayerForContainer_completionHandler_, 1, b'v@@')

if __name__ == "__main__":
    main()
