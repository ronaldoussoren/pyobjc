import Security
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestSecTask(TestCase):
    def test_types(self):
        self.assertIsCFType(Security.SecTaskRef)

    def test_functions(self):
        self.assertIsInstance(Security.SecTaskGetTypeID(), int)

        self.assertResultHasType(Security.SecTaskCreateWithAuditToken, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecTaskCreateWithAuditToken)
        self.assertArgHasType(Security.SecTaskCreateWithAuditToken, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTaskCreateWithAuditToken, 1, b"{?=[8I]}")

        self.assertResultHasType(Security.SecTaskCreateFromSelf, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecTaskCreateFromSelf)
        self.assertArgHasType(Security.SecTaskCreateFromSelf, 0, objc._C_ID)

        self.assertResultHasType(Security.SecTaskCopyValueForEntitlement, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecTaskCopyValueForEntitlement)
        self.assertArgHasType(Security.SecTaskCopyValueForEntitlement, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTaskCopyValueForEntitlement, 1, objc._C_ID)
        self.assertArgHasType(
            Security.SecTaskCopyValueForEntitlement,
            2,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )

        self.assertResultHasType(Security.SecTaskCopyValuesForEntitlements, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecTaskCopyValuesForEntitlements)
        self.assertArgHasType(Security.SecTaskCopyValuesForEntitlements, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTaskCopyValuesForEntitlements, 1, objc._C_ID)
        self.assertArgHasType(
            Security.SecTaskCopyValuesForEntitlements,
            2,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )

    @min_os_level("10.12")
    def test_functions10_12(self):
        self.assertResultHasType(Security.SecTaskCopySigningIdentifier, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecTaskCopySigningIdentifier)
        self.assertArgHasType(Security.SecTaskCopySigningIdentifier, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecTaskCopySigningIdentifier,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
