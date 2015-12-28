
from PyObjCTools.TestSupport import *
from XgridFoundation import *

class TestXGFileDownload (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(XGFileDownload.setDestination_allowOverwrite_, 1)


if __name__ == "__main__":
    main()
