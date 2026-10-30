import GameKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestGKPlayer(TestCase):
    def test_enums(self):
        self.assertIsEnumType(GameKit.GKPhotoSize)
        self.assertEqual(GameKit.GKPhotoSizeSmall, 0)
        self.assertEqual(GameKit.GKPhotoSizeNormal, 1)

    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(GameKit.GKPlayerIDNoLongerAvailable, str)

    def test_methods(self):
        self.assertArgIsBlock(
            GameKit.GKPlayer.loadPlayersForIdentifiers_withCompletionHandler_, 1, b"v@@"
        )

        self.assertArgIsBlock(
            GameKit.GKPlayer.loadPhotoForSize_withCompletionHandler_, 1, b"v@@"
        )

        self.assertResultIsBOOL(GameKit.GKPlayer().isFriend)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(GameKit.GKPlayer.scopedIDsArePersistent)

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(GameKit.GKPlayer.isInvitable)
