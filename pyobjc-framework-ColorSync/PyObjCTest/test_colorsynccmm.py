import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import ColorSync

    class TestColorSyncCMM (TestCase):
        @min_os_level('10.13')
        def testCFType(self):
            self.assertIsCFType(ColorSync.ColorSyncCMMRef)

        @min_os_level('10.13')
        def testFunctions(self):
            self.assertIsInstance(ColorSync.ColorSyncCMMGetTypeID(), (int, long))
            self.assertResultIsCFRetained(ColorSync.ColorSyncCMMCreate)
            ColorSync.ColorSyncCMMGetBundle
            self.assertResultIsCFRetained(ColorSync.ColorSyncCMMCopyLocalizedName)
            self.assertResultIsCFRetained(ColorSync.ColorSyncCMMCopyCMMIdentifier)

            self.assertArgIsFunction(ColorSync.ColorSyncIterateInstalledCMMs, 0, objc._C_BOOL + b'^{ColorSyncCMM=}^v', False)

        @min_os_level('10.13')
        def testConstants(self):
            self.assertIsInstance(ColorSync.kCMMInitializeLinkProfileProcName, unicode)
            self.assertIsInstance(ColorSync.kCMMInitializeTransformProcName, unicode)
            self.assertIsInstance(ColorSync.kCMMApplyTransformProcName, unicode)
            self.assertIsInstance(ColorSync.kCMMCreateTransformPropertyProcName, unicode)

if __name__ == "__main__":
    main()
