from PyObjCTools.TestSupport import *
from CoreFoundation import *


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

        CFNotificationCenterAddObserver(ref, u"object", observe, u"pyobjc.test", ref, CFNotificationSuspensionBehaviorDeliverImmediately)

        CFNotificationCenterPostNotificationWithOptions(ref, u"pyobjc.test", ref, {u"name":u"value"},  kCFNotificationPostToAllSessions)
        self.assertEqual(len(notifications) , 1)
        info = notifications[-1]
        self.assertIs(info[0], ref)
        self.assertEqual(info[1] , u"object")
        self.assertEqual(info[2] , u"pyobjc.test")
        self.assertIs(info[3], ref)
        self.assertEqual(info[4] , {u"name":u"value"})
        CFNotificationCenterPostNotification(ref, u"pyobjc.test", ref, {u"name2":u"value2"},  True)
        self.assertEqual(len(notifications) , 2)
        info = notifications[-1]
        self.assertIs(info[0], ref)
        self.assertEqual(info[1] , u"object")
        self.assertEqual(info[2] , u"pyobjc.test")
        self.assertIs(info[3], ref)
        self.assertEqual(info[4] , {u"name2":u"value2"})
        self.assertArgHasType(CFNotificationCenterRemoveObserver, 1, b'@')
        self.assertArgHasType(CFNotificationCenterRemoveObserver, 3, b'@')
        CFNotificationCenterRemoveObserver(ref, u"object", u"pyobjc.test", ref)

        self.assertArgHasType(CFNotificationCenterPostNotificationWithOptions, 2, b'@') 
        CFNotificationCenterPostNotificationWithOptions(ref, u"pyobjc.test", ref, {u"name":u"value"},  kCFNotificationPostToAllSessions)
        self.assertEqual(len(notifications) , 2)
        CFNotificationCenterAddObserver(ref, u"object", observe, u"pyobjc.test", ref, CFNotificationSuspensionBehaviorDeliverImmediately)

        self.assertArgHasType(CFNotificationCenterPostNotification, 2, b'@')
        self.assertArgIsBOOL(CFNotificationCenterPostNotification, 4)
        CFNotificationCenterPostNotification(ref, u"pyobjc.test", ref, {u"name2":u"value2"},  True)
        self.assertEqual(len(notifications) , 3)
        CFNotificationCenterRemoveEveryObserver(ref, u"object")
        CFNotificationCenterPostNotification(ref, u"pyobjc.test", ref, {u"name2":u"value2"},  True)
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
