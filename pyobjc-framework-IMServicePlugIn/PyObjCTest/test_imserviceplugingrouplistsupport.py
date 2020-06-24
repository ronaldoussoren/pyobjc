import IMServicePlugIn  # noqa: F401
from PyObjCTools.TestSupport import TestCase
import objc


class TestIMServicePlugInGroupListSupport(TestCase):
    def testProtocols(self):
        objc.protocolNamed("IMServicePlugInGroupListSupport")
        objc.protocolNamed("IMServicePlugInGroupListEditingSupport")
        objc.protocolNamed("IMServicePlugInGroupListOrderingSupport")
        objc.protocolNamed("IMServicePlugInGroupListAuthorizationSupport")
        objc.protocolNamed("IMServicePlugInGroupListHandlePictureSupport")
        objc.protocolNamed("IMServiceApplicationGroupListSupport")
        objc.protocolNamed("IMServiceApplicationGroupListAuthorizationSupport")
