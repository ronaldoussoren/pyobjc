from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZVirtioSharedMemoryRegion(TestCase):
    @min_os_level("27.0")
    def test_methods(self):
        self.assertArgIsBlock(
            Virtualization.VZVirtioSharedMemoryRegion.mapMemory_atOffset_size_completionHandler_,
            3,
            b"v@",
        )
        self.assertArgIsBlock(
            Virtualization.VZVirtioSharedMemoryRegion.unmapMemoryAtOffset_size_completionHandler_,
            2,
            b"v@",
        )
