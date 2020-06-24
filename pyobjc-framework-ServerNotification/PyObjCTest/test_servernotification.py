from PyObjCTools.TestSupport import TestCase
import ServerNotification


class TestServerNotification(TestCase):
    def testClasses(self):
        self.assertArgIsSEL(
            ServerNotification.NSServerNotificationCenter.addObserver_selector_name_object_,
            1,
            b"v@:@",
        )
