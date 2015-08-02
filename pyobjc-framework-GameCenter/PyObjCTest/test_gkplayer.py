from PyObjCTools.TestSupport import *
import objc
import sys

try:
    unicode
except NameError:
    unicode = str

if sys.maxsize > 2 ** 32:
    import GameCenter

    class TestGKPlayer (TestCase):
        @min_os_level('10.8')
        def testMethods10_8(self):
            self.assertIsInstance(GameCenter.GKPlayer, objc.objc_class)

            self.assertArgIsBlock(GameCenter.GKPlayer.loadPlayersForIdentifiers_withCompletionHandler_, 1, b'v@@')
            self.assertArgIsBlock(GameCenter.GKPlayer.loadPhotoForSize_withCompletionHandler_, 1, b'v@@')

            self.assertResultIsBOOL(GameCenter.GKPlayer.isFriend)
            self.assertArgIsBOOL(GameCenter.GKPlayer.setIsFriend_, 0)

        def testConstants(self):
            self.assertEqual(GameCenter.GKPhotoSizeSmall, 0)
            self.assertEqual(GameCenter.GKPhotoSizeNormal, 1)

            self.assertIsInstance(GameCenter.GKPlayerDidChangeNotificationName, unicode)

        @min_os_level('10.10')
        def testMethods10_10(self):
            self.assertResultIsBlock(GameCenter.GKPlayer.loadFriendPlayersWithCompletionHandler_, 0, b'v@@')
            self.assertResultIsBlock(GameCenter.GKPlayer.setDefaultLeaderboardIdentifier_completionHandler_, 1, b'v@')
            self.assertResultIsBlock(GameCenter.GKPlayer.loadDefaultLeaderboardIdentifierWithCompletionHandler_, 0, b'v@@')
            self.assertResultIsBlock(GameCenter.GKPlayer.generateIdentityVerificationSignatureWithCompletionHandler_, 0, b'v@@@Q@')

        @min_os_level('10.8')
        def testConstants(self):
            self.assertIsInstance(GameCenter.GKPlayerAuthenticationDidChangeNotificationName, unicode)


if __name__ == "__main__":
    main()
