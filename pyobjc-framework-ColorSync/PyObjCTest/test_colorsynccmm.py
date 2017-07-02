import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import ColorSync

    class TestColorSyncCMM (TestCase):
        def testConstants(self):
            self.assertIsInstance(kCMMInitializeLinkProfileProcName, unicode)
            self.assertIsInstance(kCMMInitializeTransformProcName, unicode)
            self.assertIsInstance(kCMMApplyTransformProcName, unicode)
            self.assertIsInstance(kCMMCreateTransformPropertyProcName, unicode)

if __name__ == "__main__":
    main()
