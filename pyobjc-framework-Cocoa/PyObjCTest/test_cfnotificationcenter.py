import unittest
from CoreFoundation import *


class TestNotificationCenter (unittest.TestCase):

    def testTypeID(self):
        self.failUnless(isinstance(CFNotificationCenterGetTypeID(), (int, long)))

    def testGetting(self):
        ref = CFNotificationCenterGetLocalCenter();
        self.failUnless(isinstance(ref,CFNotificationCenterRef))

        ref = CFNotificationCenterGetDistributedCenter();
        self.failUnless(isinstance(ref,CFNotificationCenterRef))

        ref = CFNotificationCenterGetDarwinNotifyCenter();
        self.failUnless(isinstance(ref,CFNotificationCenterRef))

    def testSending(self):
        ref = CFNotificationCenterGetLocalCenter();
        self.failUnless(isinstance(ref,CFNotificationCenterRef))

        notifications = []
        @objc.callbackFor(CFNotificationCenterAddObserver)
        def observe(center, observer, name, object, userInfo):
            notifications.append(( center, observer, name, object, userInfo ))

        CFNotificationCenterAddObserver(ref, u"object", observe, u"pyobjc.test", ref, CFNotificationSuspensionBehaviorDeliverImmediately)

        CFNotificationCenterPostNotificationWithOptions(ref, u"pyobjc.test", ref, {u"name":u"value"},  kCFNotificationPostToAllSessions)
        self.failUnless(len(notifications) == 1)
        info = notifications[-1]
        self.failUnless(info[0] is ref)
        self.failUnless(info[1] == u"object")
        self.failUnless(info[2] == u"pyobjc.test")
        self.failUnless(info[3] is ref)
        self.failUnless(info[4] == {u"name":u"value"})

        CFNotificationCenterPostNotification(ref, u"pyobjc.test", ref, {u"name2":u"value2"},  True)
        self.failUnless(len(notifications) == 2)
        info = notifications[-1]
        self.failUnless(info[0] is ref)
        self.failUnless(info[1] == u"object")
        self.failUnless(info[2] == u"pyobjc.test")
        self.failUnless(info[3] is ref)
        self.failUnless(info[4] == {u"name2":u"value2"})

        CFNotificationCenterRemoveObserver(ref, u"object", u"pyobjc.test", ref)
        CFNotificationCenterPostNotificationWithOptions(ref, u"pyobjc.test", ref, {u"name":u"value"},  kCFNotificationPostToAllSessions)
        self.failUnless(len(notifications) == 2)

        CFNotificationCenterAddObserver(ref, u"object", observe, u"pyobjc.test", ref, CFNotificationSuspensionBehaviorDeliverImmediately)
        CFNotificationCenterPostNotification(ref, u"pyobjc.test", ref, {u"name2":u"value2"},  True)
        self.failUnless(len(notifications) == 3)

        CFNotificationCenterRemoveEveryObserver(ref, u"object")
        CFNotificationCenterPostNotification(ref, u"pyobjc.test", ref, {u"name2":u"value2"},  True)
        self.failUnless(len(notifications) == 3)


    def testConstants(self):
        self.failUnless(CFNotificationSuspensionBehaviorDrop == 1)
        self.failUnless(CFNotificationSuspensionBehaviorCoalesce == 2)
        self.failUnless(CFNotificationSuspensionBehaviorHold == 3)
        self.failUnless(CFNotificationSuspensionBehaviorDeliverImmediately == 4)
        self.failUnless(kCFNotificationDeliverImmediately == (1 << 0))
        self.failUnless(kCFNotificationPostToAllSessions == (1 << 1))


if __name__ == "__main__":
    unittest.main()
