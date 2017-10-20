from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2**32:
    import Vision

    class TestVNFaceObservationAccepting (TestCase):
        @min_sdk_level('10.13')
        def testProtocols10_13(self):
            objc.protocolNamed('VNFaceObservationAccepting')


if __name__ == "__main__":
    main()
