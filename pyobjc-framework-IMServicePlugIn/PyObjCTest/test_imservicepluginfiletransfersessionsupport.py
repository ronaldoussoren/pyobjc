from PyObjCTools.TestSupport import *
import IMServicePlugIn
import objc

class TestIMServicePlugInChatRoomSupport (TestCase):
    def testProtocols(self):
        objc.protocolNamed('IMServicePlugInFileTransferSessionSupport')
        objc.protocolNamed('IMServiceApplicationFileTransferSessionSupport')

if __name__ == "__main__":
    main()
