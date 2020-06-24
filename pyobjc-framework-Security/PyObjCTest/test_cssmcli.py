import Security
from PyObjCTools.TestSupport import TestCase


class TestCSSMCLI(TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, "CSSM_SPI_CL_FUNCS"))
