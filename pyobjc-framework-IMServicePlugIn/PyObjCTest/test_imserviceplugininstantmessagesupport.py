import IMServicePlugIn  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestIMServicePlugInInstantMessageSupport(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("IMServicePlugInInstantMessagingSupport")
        self.assertProtocolExists("IMServiceApplicationInstantMessagingSupport")
