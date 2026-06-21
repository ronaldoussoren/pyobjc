from PyObjCTools.TestSupport import TestCase, min_os_level
import GameController


class TestGCPhysicalInputProfile(TestCase):
    @min_os_level("12.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            GameController.GCPhysicalInputProfile.hasRemappedElements
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBlock(
            GameController.GCPhysicalInputProfile.valueDidChangeHandler, b"v@@"
        )
        self.assertArgIsBlock(
            GameController.GCPhysicalInputProfile.setValueDidChangeHandler_, 0, b"v@@"
        )
