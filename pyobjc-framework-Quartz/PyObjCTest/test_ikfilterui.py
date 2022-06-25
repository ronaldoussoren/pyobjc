from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestIKFilterUI(TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(Quartz.IKUISizeFlavor, str)
        self.assertIsInstance(Quartz.IKUISizeMini, str)
        self.assertIsInstance(Quartz.IKUISizeSmall, str)
        self.assertIsInstance(Quartz.IKUISizeRegular, str)
        self.assertIsInstance(Quartz.IKUImaxSize, str)
        self.assertIsInstance(Quartz.IKUIFlavorAllowFallback, str)

    @min_os_level("10.5")
    def no_testProtocol(self):
        self.assertIsInstance(
            self.assertProtocolExists("IKFilterCustomUIProvider"), objc.formal_protocol
        )
