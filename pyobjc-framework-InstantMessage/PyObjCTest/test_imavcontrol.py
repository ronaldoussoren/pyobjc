import InstantMessage
from PyObjCTools.TestSupport import TestCase


class TestIMControl(TestCase):
    def test_methods(self):
        self.assertArgIsSEL(InstantMessage.IMAVControl.setAction_, 0, b"v@:@")
        self.assertResultIsBOOL(InstantMessage.IMAVControl.isEnabled)
        self.assertArgIsBOOL(InstantMessage.IMAVControl.setEnabled_, 0)
