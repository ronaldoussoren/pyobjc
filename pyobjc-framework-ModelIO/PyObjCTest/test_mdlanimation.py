from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import ModelIO

    class TestMDLAnimation (TestCase):
        @min_sdk_level('10.13')
        def testProtocols(self):
            objc.protocolNamed('MDLJointAnimation')

if __name__ == "__main__":
    main()
