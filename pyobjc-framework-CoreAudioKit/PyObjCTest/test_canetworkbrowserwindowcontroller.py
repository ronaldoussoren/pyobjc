from PyObjCTools.TestSupport import *

import CoreAudioKit

class TestCANetworkBrowserWindowController (TestCase):
    @min_os_level('10.11')
    def testMethods(self):
        self.assertResultIsBOOL(CoreAudioKit.CANetworkBrowserWindowController.isAVBSupported)

if __name__ == "__main__":
    main()
