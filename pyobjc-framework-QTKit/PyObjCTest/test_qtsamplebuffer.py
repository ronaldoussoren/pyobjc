from PyObjCTools.TestSupport import TestCase
import QTKit


class TestQTSampleBuffer(TestCase):
    def testConstants(self):
        self.assertIsInstance(QTKit.QTSampleBufferSMPTETimeAttribute, str)
        self.assertIsInstance(QTKit.QTSampleBufferDateRecordedAttribute, str)
        self.assertIsInstance(QTKit.QTSampleBufferHostTimeAttribute, str)
        self.assertIsInstance(QTKit.QTSampleBufferSceneChangeTypeAttribute, str)
        self.assertIsInstance(QTKit.QTSampleBufferExplicitSceneChange, str)
        self.assertIsInstance(
            QTKit.QTSampleBufferTimeStampDiscontinuitySceneChange, str
        )

        self.assertEqual(
            QTKit.QTSampleBufferAudioBufferListOptionAssure16ByteAlignment, 1
        )

    def testMethods(self):
        self.assertResultIsBOOL(
            QTKit.QTSampleBuffer.getAudioStreamPacketDescriptions_inRange_
        )
