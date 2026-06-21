import GameKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestGKPlayerHelper(GameKit.GKPlayer):
    def isFriend(self):
        return 1


class TestGKPlayer(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameKit.GKPhotoSize)

    def test_constants(self):
        self.assertEqual(GameKit.GKPhotoSizeSmall, 0)
        self.assertEqual(GameKit.GKPhotoSizeNormal, 1)

    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(GameKit.GKPlayerIDNoLongerAvailable, str)

    def test_methods(self):
        self.assertArgIsBlock(
            GameKit.GKPlayer.loadPlayersForIdentifiers_withCompletionHandler_, 1, b"v@@"
        )

    @min_os_level("10.8")
    def test_methods10_8(self):
        self.assertArgIsBlock(
            GameKit.GKPlayer.loadPhotoForSize_withCompletionHandler_, 1, b"v@@"
        )

        self.assertResultIsBOOL(TestGKPlayerHelper.isFriend)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(GameKit.GKPlayer.scopedIDsArePersistent)

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(GameKit.GKPlayer.isInvitable)
