import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSDistributedNotificationCenter(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Foundation.NSDistributedNotificationCenterType, str)

    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSDistributedNotificationOptions)
        self.assertIsEnumType(Foundation.NSNotificationSuspensionBehavior)

    def testConstants(self):
        self.assertIsInstance(Foundation.NSLocalNotificationCenterType, str)
        self.assertEqual(Foundation.NSNotificationSuspensionBehaviorDrop, 1)
        self.assertEqual(Foundation.NSNotificationSuspensionBehaviorCoalesce, 2)
        self.assertEqual(Foundation.NSNotificationSuspensionBehaviorHold, 3)
        self.assertEqual(
            Foundation.NSNotificationSuspensionBehaviorDeliverImmediately, 4
        )

        self.assertEqual(Foundation.NSNotificationDeliverImmediately, 1)
        self.assertEqual(Foundation.NSNotificationPostToAllSessions, 2)

        self.assertEqual(Foundation.NSDistributedNotificationDeliverImmediately, 1)
        self.assertEqual(Foundation.NSDistributedNotificationPostToAllSessions, 2)

    def testMethods(self):
        self.assertArgIsSEL(
            Foundation.NSDistributedNotificationCenter.addObserver_selector_name_object_suspensionBehavior_,  # noqa: B950
            1,
            b"v@:@",
        )
        self.assertArgIsSEL(
            Foundation.NSDistributedNotificationCenter.addObserver_selector_name_object_,
            1,
            b"v@:@",
        )

        self.assertArgIsBOOL(
            Foundation.NSDistributedNotificationCenter.postNotificationName_object_userInfo_deliverImmediately_,  # noqa: B950
            3,
        )
        self.assertArgIsBOOL(
            Foundation.NSDistributedNotificationCenter.setSuspended_, 0
        )
        self.assertResultIsBOOL(Foundation.NSDistributedNotificationCenter.suspended)
