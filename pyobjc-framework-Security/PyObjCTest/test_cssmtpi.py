import Security
from PyObjCTools.TestSupport import *


class Testcssmtpi(TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, "CSSM_SPI_TP_FUNCS"))


if __name__ == "__main__":
    main()
