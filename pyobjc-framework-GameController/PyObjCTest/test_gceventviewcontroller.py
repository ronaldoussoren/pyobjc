import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import GameController

    class TestGCEventViewController(TestCase):
        @min_os_level("10.15")
        def test_methods10_15(self):
            self.assertResultIsBOOL(
                GameController.GCEventViewController.controllerUserInteractionEnabled
            )
            self.assertArgIsBOOL(
                GameController.GCEventViewController.setControllerUserInteractionEnabled_,
                0,
            )


if __name__ == "__main__":
    main()
