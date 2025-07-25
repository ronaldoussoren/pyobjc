import SecurityFoundation
from PyObjCTools.TestSupport import TestCase


class TestSFAuthorization(TestCase):
    def test_classes(self):
        SecurityFoundation.SFAuthorization

    def test_methods(self):
        self.assertResultIsBOOL(
            SecurityFoundation.SFAuthorization.obtainWithRight_flags_error_
        )
        self.assertArgIsOut(
            SecurityFoundation.SFAuthorization.obtainWithRight_flags_error_, 2
        )

        self.assertResultIsBOOL(
            SecurityFoundation.SFAuthorization.obtainWithRights_flags_environment_authorizedRights_error_
        )
        self.assertArgIsOut(
            SecurityFoundation.SFAuthorization.obtainWithRights_flags_environment_authorizedRights_error_,
            3,
        )
        self.assertArgIsOut(
            SecurityFoundation.SFAuthorization.obtainWithRights_flags_environment_authorizedRights_error_,
            4,
        )

        # XXX: These look like the need more work.
        self.assertArgHasType(
            SecurityFoundation.SFAuthorization.authorizationWithFlags_rights_environment_,
            1,
            b"^{_AuthorizationRights=I^{_AuthorizationItem=^cQ^vI}}",
        )
        self.assertArgHasType(
            SecurityFoundation.SFAuthorization.authorizationWithFlags_rights_environment_,
            2,
            b"^{_AuthorizationEnvironment=I^{_AuthorizationItem=^cQ^vI}}",
        )

        self.assertArgHasType(
            SecurityFoundation.SFAuthorization.initWithFlags_rights_environment_,
            1,
            b"^{_AuthorizationRights=I^{_AuthorizationItem=^cQ^vI}}",
        )
        self.assertArgHasType(
            SecurityFoundation.SFAuthorization.initWithFlags_rights_environment_,
            2,
            b"^{_AuthorizationEnvironment=I^{_AuthorizationItem=^cQ^vI}}",
        )
