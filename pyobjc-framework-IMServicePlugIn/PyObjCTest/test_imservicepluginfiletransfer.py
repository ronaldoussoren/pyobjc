import IMServicePlugIn
from PyObjCTools.TestSupport import TestCase, expectedFailure
import objc


class TestIMServicePlugInFileTransfer(TestCase):
    @expectedFailure  # Class are likely part of the host application
    def testClasses(self):
        self.assertIsInstance(
            IMServicePlugIn.IMServicePlugInFileTransfer, objc.objc_class
        )
        self.assertIsInstance(
            IMServicePlugIn.IMServicePlugInOutgoingFileTransfer, objc.objc_class
        )
        self.assertIsInstance(
            IMServicePlugIn.IMServicePlugInIncomingFileTransfer, objc.objc_class
        )
