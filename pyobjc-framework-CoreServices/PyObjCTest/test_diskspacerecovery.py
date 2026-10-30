import CoreServices
from PyObjCTools.TestSupport import TestCase
import objc


class TestDiskSpaceRecovery(TestCase):
    def test_functions(self):
        self.assertArgIsOut(CoreServices.CSDiskSpaceStartRecovery, 3)
        self.assertArgIsBlock(CoreServices.CSDiskSpaceStartRecovery, 5, b"vZQ@")

        self.assertArgHasType(
            CoreServices.CSDiskSpaceCancelRecovery, 0, b"^{__CFUUID=}"
        )

        self.assertResultHasType(
            CoreServices.CSDiskSpaceGetRecoveryEstimate, objc._C_ULNG_LNG
        )
