import Security
from PyObjCTools.TestSupport import TestCase


class Testcssmtpi(TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, "CSSM_SPI_TP_FUNCS"))
