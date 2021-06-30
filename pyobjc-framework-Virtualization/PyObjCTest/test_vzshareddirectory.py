from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZSharedDirectory(TestCase):
    @min_os_level("12.0")
    def test_methods(self):
        self.assertArgIsBOOL(Virtualization.VZSharedDirectory.initWithURL_readOnly_, 1)
        self.assertResultIsBOOL(Virtualization.VZSharedDirectory.isReadOnly)
