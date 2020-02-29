import Security
from PyObjCTools.TestSupport import *


class TestCSSMACI(TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, "CSSM_SPI_AC_FUNCS"))


if __name__ == "__main__":
    main()
