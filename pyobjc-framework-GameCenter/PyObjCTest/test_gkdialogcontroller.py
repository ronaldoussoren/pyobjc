from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter
    import objc

    class TestGKDialogController (TestCase):
        @min_os_level('10.8')
        def testClasses10_8(self):
            self.assertIsInstance(GameCenter.GKDialogController, objc.objc_class)

            self.assertResultIsBOOL(GameCenter.GKDialogController.presentViewController_)

        @min_os_level('10.8')
        def testProtocols10_8(self):
            objc.protocolNamed('GKViewController')

if __name__ == "__main__":
    main()
