from PyObjCTools.TestSupport import TestCase
import Quartz


class TestIKFilterUI(TestCase):
    def test_constants(self):
        self.assertIsInstance(Quartz.IKUISizeFlavor, str)
        self.assertIsInstance(Quartz.IKUISizeMini, str)
        self.assertIsInstance(Quartz.IKUISizeSmall, str)
        self.assertIsInstance(Quartz.IKUISizeRegular, str)
        self.assertIsInstance(Quartz.IKUImaxSize, str)
        self.assertIsInstance(Quartz.IKUIFlavorAllowFallback, str)

    def test_protocols(self):
        self.assertProtocolExists("IKFilterCustomUIProvider", Quartz)
