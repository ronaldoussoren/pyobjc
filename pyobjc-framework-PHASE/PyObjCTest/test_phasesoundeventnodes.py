from PyObjCTools.TestSupport import TestCase, min_os_level

import PHASE
import CoreAudio

PHASEPullStreamRenderBlock = (
    b"iN^Bn^"
    + CoreAudio.AudioTimeStamp.__typestr__
    + b"I"
    + CoreAudio.AudioBufferList.__typestr__
)


class TestPHASESoundEventNodes(TestCase):
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

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertResultIsBOOL(PHASE.PHASEPullStreamNodeDefinition.normalize)
        self.assertArgIsBOOL(PHASE.PHASEPullStreamNodeDefinition.setNormalize_, 0)

        self.assertResultIsBlock(
            PHASE.PHASEPullStreamNode.renderBlock, PHASEPullStreamRenderBlock
        )
        self.assertArgIsBlock(
            PHASE.PHASEPullStreamNode.setRenderBlock_, 0, PHASEPullStreamRenderBlock
        )
