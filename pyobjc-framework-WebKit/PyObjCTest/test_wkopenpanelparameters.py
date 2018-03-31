from PyObjCTools.TestSupport import *
from WebKit import *


class TestWKOpenPanelParameters (TestCase):
    @onlyOn64Bit
    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(WKOpenPanelParameters.allowsMultipleSelection)

    @onlyOn64Bit
    @min_os_level('10.13.4')
    def testMethods10_13_4(self):
        self.assertResultIsBOOL(WKOpenPanelParameters.allowsDirectories)

if __name__ == "__main__":
    main()
