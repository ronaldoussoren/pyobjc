from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestNotificationCenter (TestCase):

    def testTypes(self):
        self.failUnlessIsCFType(CFNotificationCenterRef)

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

        self.failUnlessArgHasType(CFNotificationCenterAddObserver, 1, '@')
        self.failUnlessArgIsFunction(CFNotificationCenterAddObserver, 2, 'v@@@@@', True)
        self.failUnlessArgHasType(CFNotificationCenterAddObserver, 4, '@')

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

        self.failUnlessArgHasType(CFNotificationCenterRemoveObserver, 1, '@')
        self.failUnlessArgHasType(CFNotificationCenterRemoveObserver, 3, '@')
        CFNotificationCenterRemoveObserver(ref, u"object", u"pyobjc.test", ref)

        self.failUnlessArgHasType(CFNotificationCenterPostNotificationWithOptions, 2, '@') 
        CFNotificationCenterPostNotificationWithOptions(ref, u"pyobjc.test", ref, {u"name":u"value"},  kCFNotificationPostToAllSessions)
        self.failUnless(len(notifications) == 2)

        CFNotificationCenterAddObserver(ref, u"object", observe, u"pyobjc.test", ref, CFNotificationSuspensionBehaviorDeliverImmediately)

        self.failUnlessArgHasType(CFNotificationCenterPostNotification, 2, '@')
        self.failUnlessArgIsBOOL(CFNotificationCenterPostNotification, 4)
        CFNotificationCenterPostNotification(ref, u"pyobjc.test", ref, {u"name2":u"value2"},  True)
        self.failUnless(len(notifications) == 3)

        CFNotificationCenterRemoveEveryObserver(ref, u"object")
        CFNotificationCenterPostNotification(ref, u"pyobjc.test", ref, {u"name2":u"value2"},  True)
        self.failUnless(len(notifications) == 3)


    def testConstants(self):
        self.failUnlessEqual(CFNotificationSuspensionBehaviorDrop, 1)
        self.failUnlessEqual(CFNotificationSuspensionBehaviorCoalesce, 2)
        self.failUnlessEqual(CFNotificationSuspensionBehaviorHold, 3)
        self.failUnlessEqual(CFNotificationSuspensionBehaviorDeliverImmediately, 4)
        self.failUnlessEqual(kCFNotificationDeliverImmediately, 1)
        self.failUnlessEqual(kCFNotificationPostToAllSessions, 2)


if __name__ == "__main__":
    main()
