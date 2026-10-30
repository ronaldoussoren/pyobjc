from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZVirtioQueueElement(TestCase):
    @min_os_level("27.0")
    def test_methods(self):
        self.assertArgIsOut(
            Virtualization.VZVirtioQueueElement.peekIntoReadBuffersWithExactLength_error_,
            1,
        )
        self.assertArgIsOut(
            Virtualization.VZVirtioQueueElement.readBytesWithExactLength_error_, 1
        )

        self.assertResultIsBOOL(
            Virtualization.VZVirtioQueueElement.readBytesIntoBuffer_exactLength_error_
        )
        self.assertArgIsOut(
            Virtualization.VZVirtioQueueElement.readBytesIntoBuffer_exactLength_error_,
            0,
        )
        self.assertArgSizeInArg(
            Virtualization.VZVirtioQueueElement.readBytesIntoBuffer_exactLength_error_,
            0,
            1,
        )
        self.assertArgIsOut(
            Virtualization.VZVirtioQueueElement.readBytesIntoBuffer_exactLength_error_,
            2,
        )

        self.assertResultIsBOOL(Virtualization.VZVirtioQueueElement.writeData_error_)
        self.assertArgIsOut(Virtualization.VZVirtioQueueElement.writeData_error_, 1)

        self.assertResultIsBOOL(
            Virtualization.VZVirtioQueueElement.writeBuffer_exactLength_error_
        )
        self.assertArgIsIn(
            Virtualization.VZVirtioQueueElement.writeBuffer_exactLength_error_, 0
        )
        self.assertArgSizeInArg(
            Virtualization.VZVirtioQueueElement.writeBuffer_exactLength_error_, 0, 1
        )
        self.assertArgIsOut(
            Virtualization.VZVirtioQueueElement.writeBuffer_exactLength_error_, 2
        )
