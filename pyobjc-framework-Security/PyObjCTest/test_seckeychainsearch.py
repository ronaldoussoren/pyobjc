import Security
from PyObjCTools.TestSupport import *


class TestSecKeychainSearch(TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, "SecKeychainSearchGetTypeID"))
        self.assertFalse(hasattr(Security, "SecKeychainSearchCreateFromAttributes"))
        self.assertFalse(hasattr(Security, "SecKeychainSearchCopyNext"))
        self.assertFalse(hasattr(Security, "SecKeychainSearchRef"))


if __name__ == "__main__":
    main()
