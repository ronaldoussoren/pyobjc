from PyObjCTools.TestSupport import *

import CoreServices

class TestToolUtils (TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(not hasattr(CoreServices, name), "%r exposed in bindings"%(name,))

    def test_not_wrapped(self):
        self.assert_not_wrapped('BitTst')
        self.assert_not_wrapped('BitSet')
        self.assert_not_wrapped('BitClr')
        self.assert_not_wrapped('BitAnd')
        self.assert_not_wrapped('BitOr')
        self.assert_not_wrapped('BitXor')
        self.assert_not_wrapped('BitNot')
        self.assert_not_wrapped('BitShift')


if __name__ == "__main__":
    main()
