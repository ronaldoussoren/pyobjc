from PyObjCTools.TestSupport import *

import libdispatch

class TestDispatch (TestCase):
    def test_constants(self):
        self.assertFalse(hasattr(libdispatch, 'DISPATCH_API_VERSION'))


if __name__ == "__main__":
    main()
