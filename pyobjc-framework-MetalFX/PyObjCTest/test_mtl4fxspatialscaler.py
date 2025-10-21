from PyObjCTools.TestSupport import TestCase

import MetalFX  # noqa: F401


class TestMTL4FXSpatialScaler(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("MTL4FXSpatialScaler")
