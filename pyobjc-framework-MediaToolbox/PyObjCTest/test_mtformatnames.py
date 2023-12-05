import MediaToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMTFormatNames(TestCase):
    @min_os_level("10.11")
    def test_functions(self):
        self.assertResultIsCFRetained(MediaToolbox.MTCopyLocalizedNameForMediaType)
        self.assertResultIsCFRetained(MediaToolbox.MTCopyLocalizedNameForMediaSubType)
