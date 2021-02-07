import IMServicePlugIn  # noqa: F401
from PyObjCTools.TestSupport import TestCase
import objc


class TestIMServicePlugInInstantMessageSupport(TestCase):
    def testProtocols(self):
        objc.protocolNamed("IMServicePlugInInstantMessagingSupport")
        objc.protocolNamed("IMServiceApplicationInstantMessagingSupport")
