from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter

    class TestGKPlayer (TestCase):
        @min_os_level('10.8')
        def testMethods10_8(self):
            self.assertIsInstance(GameCenter.GKPlayer, objc.objc_class)

            self.assertArgIsBlock(GameCenter.GKPlayer.loadPlayersForIdentifiers_withCompletionHandler_, 1, b'v@@')
            self.assertArgIsBlock(GameCenter.GKPlayer.loadPhotoForSize_withCompletionHandler_, 1, b'v@@')

        @expectedFailure
        @min_os_level('10.8')
        def testMethods10_8_fail(self):
            self.assertResultIsBOOL(GameCenter.GKPlayer.isFriend)
            self.assertArgIsBOOL(GameCenter.GKPlayer.setIsFriend_, 0)

        def testConstants(self):
            self.assertEqual(GameCenter.GKPhotoSizeSmall, 0)
            self.assertEqual(GameCenter.GKPhotoSizeNormal, 1)

            self.assertIsInstance(GameCenter.GKPlayerDidChangeNotificationName, unicode)

        @min_os_level('10.8')
        def testConstants(self):
            self.assertIsInstance(GameCenter.GKPlayerAuthenticationDidChangeNotificationName, unicode)


if __name__ == "__main__":
    main()
