import Security
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSecTask(TestCase):
    def test_types(self):
        self.assertIsCFType(Security.SecTaskRef)

    def test_functions(self):
        self.assertIsInstance(Security.SecTaskGetTypeID(), int)

        Security.SecTaskCreateWithAuditToken
        self.assertArgHasType(
            Security.SecTaskCreateWithAuditToken, 1, b"{audit_token_t=[8I]}"
        )

        self.assertResultIsCFRetained(Security.SecTaskCreateFromSelf)

        self.assertResultIsCFRetained(Security.SecTaskCopyValueForEntitlement)
        self.assertArgIsOut(
            Security.SecTaskCopyValueForEntitlement,
            2,
        )

        self.assertResultIsCFRetained(Security.SecTaskCopyValuesForEntitlements)
        self.assertArgIsOut(
            Security.SecTaskCopyValuesForEntitlements,
            2,
        )

    @min_os_level("10.12")
    def test_functions10_12(self):
        self.assertResultIsCFRetained(Security.SecTaskCopySigningIdentifier)
        self.assertArgIsOut(
            Security.SecTaskCopySigningIdentifier,
            1,
        )
