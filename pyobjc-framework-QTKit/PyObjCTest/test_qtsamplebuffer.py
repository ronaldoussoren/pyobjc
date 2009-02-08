
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTSampleBuffer (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(QTSampleBufferSMPTETimeAttribute, unicode)
        self.failUnlessIsInstance(QTSampleBufferDateRecordedAttribute, unicode)
        self.failUnlessIsInstance(QTSampleBufferHostTimeAttribute, unicode)
        self.failUnlessIsInstance(QTSampleBufferSceneChangeTypeAttribute, unicode)
        self.failUnlessIsInstance(QTSampleBufferExplicitSceneChange, unicode)
        self.failUnlessIsInstance(QTSampleBufferTimeStampDiscontinuitySceneChange, unicode)

        self.failUnlessEqual(QTSampleBufferAudioBufferListOptionAssure16ByteAlignment, 1)

    def testMethods(self):
        self.failUnlessResultIsBOOL(QTSampleBuffer.getAudioStreamPacketDescriptions_inRange_)



if __name__ == "__main__":
    main()
