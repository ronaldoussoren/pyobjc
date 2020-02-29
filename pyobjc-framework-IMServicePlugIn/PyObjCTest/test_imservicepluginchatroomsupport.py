import IMServicePlugIn
import objc
from PyObjCTools.TestSupport import *


class TestIMServicePlugInChatRoomSupport(TestCase):
    def testProtocols(self):
        objc.protocolNamed("IMServicePlugInChatRoomSupport")
        objc.protocolNamed("IMServiceApplicationChatRoomSupport")


if __name__ == "__main__":
    main()
