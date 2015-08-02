from PyObjCTools.TestSupport import *
import IMServicePlugIn
import objc

class TestIMServicePlugInChatRoomSupport (TestCase):
    def testProtocols(self):
        objc.protocolNamed('IMServicePlugInChatRoomSupport')
        objc.protocolNamed('IMServiceApplicationChatRoomSupport')

if __name__ == "__main__":
    main()
