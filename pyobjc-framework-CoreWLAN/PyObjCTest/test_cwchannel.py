from PyObjCTools.TestSupport import *

import CoreWLAN

class TestCWChannel (TestCase):
    @min_os_level('10.6')
    def testMethods(self):
        self.assertResultIsBOOL(CoreWLAN.CWChannel.isEqualToChannel_)

if __name__ == "__main__":
    main()
