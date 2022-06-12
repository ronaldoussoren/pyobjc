from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCAAnimation(TestCase):
    def test_constants(self):
        self.assertFalse(hasattr(Quartz, "UNIFIED_CORE_IMAGE"))
        self.assertFalse(hasattr(Quartz, "COREIMAGE_SUPPORTS_IOSURFACE"))
