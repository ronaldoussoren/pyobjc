from PyObjCTools.TestSupport import *
import IMServicePlugIn
import objc

class TestIMServicePlugInProtocolsHelper (IMServicePlugIn.NSObject):
    def plugInDidLogOutWithError_reconnect_(self, p, r): pass

class TestIMServicePlugInProtocols (TestCase):
    def testProtocols(self):
        objc.protocolNamed('IMServicePlugIn')
        objc.protocolNamed('IMServiceApplication')

        self.assertArgIsBOOL(TestIMServicePlugInProtocolsHelper.plugInDidLogOutWithError_reconnect_, 1)

if __name__ == "__main__":
    main()
