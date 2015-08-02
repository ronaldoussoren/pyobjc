from PyObjCTools.TestSupport import *
import IMServicePlugIn
import objc

class TestIMServicePlugInFileTransfer (TestCase):
    @expectedFailure # Class is likely part of the host application
    def testClasses(self):
        self.assertIsInstance(IMServicePlugIn.IMServicePlugInMessage, objc.objc_class)

if __name__ == "__main__":
    main()
