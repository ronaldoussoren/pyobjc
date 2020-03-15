# NOTE: This file only contains basic tests of the keyvalue observing header definitions,
# test_keyvalue contains tests for the actualy KVC/KVO mechanisms.
import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSKeyValueObserving(TestCase):
    def testConstants(self):
        self.assertEqual(Foundation.NSKeyValueObservingOptionNew, 1)
        self.assertEqual(Foundation.NSKeyValueObservingOptionOld, 2)
        self.assertEqual(Foundation.NSKeyValueObservingOptionInitial, 4)
        self.assertEqual(Foundation.NSKeyValueObservingOptionPrior, 8)

        self.assertEqual(Foundation.NSKeyValueChangeSetting, 1)
        self.assertEqual(Foundation.NSKeyValueChangeInsertion, 2)
        self.assertEqual(Foundation.NSKeyValueChangeRemoval, 3)
        self.assertEqual(Foundation.NSKeyValueChangeReplacement, 4)

        self.assertEqual(Foundation.NSKeyValueUnionSetMutation, 1)
        self.assertEqual(Foundation.NSKeyValueMinusSetMutation, 2)
        self.assertEqual(Foundation.NSKeyValueIntersectSetMutation, 3)
        self.assertEqual(Foundation.NSKeyValueSetSetMutation, 4)

        self.assertIsInstance(Foundation.NSKeyValueChangeKindKey, str)
        self.assertIsInstance(Foundation.NSKeyValueChangeNewKey, str)
        self.assertIsInstance(Foundation.NSKeyValueChangeOldKey, str)
        self.assertIsInstance(Foundation.NSKeyValueChangeIndexesKey, str)
        self.assertIsInstance(Foundation.NSKeyValueChangeNotificationIsPriorKey, str)

    def testContext(self):
        o = Foundation.NSObject.alloc().init()
        m = o.observeValueForKeyPath_ofObject_change_context_.__metadata__()
        self.assertEqual(m["arguments"][5]["type"], b"^v")

        m = o.addObserver_forKeyPath_options_context_.__metadata__()
        self.assertEqual(m["arguments"][5]["type"], b"^v")

        m = o.setObservationInfo_.__metadata__()
        self.assertEqual(m["arguments"][2]["type"], b"^v")

        m = o.observationInfo.__metadata__()
        self.assertEqual(m["retval"]["type"], b"^v")

        o = Foundation.NSArray.alloc().init()
        m = o.addObserver_toObjectsAtIndexes_forKeyPath_options_context_.__metadata__()
        self.assertEqual(m["arguments"][6]["type"], b"^v")

        m = o.addObserver_forKeyPath_options_context_.__metadata__()
        self.assertEqual(m["arguments"][5]["type"], b"^v")

        o = Foundation.NSSet.alloc().init()
        m = o.addObserver_forKeyPath_options_context_.__metadata__()
        self.assertEqual(m["arguments"][5]["type"], b"^v")

    @min_os_level("10.7")
    def testContext10_7(self):
        o = Foundation.NSObject.alloc().init()
        m = o.removeObserver_forKeyPath_context_.__metadata__()
        self.assertEqual(m["arguments"][4]["type"], b"^v")

        o = Foundation.NSMutableArray.alloc().init()
        m = o.removeObserver_fromObjectsAtIndexes_forKeyPath_context_.__metadata__()
        self.assertEqual(m["arguments"][5]["type"], b"^v")

        o = Foundation.NSOrderedSet.alloc().init()
        m = o.removeObserver_forKeyPath_context_.__metadata__()
        self.assertEqual(m["arguments"][4]["type"], b"^v")

        o = Foundation.NSSet.alloc().init()
        m = o.removeObserver_forKeyPath_context_.__metadata__()
        self.assertEqual(m["arguments"][4]["type"], b"^v")

    def testMethods(self):
        self.assertResultIsBOOL(
            Foundation.NSObject.automaticallyNotifiesObserversForKey_
        )
