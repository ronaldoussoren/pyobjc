import Security
from PyObjCTools.TestSupport import TestCase


class Testcssmcspi(TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, "CSSM_SPI_CSP_FUNCS"))
