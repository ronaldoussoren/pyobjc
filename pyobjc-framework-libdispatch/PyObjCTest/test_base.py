import libdispatch
from PyObjCTools.TestSupport import *


class TestBase(TestCase):
    def test_constants(self):
        self.assertFalse(hasattr(libdispatch, "DISPATCH_SWIFT3_OVERLAY"))


if __name__ == "__main__":
    main()
