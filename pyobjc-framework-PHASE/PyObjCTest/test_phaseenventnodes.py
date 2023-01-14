from PyObjCTools.TestSupport import TestCase
import objc

import PHASE


class TestPHASESoundEventNodes(TestCase):
    def test_constants(self):
        self.assertIsEnumType(PHASE.PHASEPushStreamBufferOptions)
        self.assertEqual(PHASE.PHASEPushStreamBufferDefault, 1 << 0)
        self.assertEqual(PHASE.PHASEPushStreamBufferLoops, 1 << 1)
        self.assertEqual(PHASE.PHASEPushStreamBufferInterrupts, 1 << 2)
        self.assertEqual(PHASE.PHASEPushStreamBufferInterruptsAtLoop, 1 << 3)

        self.assertIsEnumType(PHASE.PHASEPushStreamCompletionCallbackCondition)
        self.assertEqual(PHASE.PHASEPushStreamCompletionDataRendered, 0)

    def test_methods(self):
        self.assertResultIsBOOL(PHASE.PHASEPushStreamNodeDefinition.normalize)
        self.assertArgIsBOOL(PHASE.PHASEPushStreamNodeDefinition.setNormalize_, 0)

        self.assertArgIsBlock(
            PHASE.PHASEPushStreamNode.scheduleBuffer_completionCallbackType_completionHandler_,
            2,
            b"v" + objc._C_NSInteger,
        )
        self.assertArgIsBlock(
            PHASE.PHASEPushStreamNode.scheduleBuffer_atTime_options_completionCallbackType_completionHandler_,
            4,
            b"v" + objc._C_NSInteger,
        )
