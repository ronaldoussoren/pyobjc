from PyObjCTools.TestSupport import *
import IMServicePlugIn
import objc

class TestIMServicePlugInInstantMessageSupport (TestCase):
    def testProtocols(self):
        objc.protocolNamed('IMServicePlugInInstantMessagingSupport')
        objc.protocolNamed('IMServiceApplicationInstantMessagingSupport')

if __name__ == "__main__":
    main()
