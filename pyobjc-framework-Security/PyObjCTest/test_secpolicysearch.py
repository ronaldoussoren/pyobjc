from PyObjCTools.TestSupport import *

import Security

class TestSecPolicySearch (TestCase):

    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, 'SecPolicySearchRef'))
        self.assertFalse(hasattr(Security, 'SecPolicySearchGetTypeID'))
        self.assertFalse(hasattr(Security, 'SecPolicySearchCreate'))
        self.assertFalse(hasattr(Security, 'SecPolicySearchCopyNext'))

if __name__ == "__main__":
    main()
