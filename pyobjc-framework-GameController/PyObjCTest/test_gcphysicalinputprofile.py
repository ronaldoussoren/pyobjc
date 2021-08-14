from PyObjCTools.TestSupport import TestCase, min_os_level
import GameController


class TestGCPhysicalInputProfile(TestCase):
    @min_os_level("12.0")
    def testMethods(self):
        self.assertResultIsBOOL(
            GameController.GCPhysicalInputProfile.hasRemappedElements
        )
