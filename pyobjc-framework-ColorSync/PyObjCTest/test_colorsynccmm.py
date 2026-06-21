from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import ColorSync


class TestColorSyncCMM(TestCase):
    @min_os_level("10.13")
    def test_cftype(self):
        self.assertIsCFType(ColorSync.ColorSyncCMMRef)

    @min_os_level("10.13")
    def test_functions(self):
        self.assertIsInstance(ColorSync.ColorSyncCMMGetTypeID(), int)
        self.assertResultIsCFRetained(ColorSync.ColorSyncCMMCreate)
        ColorSync.ColorSyncCMMGetBundle
        self.assertResultIsCFRetained(ColorSync.ColorSyncCMMCopyLocalizedName)
        self.assertResultIsCFRetained(ColorSync.ColorSyncCMMCopyCMMIdentifier)

        self.assertArgIsFunction(
            ColorSync.ColorSyncIterateInstalledCMMs,
            0,
            objc._C_BOOL + b"^{ColorSyncCMM=}^v",
            False,
        )

    @min_os_level("10.13")
    def test_constants(self):
        self.assertIsInstance(ColorSync.kCMMInitializeLinkProfileProcName, str)
        self.assertIsInstance(ColorSync.kCMMInitializeTransformProcName, str)
        self.assertIsInstance(ColorSync.kCMMApplyTransformProcName, str)
        self.assertIsInstance(ColorSync.kCMMCreateTransformPropertyProcName, str)
