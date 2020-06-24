import IMServicePlugIn  # noqa: F401
from PyObjCTools.TestSupport import TestCase
import objc


class TestIMServicePlugInPresenceSupport(TestCase):
    def testProtocols(self):
        objc.protocolNamed("IMServicePlugInPresenceSupport")
