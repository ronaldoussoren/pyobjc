from PyObjCTools.TestSupport import TestCase

import PHASE


class TestPHASEAssetRegistry(TestCase):
    def test_methods(self):
        self.assertArgIsOut(
            PHASE.PHASEAssetRegistry.registerGlobalMetaParameter_error_, 1
        )
        self.assertArgIsOut(
            PHASE.PHASEAssetRegistry.registerSoundEventAssetWithRootNode_identifier_error_,
            2,
        )
        self.assertArgIsOut(
            PHASE.PHASEAssetRegistry.registerSoundAssetAtURL_identifier_assetType_channelLayout_normalizationMode_error_,
            5,
        )
        self.assertArgIsOut(
            PHASE.PHASEAssetRegistry.registerSoundAssetWithData_identifier_format_normalizationMode_error_,
            4,
        )

        self.assertArgIsBlock(
            PHASE.PHASEAssetRegistry.unregisterAssetWithIdentifier_completion_, 1, b"vB"
        )
