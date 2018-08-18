from PyObjCTools.TestSupport import *

import CoreAudioKit

class TestCANetworkBrowserWindowController (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(CoreAudioKit.CANetworkBrowserWindowController.isAVBSupported)

if __name__ == "__main__":
    main()
