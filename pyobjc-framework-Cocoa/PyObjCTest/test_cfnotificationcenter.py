import CoreFoundation
from PyObjCTools.TestSupport import TestCase
import objc


class TestNotificationCenter(TestCase):
    def testTypes(self):
        self.assertIsCFType(CoreFoundation.CFNotificationCenterRef)

    def testTypeID(self):
        self.assertIsInstance(CoreFoundation.CFNotificationCenterGetTypeID(), int)

    def testGetting(self):
        ref = CoreFoundation.CFNotificationCenterGetLocalCenter()
        self.assertIsInstance(ref, CoreFoundation.CFNotificationCenterRef)
        ref = CoreFoundation.CFNotificationCenterGetDistributedCenter()
        self.assertIsInstance(ref, CoreFoundation.CFNotificationCenterRef)
        ref = CoreFoundation.CFNotificationCenterGetDarwinNotifyCenter()
        self.assertIsInstance(ref, CoreFoundation.CFNotificationCenterRef)

    def testSending(self):
        ref = CoreFoundation.CFNotificationCenterGetLocalCenter()
        self.assertIsInstance(ref, CoreFoundation.CFNotificationCenterRef)
        notifications = []

        @objc.callbackFor(CoreFoundation.CFNotificationCenterAddObserver)
        def observe(center, observer, name, value, userInfo):
            notifications.append((center, observer, name, value, userInfo))

        self.assertArgHasType(CoreFoundation.CFNotificationCenterAddObserver, 1, b"@")
        self.assertArgIsFunction(
            CoreFoundation.CFNotificationCenterAddObserver, 2, b"v@@@@@", True
        )
        self.assertArgHasType(CoreFoundation.CFNotificationCenterAddObserver, 4, b"@")

        args = {}
        args["object"] = "object"
        args["pyobjc.test"] = "pyobjc.test"

        CoreFoundation.CFNotificationCenterAddObserver(
            ref,
            args["object"],
            observe,
            args["pyobjc.test"],
            ref,
            CoreFoundation.CFNotificationSuspensionBehaviorDeliverImmediately,
        )

        CoreFoundation.CFNotificationCenterPostNotificationWithOptions(
            ref,
            "pyobjc.test",
            ref,
            {"name": "value"},
            CoreFoundation.kCFNotificationPostToAllSessions,
        )
        self.assertEqual(len(notifications), 1)
        info = notifications[-1]
        self.assertIs(info[0], ref)
        self.assertEqual(info[1], "object")
        self.assertEqual(info[2], "pyobjc.test")
        self.assertIs(info[3], ref)
        self.assertEqual(info[4], {"name": "value"})
        CoreFoundation.CFNotificationCenterPostNotification(
            ref, "pyobjc.test", ref, {"name2": "value2"}, True
        )
        self.assertEqual(len(notifications), 2)
        info = notifications[-1]
        self.assertIs(info[0], ref)
        self.assertEqual(info[1], "object")
        self.assertEqual(info[2], "pyobjc.test")
        self.assertIs(info[3], ref)
        self.assertEqual(info[4], {"name2": "value2"})
        self.assertArgHasType(
            CoreFoundation.CFNotificationCenterRemoveObserver, 1, b"@"
        )
        self.assertArgHasType(
            CoreFoundation.CFNotificationCenterRemoveObserver, 3, b"@"
        )
        CoreFoundation.CFNotificationCenterRemoveObserver(
            ref, args["object"], args["pyobjc.test"], ref
        )

        self.assertArgHasType(
            CoreFoundation.CFNotificationCenterPostNotificationWithOptions, 2, b"@"
        )
        CoreFoundation.CFNotificationCenterPostNotificationWithOptions(
            ref,
            "pyobjc.test",
            ref,
            {"name": "value"},
            CoreFoundation.kCFNotificationPostToAllSessions,
        )
        self.assertEqual(len(notifications), 2)

        CoreFoundation.CFNotificationCenterAddObserver(
            ref,
            args["object"],
            observe,
            args["pyobjc.test"],
            ref,
            CoreFoundation.CFNotificationSuspensionBehaviorDeliverImmediately,
        )

        self.assertArgHasType(
            CoreFoundation.CFNotificationCenterPostNotification, 2, b"@"
        )
        self.assertArgIsBOOL(CoreFoundation.CFNotificationCenterPostNotification, 4)
        CoreFoundation.CFNotificationCenterPostNotification(
            ref, "pyobjc.test", ref, {"name2": "value2"}, True
        )
        self.assertEqual(len(notifications), 3)
        CoreFoundation.CFNotificationCenterRemoveEveryObserver(ref, args["object"])
        CoreFoundation.CFNotificationCenterPostNotification(
            ref, "pyobjc.test", ref, {"name2": "value2"}, True
        )
        self.assertEqual(len(notifications), 3)

    def testConstants(self):
        self.assertEqual(CoreFoundation.CFNotificationSuspensionBehaviorDrop, 1)
        self.assertEqual(CoreFoundation.CFNotificationSuspensionBehaviorCoalesce, 2)
        self.assertEqual(CoreFoundation.CFNotificationSuspensionBehaviorHold, 3)
        self.assertEqual(
            CoreFoundation.CFNotificationSuspensionBehaviorDeliverImmediately, 4
        )

        self.assertEqual(CoreFoundation.kCFNotificationDeliverImmediately, 1)
        self.assertEqual(CoreFoundation.kCFNotificationPostToAllSessions, 2)
