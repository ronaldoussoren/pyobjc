import objc
import PreferencePanes
from PyObjCTools.TestSupport import TestCase


class TestPreferencePanes(TestCase):
    def testClasses(self):
        self.assertTrue(hasattr(PreferencePanes, "NSPreferencePane"))
        self.assertTrue(isinstance(PreferencePanes.NSPreferencePane, objc.objc_class))


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(PreferencePanes)
