from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import PhotosUI

    class TestPHContentEditingControllerHelper (NSObject):
        def canHandleAdjustmentData_(self, d): return True
        def finishContentEditingWithCompletionHandler_(self, handler): pass


    class TestPHContentEditingController (TestCase):
        @min_os_level('10.11')
        def testProtocols(self):
            self.assertIsInstance(objc.protocolNamed('PHContentEditingController'), objc.formal_protocol)

        @min_os_level('10.11')
        def testMethods(self):
            self.assertResultIsBOOL(TestPHContentEditingControllerHelper.canHandleAdjustmentData_)
            self.assertArgIsBlock(TestPHContentEditingControllerHelper.finishContentEditingWithCompletionHandler_, 0, b'v@')
            self.assertResultIsBOOL(TestPHContentEditingControllerHelper.shouldShowCancelConfirmation)

if __name__ == "__main__":
    main()
