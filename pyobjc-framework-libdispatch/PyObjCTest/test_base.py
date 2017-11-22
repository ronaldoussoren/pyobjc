from PyObjCTools.TestSupport import *

import libdispatch

class TestBase (TestCase):
    def test_constants(self):
        self.assertFalse(hasattr(libdispatch, 'DISPATCH_SWIFT3_OVERLAY'))


if __name__ == "__main__":
    main()
