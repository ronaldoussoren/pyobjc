from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import ModelIO

    class TestMDLAssetResolverHelper (ModelIO.NSObject):
        def canResolveAssetNamed_(self, name): return 1

    class TestMDLAssetResolver (TestCase):
        @min_sdk_level('10.13')
        def testProtocols(self):
            objc.protocolNamed('MDLAssetResolver')

        def testMethods(self):
            self.assertResultIsBOOL(ModelIO.TestMDLAssetResolverHelper.canResolveAssetNamed_)


if __name__ == "__main__":
    main()
