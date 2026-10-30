from PyObjCTools.TestSupport import TestCase, min_sdk_level
import ModelIO


class TestMDLAssetResolverHelper(ModelIO.NSObject):
    def canResolveAssetNamed_(self, name):
        return 1


class TestMDLAssetResolver(TestCase):
    @min_sdk_level("10.13")
    def test_protocols(self):
        self.assertProtocolExists("MDLAssetResolver", ModelIO)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(
            ModelIO.TestMDLAssetResolverHelper.canResolveAssetNamed_
        )
