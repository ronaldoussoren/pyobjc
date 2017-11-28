from PyObjCTools.TestSupport import *

import Security

class Testcssmcspi (TestCase):

    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, 'CSSM_SPI_CSP_FUNCS'))

if __name__ == "__main__":
    main()
