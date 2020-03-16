from PyObjCTools.TestSupport import TestCase
import XgridFoundation


class TestXGFileDownload(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(XgridFoundation.XGFileDownload.setDestination_allowOverwrite_, 1)
