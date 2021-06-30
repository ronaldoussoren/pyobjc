from PyObjCTools.TestSupport import TestCase

import Virtualization


class TestVZMacHardwareModel(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Virtualization.VZMacHardwareModel.isSupported)
