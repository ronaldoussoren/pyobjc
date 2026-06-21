from PyObjCTools.TestSupport import TestCase

import SafetyKit


class TestSafetyKit(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(SafetyKit)
