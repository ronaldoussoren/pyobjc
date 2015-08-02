from PyObjCTools.TestSupport import *
import IMServicePlugIn
import objc

class TestIMServicePlugInFileTransferSession (TestCase):

    @expectedFailure # Class is probably part of the host application
    def testClasses(self):
        self.assertIsInstance(IMServicePlugIn.IMServicePlugInFileTransferSession, objc.objc_class)
        self.assertIsInstance(IMServicePlugIn.IMServicePlugInOutgoingFileTransferSession, objc.objc_class)
        self.assertIsInstance(IMServicePlugIn.IMServicePlugInIncomingFileTransferSession, objc.objc_class)

if __name__ == "__main__":
    main()
