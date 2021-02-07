import Security
from PyObjCTools.TestSupport import TestCase


class Testcssmkrspi(TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, "CSSM_SPI_KR_FUNCS"))
