import IMServicePlugIn  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestIMServicePlugInChatRoomSupport(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("IMServicePlugInChatRoomSupport")
        self.assertProtocolExists("IMServiceApplicationChatRoomSupport")
