import Security
from PyObjCTools.TestSupport import TestCase
import objc


class TestSecTrustedApplication(TestCase):
    def test_types(self):
        self.assertIsCFType(Security.SecTrustedApplicationRef)

    def test_functions10_7(self):
        self.assertIsInstance(Security.SecTrustedApplicationGetTypeID(), int)

        self.assertArgHasType(
            Security.SecTrustedApplicationCreateFromPath,
            0,
            objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgIsNullTerminated(Security.SecTrustedApplicationCreateFromPath, 0)
        self.assertArgIsOut(
            Security.SecTrustedApplicationCreateFromPath,
            1,
        )
        self.assertArgIsCFRetained(Security.SecTrustedApplicationCreateFromPath, 1)

        self.assertArgIsOut(
            Security.SecTrustedApplicationCopyData,
            1,
        )
        self.assertArgIsCFRetained(Security.SecTrustedApplicationCopyData, 1)

        Security.SecTrustedApplicationSetData
