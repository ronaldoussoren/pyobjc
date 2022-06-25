from PyObjCTools.TestSupport import TestCase, min_sdk_level
import ModelIO


class TestMDLAssetResolverHelper(ModelIO.NSObject):
    def canResolveAssetNamed_(self, name):
        return 1


class TestMDLAssetResolver(TestCase):
    @min_sdk_level("10.13")
    def testProtocols(self):
        self.assertProtocolExists("MDLAssetResolver")

    def testMethods(self):
        self.assertResultIsBOOL(
            ModelIO.TestMDLAssetResolverHelper.canResolveAssetNamed_
        )
