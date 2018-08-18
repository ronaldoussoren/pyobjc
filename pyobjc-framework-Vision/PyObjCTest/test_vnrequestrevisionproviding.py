from PyObjCTools.TestSupport import *
import sys
import objc

if sys.maxsize >= 2**32:
    import Vision

    class TestVNRequestRevisionProviderHelper (Vision.NSObject):
        def requestRevision(self): return 1

    class TestVNRequestRevisionProvider (TestCase):

        def test_methods(self):
            self.assertResultHasType(TestVNRequestRevisionProviderHelper.requestRevision, objc._C_NSUInteger)

        @min_sdk_level('10.14')
        def test_protocols(self):
            objc.protocolNamed('VNRequestRevisionProviding')



if __name__ == "__main__":
    main()
