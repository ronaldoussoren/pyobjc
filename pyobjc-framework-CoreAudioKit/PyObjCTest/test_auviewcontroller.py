import CoreAudioKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAUViewController(TestCase):
    @min_os_level("10.13")
    def testMethods(self):
        self.assertArgIsBOOL(
            CoreAudioKit.AUAudioUnitViewConfiguration.initWithWidth_height_hostHasController_,
            2,
        )
        self.assertResultIsBOOL(
            CoreAudioKit.AUAudioUnitViewConfiguration.hostHasController
        )

        self.assertArgIsBlock(
            CoreAudioKit.AUAudioUnit.requestViewControllerWithCompletionHandler_,
            0,
            b"v@",
        )
