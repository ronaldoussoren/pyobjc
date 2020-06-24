import Security
from PyObjCTools.TestSupport import TestCase
import objc


class TestSecRequirement(TestCase):
    def testTypes(self):
        self.assertIsCFType(Security.SecRequirementRef)

    def test_functions(self):
        self.assertIsInstance(Security.SecRequirementGetTypeID(), int)

        self.assertResultHasType(Security.SecRequirementCreateWithData, objc._C_INT)
        self.assertArgHasType(Security.SecRequirementCreateWithData, 0, objc._C_ID)
        self.assertArgHasType(Security.SecRequirementCreateWithData, 1, objc._C_UINT)
        self.assertArgHasType(
            Security.SecRequirementCreateWithData,
            2,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecRequirementCreateWithData, 2)

        self.assertResultHasType(Security.SecRequirementCreateWithString, objc._C_INT)
        self.assertArgHasType(Security.SecRequirementCreateWithString, 0, objc._C_ID)
        self.assertArgHasType(Security.SecRequirementCreateWithString, 1, objc._C_UINT)
        self.assertArgHasType(
            Security.SecRequirementCreateWithString,
            2,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecRequirementCreateWithString, 2)

        self.assertResultHasType(
            Security.SecRequirementCreateWithStringAndErrors, objc._C_INT
        )
        self.assertArgHasType(
            Security.SecRequirementCreateWithStringAndErrors, 0, objc._C_ID
        )
        self.assertArgHasType(
            Security.SecRequirementCreateWithStringAndErrors, 1, objc._C_UINT
        )
        self.assertArgHasType(
            Security.SecRequirementCreateWithStringAndErrors,
            2,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgHasType(
            Security.SecRequirementCreateWithStringAndErrors,
            3,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecRequirementCreateWithStringAndErrors, 3)

        self.assertResultHasType(Security.SecRequirementCopyData, objc._C_INT)
        self.assertArgHasType(Security.SecRequirementCopyData, 0, objc._C_ID)
        self.assertArgHasType(Security.SecRequirementCopyData, 1, objc._C_UINT)
        self.assertArgHasType(
            Security.SecRequirementCopyData, 2, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecRequirementCopyData, 2)

        self.assertResultHasType(Security.SecRequirementCopyString, objc._C_INT)
        self.assertArgHasType(Security.SecRequirementCopyString, 0, objc._C_ID)
        self.assertArgHasType(Security.SecRequirementCopyString, 1, objc._C_UINT)
        self.assertArgHasType(
            Security.SecRequirementCopyString, 2, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecRequirementCopyString, 2)
