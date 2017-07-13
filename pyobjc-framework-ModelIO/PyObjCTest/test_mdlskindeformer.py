from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import ModelIO

    class TestMDLSkinDeformer (TestCase):
        @min_sdk_level('10.13')
        def testProtocols(self):
            objc.protocolNamed('MDLSkinDeformerComponent')

            # XXX: matrix_float4x4 arguments, requires SIMD support:
            # meshBindTransform
            # copyJointBindTranformsInto_maxCount_

        # XXX: matrix_float4 in MDLSkinDeformer APIs

if __name__ == "__main__":
    main()
