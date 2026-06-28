import objc
from PyObjCTools.TestSupport import TestCase

import GameCenter


class TestGKPlayer(TestCase):
    def test_methods(self):
        self.assertIsInstance(GameCenter.GKPlayer, objc.objc_class)

        self.assertArgIsBlock(
            GameCenter.GKPlayer.loadPlayersForIdentifiers_withCompletionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameCenter.GKPlayer.loadPhotoForSize_withCompletionHandler_, 1, b"v@@"
        )

        self.assertResultIsBOOL(GameCenter.GKPlayer().isFriend)

    def test_constants(self):
        self.assertEqual(GameCenter.GKPhotoSizeSmall, 0)
        self.assertEqual(GameCenter.GKPhotoSizeNormal, 1)

        self.assertIsInstance(GameCenter.GKPlayerDidChangeNotificationName, str)

        self.assertIsInstance(
            GameCenter.GKPlayerAuthenticationDidChangeNotificationName, str
        )
