# NOTE: This file only contains basic tests of the keyvalue observing header definitions,
# test_keyvalue contains tests for the actualy KVC/KVO mechanisms.
from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSKeyValueObserving (TestCase):

    def testConstants(self):
        self.assertEqual( NSKeyValueObservingOptionNew, 1)
        self.assertEqual( NSKeyValueObservingOptionOld, 2)
        self.assertEqual( NSKeyValueObservingOptionInitial, 4)
        self.assertEqual( NSKeyValueObservingOptionPrior, 8)

        self.assertEqual( NSKeyValueChangeSetting, 1)
        self.assertEqual( NSKeyValueChangeInsertion, 2)
        self.assertEqual( NSKeyValueChangeRemoval, 3)
        self.assertEqual( NSKeyValueChangeReplacement, 4)

        self.assertEqual( NSKeyValueUnionSetMutation, 1)
        self.assertEqual( NSKeyValueMinusSetMutation, 2)
        self.assertEqual( NSKeyValueIntersectSetMutation, 3)
        self.assertEqual( NSKeyValueSetSetMutation, 4)

        self.assertIsInstance(NSKeyValueChangeKindKey, unicode)
        self.assertIsInstance(NSKeyValueChangeNewKey, unicode)
        self.assertIsInstance(NSKeyValueChangeOldKey, unicode)
        self.assertIsInstance(NSKeyValueChangeIndexesKey, unicode)
        self.assertIsInstance(NSKeyValueChangeNotificationIsPriorKey, unicode)
    def testContext(self):
        o = NSObject.alloc().init()
        m = o.observeValueForKeyPath_ofObject_change_context_.__metadata__()
        self.assertEqual( m['arguments'][5]['type'], b'^v' )

        m = o.addObserver_forKeyPath_options_context_.__metadata__()
        self.assertEqual( m['arguments'][5]['type'], b'^v' )

        m = o.setObservationInfo_.__metadata__()
        self.assertEqual( m['arguments'][2]['type'], b'^v' )

        m = o.observationInfo.__metadata__()
        self.assertEqual( m['retval']['type'], b'^v' )

        o = NSArray.alloc().init()
        m = o.addObserver_toObjectsAtIndexes_forKeyPath_options_context_.__metadata__()
        self.assertEqual( m['arguments'][6]['type'], b'^v' )

        m = o.addObserver_forKeyPath_options_context_.__metadata__()
        self.assertEqual( m['arguments'][5]['type'], b'^v' )

        o = NSSet.alloc().init()
        m = o.addObserver_forKeyPath_options_context_.__metadata__()
        self.assertEqual( m['arguments'][5]['type'], b'^v' )


if __name__ == "__main__":
    main()
