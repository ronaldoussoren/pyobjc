from PyObjCTools.TestSupport import *

from ImageCaptureCore import *


class TestICScannerBandData (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(ICScannerBandData.isBigEndian)

if __name__ == "__main__":
    main()
