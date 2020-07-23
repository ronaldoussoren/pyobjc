from PyObjCTools.TestSupport import TestCase

import Virtualization


class TestVZFileSerialPortAttachment(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(
            Virtualization.VZFileSerialPortAttachment.initWithURL_append_error_, 1
        )
        self.assertArgIsOut(
            Virtualization.VZFileSerialPortAttachment.initWithURL_append_error_, 2
        )

        self.assertResultIsBOOL(Virtualization.VZFileSerialPortAttachment.append)
