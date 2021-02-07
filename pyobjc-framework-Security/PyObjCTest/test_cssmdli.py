import Security
from PyObjCTools.TestSupport import TestCase


class Testcssmdli(TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, "CSSM_SPI_DL_FUNCS"))
