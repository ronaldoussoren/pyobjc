from PyObjCTools.TestSupport import TestCase

import MetalFX  # noqa: F401


class TestMTL4FXTemporalScaler(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("MTL4FXTemporalScaler")
