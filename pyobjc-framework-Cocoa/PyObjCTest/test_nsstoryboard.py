import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level

NSStoryboardControllerCreator = b"@@"


class TestNSStoryboard(TestCase):
    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsBlock(
            AppKit.NSStoryboard.instantiateInitialControllerWithCreator_,
            0,
            NSStoryboardControllerCreator,
        )
        self.assertArgIsBlock(
            AppKit.NSStoryboard.instantiateControllerWithIdentifier_creator_,
            1,
            NSStoryboardControllerCreator,
        )
