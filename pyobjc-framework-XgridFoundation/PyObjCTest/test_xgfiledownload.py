
from PyObjCTools.TestSupport import *
from XgridFoundation import *

class TestXGFileDownload (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(XGFileDownload.setDestination_allowOverwrite_, 1)

    def testProtocols(self):
        self.assertIsInstance(protocols.XGFileDownloadDelegate, objc.informal_protocol)


if __name__ == "__main__":
    main()
