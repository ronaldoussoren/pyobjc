from PyObjCTools.TestSupport import *
import IMServicePlugIn
import objc

class TestIMServicePlugInPresenceSupport (TestCase):
    def testProtocols(self):
        objc.protocolNamed('IMServicePlugInPresenceSupport')

if __name__ == "__main__":
    main()
