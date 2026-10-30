import Security
from PyObjCTools.TestSupport import TestCase


class TestSecRequirement(TestCase):
    def test_types(self):
        self.assertIsCFType(Security.SecRequirementRef)

    def test_functions(self):
        self.assertIsInstance(Security.SecRequirementGetTypeID(), int)

        self.assertArgIsOut(
            Security.SecRequirementCreateWithData,
            2,
        )
        self.assertArgIsCFRetained(Security.SecRequirementCreateWithData, 2)

        self.assertArgIsOut(
            Security.SecRequirementCreateWithString,
            2,
        )
        self.assertArgIsCFRetained(Security.SecRequirementCreateWithString, 2)

        self.assertArgIsOut(
            Security.SecRequirementCreateWithStringAndErrors,
            2,
        )
        self.assertArgIsOut(
            Security.SecRequirementCreateWithStringAndErrors,
            3,
        )
        self.assertArgIsCFRetained(Security.SecRequirementCreateWithStringAndErrors, 3)

        self.assertArgIsOut(Security.SecRequirementCopyData, 2)
        self.assertArgIsCFRetained(Security.SecRequirementCopyData, 2)

        self.assertArgIsOut(Security.SecRequirementCopyString, 2)
        self.assertArgIsCFRetained(Security.SecRequirementCopyString, 2)
