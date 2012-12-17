from PyObjCTools.TestSupport import *
from CoreFoundation import *


try:
    long
except NameError:
    long = int


class TestNotificationCenter (TestCase):

    def testTypes(self):
        self.assertIsCFType(CFNotificationCenterRef)

    def testTypeID(self):
        self.assertIsInstance(CFNotificationCenterGetTypeID(), (int, long))

    def testGetting(self):
        ref = CFNotificationCenterGetLocalCenter();
        self.assertIsInstance(ref,CFNotificationCenterRef)
        ref = CFNotificationCenterGetDistributedCenter();
        self.assertIsInstance(ref,CFNotificationCenterRef)
        ref = CFNotificationCenterGetDarwinNotifyCenter();
        self.assertIsInstance(ref,CFNotificationCenterRef)

    def testSending(self):
        ref = CFNotificationCenterGetLocalCenter();
        self.assertIsInstance(ref,CFNotificationCenterRef)
        notifications = []
        @objc.callbackFor(CFNotificationCenterAddObserver)
        def observe(center, observer, name, object, userInfo):
            notifications.append(( center, observer, name, object, userInfo ))

        self.assertArgHasType(CFNotificationCenterAddObserver, 1, b'@')
        self.assertArgIsFunction(CFNotificationCenterAddObserver, 2, b'v@@@@@', True)
        self.assertArgHasType(CFNotificationCenterAddObserver, 4, b'@')

        args = {}
        args["object"] = b"object".decode('ascii')
        args["pyobjc.test"] = b"pyobjc.test".decode('ascii')

        CFNotificationCenterAddObserver(ref, args["object"], observe, args["pyobjc.test"], ref, CFNotificationSuspensionBehaviorDeliverImmediately)

        CFNotificationCenterPostNotificationWithOptions(ref, b"pyobjc.test".decode('ascii'), ref, {b"name".decode('ascii'):b"value".decode('ascii')},  kCFNotificationPostToAllSessions)
        self.assertEqual(len(notifications) , 1)
        info = notifications[-1]
        self.assertIs(info[0], ref)
        self.assertEqual(info[1] , b"object".decode('ascii'))
        self.assertEqual(info[2] , b"pyobjc.test".decode('ascii'))
        self.assertIs(info[3], ref)
        self.assertEqual(info[4] , {b"name".decode('ascii'):b"value".decode('ascii')})
        CFNotificationCenterPostNotification(ref, b"pyobjc.test".decode('ascii'), ref, {b"name2".decode('ascii'):b"value2".decode('ascii')},  True)
        self.assertEqual(len(notifications) , 2)
        info = notifications[-1]
        self.assertIs(info[0], ref)
        self.assertEqual(info[1] , b"object".decode('ascii'))
        self.assertEqual(info[2] , b"pyobjc.test".decode('ascii'))
        self.assertIs(info[3], ref)
        self.assertEqual(info[4] , {b"name2".decode('ascii'):b"value2".decode('ascii')})
        self.assertArgHasType(CFNotificationCenterRemoveObserver, 1, b'@')
        self.assertArgHasType(CFNotificationCenterRemoveObserver, 3, b'@')
        CFNotificationCenterRemoveObserver(ref, args["object"], args["pyobjc.test"], ref)

        self.assertArgHasType(CFNotificationCenterPostNotificationWithOptions, 2, b'@')
        CFNotificationCenterPostNotificationWithOptions(ref, b"pyobjc.test".decode('ascii'), ref, {b"name".decode('ascii'):b"value".decode('ascii')},  kCFNotificationPostToAllSessions)
        self.assertEqual(len(notifications) , 2)

        CFNotificationCenterAddObserver(ref, args["object"], observe, args["pyobjc.test"], ref, CFNotificationSuspensionBehaviorDeliverImmediately)

        self.assertArgHasType(CFNotificationCenterPostNotification, 2, b'@')
        self.assertArgIsBOOL(CFNotificationCenterPostNotification, 4)
        CFNotificationCenterPostNotification(ref, b"pyobjc.test".decode('ascii'), ref, {b"name2".decode('ascii'):b"value2".decode('ascii')},  True)
        self.assertEqual(len(notifications) , 3)
        CFNotificationCenterRemoveEveryObserver(ref, args["object"])
        CFNotificationCenterPostNotification(ref, b"pyobjc.test".decode('ascii'), ref, {b"name2".decode('ascii'):b"value2".decode('ascii')},  True)
        self.assertEqual(len(notifications) , 3)

    def testConstants(self):
        self.assertEqual(CFNotificationSuspensionBehaviorDrop, 1)
        self.assertEqual(CFNotificationSuspensionBehaviorCoalesce, 2)
        self.assertEqual(CFNotificationSuspensionBehaviorHold, 3)
        self.assertEqual(CFNotificationSuspensionBehaviorDeliverImmediately, 4)

        self.assertEqual(kCFNotificationDeliverImmediately, 1)
        self.assertEqual(kCFNotificationPostToAllSessions, 2)

if __name__ == "__main__":
    main()
