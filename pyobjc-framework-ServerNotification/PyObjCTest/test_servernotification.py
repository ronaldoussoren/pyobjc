from PyObjCTools.TestSupport import TestCase
import ServerNotification


class TestServerNotification(TestCase):
    def testClasses(self):
        self.assertArgIsSEL(
            ServerNotification.NSServerNotificationCenter.addObserver_selector_name_object_,
            1,
            b"v@:@",
        )


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(ServerNotification)
