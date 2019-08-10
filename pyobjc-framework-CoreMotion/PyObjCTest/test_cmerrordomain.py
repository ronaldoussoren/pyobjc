from PyObjCTools.TestSupport import *

import CoreMotion


class TestCMErrorDomain(TestCase):
    @min_os_level("10.15")
    def test_constants(self):
        self.assertIsInstance(CoreMotion.CMErrorDomain, unicode)
