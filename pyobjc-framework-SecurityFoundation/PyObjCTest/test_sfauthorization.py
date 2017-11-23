from PyObjCTools.TestSupport import *

import SecurityFoundation

class TestSFAuthorization (TestCase):
    def test_classes(self):
        SecurityFoundation.SFAuthorization

    def test_methods(self):
        self.assertResultIsBOOL(SecurityFoundation.SFAuthorization.obtainWithRight_flags_error_)
        self.assertArgIsOut(SecurityFoundation.SFAuthorization.obtainWithRight_flags_error_, 2)

        self.assertResultIsBOOL(SecurityFoundation.SFAuthorization.obtainWithRights_flags_environment_authorizedRights_error_)
        self.assertArgIsOut(SecurityFoundation.SFAuthorization.obtainWithRights_flags_environment_authorizedRights_error_, 3)
        self.assertArgIsOut(SecurityFoundation.SFAuthorization.obtainWithRights_flags_environment_authorizedRights_error_, 4)


if __name__ == "__main__":
    main()
