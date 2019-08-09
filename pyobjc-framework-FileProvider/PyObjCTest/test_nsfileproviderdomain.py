from PyObjCTools.TestSupport import *

import FileProvider

class TestNSFileProviderDomain (TestCase):
    @min_os_level('10.15')
    def test_methods10_15(self):
        self.assertResultIsBOOL(FileProvider.NSFileProviderDomain.isDisconnected)
        self.assertArgIsBOOL(FileProvider.NSFileProviderDomain.setDisconnected_, 0)
