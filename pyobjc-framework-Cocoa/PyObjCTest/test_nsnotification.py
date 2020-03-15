import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSNotification(TestCase):
    def testMethods(self):
        self.assertArgIsSEL(
            Foundation.NSNotificationCenter.addObserver_selector_name_object_,
            1,
            b"v@:@",
        )

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsBlock(
            Foundation.NSNotificationCenter.addObserverForName_object_queue_usingBlock_,
            3,
            b"v@",
        )
