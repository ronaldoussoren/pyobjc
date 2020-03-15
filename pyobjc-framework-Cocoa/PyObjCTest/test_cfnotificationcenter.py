import CoreFoundation
import objc
from PyObjCTools.TestSupport import TestCase


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
        def observe(center, observer, name, object, userInfo):
            notifications.append((center, observer, name, object, userInfo))

        self.assertArgHasType(CoreFoundation.CFNotificationCenterAddObserver, 1, b"@")
        self.assertArgIsFunction(
            CoreFoundation.CFNotificationCenterAddObserver, 2, b"v@@@@@", True
        )
        self.assertArgHasType(CoreFoundation.CFNotificationCenterAddObserver, 4, b"@")

        args = {}
        args["object"] = b"object".decode("ascii")
        args["pyobjc.test"] = b"pyobjc.test".decode("ascii")

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
            b"pyobjc.test".decode("ascii"),
            ref,
            {b"name".decode("ascii"): b"value".decode("ascii")},
            CoreFoundation.kCFNotificationPostToAllSessions,
        )
        self.assertEqual(len(notifications), 1)
        info = notifications[-1]
        self.assertIs(info[0], ref)
        self.assertEqual(info[1], b"object".decode("ascii"))
        self.assertEqual(info[2], b"pyobjc.test".decode("ascii"))
        self.assertIs(info[3], ref)
        self.assertEqual(info[4], {b"name".decode("ascii"): b"value".decode("ascii")})
        CoreFoundation.CFNotificationCenterPostNotification(
            ref,
            b"pyobjc.test".decode("ascii"),
            ref,
            {b"name2".decode("ascii"): b"value2".decode("ascii")},
            True,
        )
        self.assertEqual(len(notifications), 2)
        info = notifications[-1]
        self.assertIs(info[0], ref)
        self.assertEqual(info[1], b"object".decode("ascii"))
        self.assertEqual(info[2], b"pyobjc.test".decode("ascii"))
        self.assertIs(info[3], ref)
        self.assertEqual(info[4], {b"name2".decode("ascii"): b"value2".decode("ascii")})
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
            b"pyobjc.test".decode("ascii"),
            ref,
            {b"name".decode("ascii"): b"value".decode("ascii")},
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
            ref,
            b"pyobjc.test".decode("ascii"),
            ref,
            {b"name2".decode("ascii"): b"value2".decode("ascii")},
            True,
        )
        self.assertEqual(len(notifications), 3)
        CoreFoundation.CFNotificationCenterRemoveEveryObserver(ref, args["object"])
        CoreFoundation.CFNotificationCenterPostNotification(
            ref,
            b"pyobjc.test".decode("ascii"),
            ref,
            {b"name2".decode("ascii"): b"value2".decode("ascii")},
            True,
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
