from PyObjCTools.TestSupport import *
from AppKit import *

NSStoryboardControllerCreator = b"@@"


class TestNSStoryboard(TestCase):
    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsBlock(
            NSStoryboard.instantiateInitialControllerWithCreator_,
            0,
            NSStoryboardControllerCreator,
        )
        self.assertArgIsBlock(
            NSStoryboard.instantiateControllerWithIdentifier_creator_,
            1,
            NSStoryboardControllerCreator,
        )


if __name__ == "__main__":
    main()
