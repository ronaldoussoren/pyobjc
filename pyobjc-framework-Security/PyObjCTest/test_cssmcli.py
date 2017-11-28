from PyObjCTools.TestSupport import *

import Security

class TestCSSMCLI (TestCase):

    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, 'CSSM_SPI_CL_FUNCS'))

if __name__ == "__main__":
    main()
