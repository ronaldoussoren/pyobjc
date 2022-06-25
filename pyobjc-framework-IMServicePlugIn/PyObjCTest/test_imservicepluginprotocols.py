import IMServicePlugIn
from PyObjCTools.TestSupport import TestCase


class TestIMServicePlugInProtocolsHelper(IMServicePlugIn.NSObject):
    def plugInDidLogOutWithError_reconnect_(self, p, r):
        pass


class TestIMServicePlugInProtocols(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("IMServicePlugIn")
        self.assertProtocolExists("IMServiceApplication")

        self.assertArgIsBOOL(
            TestIMServicePlugInProtocolsHelper.plugInDidLogOutWithError_reconnect_, 1
        )
