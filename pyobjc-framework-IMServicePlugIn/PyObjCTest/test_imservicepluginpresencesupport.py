import IMServicePlugIn  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestIMServicePlugInPresenceSupport(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("IMServicePlugInPresenceSupport")
