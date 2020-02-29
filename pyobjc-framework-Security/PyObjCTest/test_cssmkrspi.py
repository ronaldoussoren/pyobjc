import Security
from PyObjCTools.TestSupport import *


class Testcssmkrspi(TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, "CSSM_SPI_KR_FUNCS"))


if __name__ == "__main__":
    main()
