import Security
from PyObjCTools.TestSupport import *


class TestSecIdentitySearch(TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, "SecIdentitySearchRef"))
        self.assertFalse(hasattr(Security, "SecIdentitySearchCreate"))
        self.assertFalse(hasattr(Security, "SecIdentitySearchCopyNext"))


if __name__ == "__main__":
    main()
