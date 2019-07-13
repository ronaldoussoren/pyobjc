import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import GameController

    class TestGCRay (TestCase):
        @expectedFailure
        def testSIMD(self):
            self.fail("GCRay.initWithOrigin:direction: has simd_float3d arguments")
            self.fail("GCRay.origin is simd_float3d property")
            self.fail("GCRay.direction is simd_float3d property")


if __name__ == "__main__":
    main()
