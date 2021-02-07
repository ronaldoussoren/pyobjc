import InstantMessage
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestIMControl(TestCase):
    @min_os_level("10.6")
    def testMethods(self):
        self.assertArgIsSEL(InstantMessage.IMAVControl.setAction_, 0, b"v@:@")
        self.assertResultIsBOOL(InstantMessage.IMAVControl.isEnabled)
        self.assertArgIsBOOL(InstantMessage.IMAVControl.setEnabled_, 0)
