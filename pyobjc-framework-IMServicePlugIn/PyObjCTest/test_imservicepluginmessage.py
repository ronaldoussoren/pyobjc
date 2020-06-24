import IMServicePlugIn
from PyObjCTools.TestSupport import TestCase, expectedFailure
import objc


class TestIMServicePlugInFileTransfer(TestCase):
    @expectedFailure  # Class is likely part of the host application
    def testClasses(self):
        self.assertIsInstance(IMServicePlugIn.IMServicePlugInMessage, objc.objc_class)
