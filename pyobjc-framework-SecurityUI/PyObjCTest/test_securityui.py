import SecurityUI
from PyObjCTools.TestSupport import TestCase


class TestSecurityUI(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(SecurityUI)
