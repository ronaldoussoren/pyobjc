from PyObjCTools.TestSupport import TestCase

import SafetyKit


class TestSafetyKit(TestCase):
    def test_metadata_sane(self):
        self.assertCallableMetadataIsSane(SafetyKit)
