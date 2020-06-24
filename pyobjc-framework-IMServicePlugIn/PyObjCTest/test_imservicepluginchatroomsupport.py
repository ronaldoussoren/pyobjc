import IMServicePlugIn  # noqa: F401
from PyObjCTools.TestSupport import TestCase
import objc


class TestIMServicePlugInChatRoomSupport(TestCase):
    def testProtocols(self):
        objc.protocolNamed("IMServicePlugInChatRoomSupport")
        objc.protocolNamed("IMServiceApplicationChatRoomSupport")
