
from PyObjCTools.TestSupport import *
from QTKit import *

try:
    unicode
except NameError:
    unicode = str

class TestQTSampleBuffer (TestCase):
    def testConstants(self):
        self.assertIsInstance(QTSampleBufferSMPTETimeAttribute, unicode)
        self.assertIsInstance(QTSampleBufferDateRecordedAttribute, unicode)
        self.assertIsInstance(QTSampleBufferHostTimeAttribute, unicode)
        self.assertIsInstance(QTSampleBufferSceneChangeTypeAttribute, unicode)
        self.assertIsInstance(QTSampleBufferExplicitSceneChange, unicode)
        self.assertIsInstance(QTSampleBufferTimeStampDiscontinuitySceneChange, unicode)

        self.assertEqual(QTSampleBufferAudioBufferListOptionAssure16ByteAlignment, 1)

    def testMethods(self):
        self.assertResultIsBOOL(QTSampleBuffer.getAudioStreamPacketDescriptions_inRange_)



if __name__ == "__main__":
    main()
