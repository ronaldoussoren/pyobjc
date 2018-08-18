from PyObjCTools.TestSupport import *

import CoreServices

class TestDriverSynchronization (TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(not hasattr(CoreServices, name), "%r exposed in bindings"%(name,))

    def test_not_wrapped(self):
        self.assert_not_wrapped('CompareAndSwap')
        self.assert_not_wrapped('TestAndClear')
        self.assert_not_wrapped('TestAndSet')
        self.assert_not_wrapped('IncrementAtomic8')
        self.assert_not_wrapped('DecrementAtomic8')
        self.assert_not_wrapped('AddAtomic8')
        self.assert_not_wrapped('BitAndAtomic8')
        self.assert_not_wrapped('BitOrAtomic8')
        self.assert_not_wrapped('BitXorAtomic8')
        self.assert_not_wrapped('IncrementAtomic16')
        self.assert_not_wrapped('DecrementAtomic16')
        self.assert_not_wrapped('AddAtomic16')
        self.assert_not_wrapped('BitAndAtomic16')
        self.assert_not_wrapped('BitOrAtomic16')
        self.assert_not_wrapped('BitXorAtomic16')
        self.assert_not_wrapped('IncrementAtomic')
        self.assert_not_wrapped('DecrementAtomic')
        self.assert_not_wrapped('AddAtomic')
        self.assert_not_wrapped('BitAndAtomic')
        self.assert_not_wrapped('BitOrAtomic')
        self.assert_not_wrapped('BitXorAtomic')



if __name__ == "__main__":
    main()
