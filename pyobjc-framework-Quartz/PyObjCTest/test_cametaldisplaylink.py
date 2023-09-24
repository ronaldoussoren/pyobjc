from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import Quartz


class TestCAMetalDisplayLink(TestCase):
    @min_sdk_level("14.0")
    def test_protocols(self):
        self.assertProtocolExists("CAMetalDisplayLinkDelegate")

    @min_os_level("14.0")
    def test_methods(self):
        self.assertResultIsBOOL(Quartz.CAMetalDisplayLink.isPaused)
        self.assertArgIsBOOL(Quartz.CAMetalDisplayLink.setPaused_, 0)
