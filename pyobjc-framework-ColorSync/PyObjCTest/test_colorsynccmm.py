import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import ColorSync

    class TestColorSyncCMM (TestCase):
        @min_os_level('10.13')
        def testCFType(self):
            self.assertCFType(ColorSync.ColorSyncCMMRef)

        @min_os_level('10.13')
        def testFunctions(self):
            self.assertIsInstance(ColorSync.ColorSyncCMMGetTypeID(), (int, long))
            self.assertResultIsCFRetained(ColorSync.ColorSyncCMMCreate)
            ColorSyncCMMGetBundle
            self.assertResultIsCFRetained(ColorSync.ColorSyncCMMCopyLocalizedName)
            self.assertResultIsCFRetained(ColorSync.ColorSyncCMMCopyCMMIdentifier)

            self.assertArgIsFunction(ColorSync.ColorSyncIterateInstalledCMMs, 0, objc._C_BOOL + b'^{ColorSyncCMM=}^v', False)

        @min_os_level('10.13')
        def testConstants(self):
            self.assertIsInstance(kCMMInitializeLinkProfileProcName, unicode)
            self.assertIsInstance(kCMMInitializeTransformProcName, unicode)
            self.assertIsInstance(kCMMApplyTransformProcName, unicode)
            self.assertIsInstance(kCMMCreateTransformPropertyProcName, unicode)

if __name__ == "__main__":
    main()
