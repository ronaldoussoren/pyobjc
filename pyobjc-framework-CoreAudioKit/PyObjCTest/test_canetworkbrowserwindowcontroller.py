import CoreAudioKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCANetworkBrowserWindowController(TestCase):
    @min_os_level("10.11")
    def testMethods(self):
        self.assertResultIsBOOL(
            CoreAudioKit.CANetworkBrowserWindowController.isAVBSupported
        )
