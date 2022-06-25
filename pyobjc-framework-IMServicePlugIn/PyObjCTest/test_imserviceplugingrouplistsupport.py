import IMServicePlugIn  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestIMServicePlugInGroupListSupport(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("IMServicePlugInGroupListSupport")
        self.assertProtocolExists("IMServicePlugInGroupListEditingSupport")
        self.assertProtocolExists("IMServicePlugInGroupListOrderingSupport")
        self.assertProtocolExists("IMServicePlugInGroupListAuthorizationSupport")
        self.assertProtocolExists("IMServicePlugInGroupListHandlePictureSupport")
        self.assertProtocolExists("IMServiceApplicationGroupListSupport")
        self.assertProtocolExists("IMServiceApplicationGroupListAuthorizationSupport")
