import Security
from PyObjCTools.TestSupport import TestCase


class TestSecIdentitySearch(TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, "SecIdentitySearchRef"))
        self.assertFalse(hasattr(Security, "SecIdentitySearchCreate"))
        self.assertFalse(hasattr(Security, "SecIdentitySearchCopyNext"))
