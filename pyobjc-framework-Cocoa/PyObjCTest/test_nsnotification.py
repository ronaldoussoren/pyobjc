import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSNotification(TestCase):
    def test_methods(self):
        self.assertArgIsSEL(
            Foundation.NSNotificationCenter.addObserver_selector_name_object_,
            1,
            b"v@:@",
        )

        self.assertArgIsBlock(
            Foundation.NSNotificationCenter.addObserverForName_object_queue_usingBlock_,
            3,
            b"v@",
        )
