import Security
from PyObjCTools.TestSupport import TestCase


class TestCSSMACI(TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, "CSSM_SPI_AC_FUNCS"))
