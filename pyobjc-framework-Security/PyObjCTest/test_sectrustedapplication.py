from PyObjCTools.TestSupport import *

import Security

class TestSecTrustedApplication (TestCase):

    def test_types(self):
        self.assertIsCFType(Security.SecTrustedApplicationRef)

    def test_functions10_7(self):
        self.assertIsInstance(Security.SecTrustedApplicationGetTypeID(), (int, long))

        self.assertResultHasType(Security.SecTrustedApplicationCreateFromPath, objc._C_INT)
        self.assertArgHasType(Security.SecTrustedApplicationCreateFromPath, 0, objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT)
        self.assertArgIsNullTerminated(Security.SecTrustedApplicationCreateFromPath, 0)
        self.assertArgHasType(Security.SecTrustedApplicationCreateFromPath, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecTrustedApplicationCreateFromPath, 1)

        self.assertResultHasType(Security.SecTrustedApplicationCopyData, objc._C_INT)
        self.assertArgHasType(Security.SecTrustedApplicationCopyData, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTrustedApplicationCopyData, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecTrustedApplicationCopyData, 1)

        self.assertResultHasType(Security.SecTrustedApplicationSetData, objc._C_INT)
        self.assertArgHasType(Security.SecTrustedApplicationSetData, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTrustedApplicationSetData, 1, objc._C_ID)


if __name__ == "__main__":
    main()
