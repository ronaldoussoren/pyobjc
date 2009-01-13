# NOTE: This file only contains basic tests of the keyvalue observing header definitions,
# test_keyvalue contains tests for the actualy KVC/KVO mechanisms.
from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSKeyValueObserving (TestCase):

    def testConstants(self):
        self.assertEquals( NSKeyValueObservingOptionNew, 1)
        self.assertEquals( NSKeyValueObservingOptionOld, 2)
        self.assertEquals( NSKeyValueObservingOptionInitial, 4)
        self.assertEquals( NSKeyValueObservingOptionPrior, 8)

        self.assertEquals( NSKeyValueChangeSetting, 1)
        self.assertEquals( NSKeyValueChangeInsertion, 2)
        self.assertEquals( NSKeyValueChangeRemoval, 3)
        self.assertEquals( NSKeyValueChangeReplacement, 4)

        self.assertEquals( NSKeyValueUnionSetMutation, 1)
        self.assertEquals( NSKeyValueMinusSetMutation, 2)
        self.assertEquals( NSKeyValueIntersectSetMutation, 3)
        self.assertEquals( NSKeyValueSetSetMutation, 4)

        self.failUnless( isinstance(NSKeyValueChangeKindKey, unicode))
        self.failUnless( isinstance(NSKeyValueChangeNewKey, unicode))
        self.failUnless( isinstance(NSKeyValueChangeOldKey, unicode))
        self.failUnless( isinstance(NSKeyValueChangeIndexesKey, unicode))
        self.failUnless( isinstance(NSKeyValueChangeNotificationIsPriorKey, unicode))

    def testContext(self):
        o = NSObject.alloc().init()
        m = o.observeValueForKeyPath_ofObject_change_context_.__metadata__()
        self.assertEquals( m['arguments'][5]['type'], '^v' )

        m = o.addObserver_forKeyPath_options_context_.__metadata__()
        self.assertEquals( m['arguments'][5]['type'], '^v' )

        m = o.setObservationInfo_.__metadata__()
        self.assertEquals( m['arguments'][2]['type'], '^v' )

        m = o.observationInfo.__metadata__()
        self.assertEquals( m['retval']['type'], '^v' )

        o = NSArray.alloc().init()
        m = o.addObserver_toObjectsAtIndexes_forKeyPath_options_context_.__metadata__()
        self.assertEquals( m['arguments'][6]['type'], '^v' )

        m = o.addObserver_forKeyPath_options_context_.__metadata__()
        self.assertEquals( m['arguments'][5]['type'], '^v' )

        o = NSSet.alloc().init()
        m = o.addObserver_forKeyPath_options_context_.__metadata__()
        self.assertEquals( m['arguments'][5]['type'], '^v' )


if __name__ == "__main__":
    main()
