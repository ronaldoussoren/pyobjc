from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZMultipleDirectoryShare(TestCase):
    @min_os_level("12.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            Virtualization.VZMultipleDirectoryShare.validateName_error_
        )
        self.assertArgIsOut(
            Virtualization.VZMultipleDirectoryShare.validateName_error_, 1
        )
