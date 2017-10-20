from PyObjCTools.TestSupport import *

import GameKit

class TestGKPlayerHelper (GameKit.GKPlayer):
    def isFriend(self): return 1

class TestGKPlayer (TestCase):
    def testConstants(self):
        self.assertEqual(GameKit.GKPhotoSizeSmall, 0)
        self.assertEqual(GameKit.GKPhotoSizeNormal, 1)

    def testMethods(self):
        self.assertArgIsBlock(GameKit.GKPlayer.loadPlayersForIdentifiers_withCompletionHandler_, 1, b'v@@')

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertArgIsBlock(GameKit.GKPlayer.loadPhotoForSize_withCompletionHandler_, 1, b'v@@')

        self.assertResultIsBOOL(TestGKPlayerHelper.isFriend)


if __name__ == "__main__":
    main()
