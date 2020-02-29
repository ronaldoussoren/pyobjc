import IMServicePlugIn
import objc
from PyObjCTools.TestSupport import *


class TestIMServicePlugInChatRoomSupport(TestCase):
    def testProtocols(self):
        objc.protocolNamed("IMServicePlugInFileTransferSessionSupport")
        objc.protocolNamed("IMServiceApplicationFileTransferSessionSupport")


if __name__ == "__main__":
    main()
