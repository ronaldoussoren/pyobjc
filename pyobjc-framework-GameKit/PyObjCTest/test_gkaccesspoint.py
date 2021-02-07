from PyObjCTools.TestSupport import TestCase, min_os_level
import GameKit


class TestGKAccessPoint(TestCase):
    def test_constants(self):
        self.assertEqual(GameKit.GKAccessPointLocationTopLeading, 0)
        self.assertEqual(GameKit.GKAccessPointLocationTopTrailing, 1)
        self.assertEqual(GameKit.GKAccessPointLocationBottomLeading, 2)
        self.assertEqual(GameKit.GKAccessPointLocationBottomTrailing, 3)

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertResultIsBOOL(GameKit.GKAccessPoint.isActive)
        self.assertArgIsBOOL(GameKit.GKAccessPoint.setActive_, 0)

        self.assertResultIsBOOL(GameKit.GKAccessPoint.isVisible)
        self.assertResultIsBOOL(GameKit.GKAccessPoint.isPresentingGameCenter)

        self.assertResultIsBOOL(GameKit.GKAccessPoint.showHighlights)
        self.assertArgIsBOOL(GameKit.GKAccessPoint.setShowHighlights_, 0)

        self.assertArgIsBlock(
            GameKit.GKAccessPoint.triggerAccessPointWithHandler_, 0, b"v"
        )
        self.assertArgIsBlock(
            GameKit.GKAccessPoint.triggerAccessPointWithState_handler_, 1, b"v"
        )
