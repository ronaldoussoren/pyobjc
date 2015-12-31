from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAudioSequencer (TestCase):
    def testConstants(self):
        self.assertEqual(AVFoundation.AVMusicSequenceLoadSMF_PreserveTracks, 0)
        self.assertEqual(AVFoundation.AVMusicSequenceLoadSMF_ChannelsToTracks, 1)

        self.assertEqual(AVFoundation.AVMusicTrackLoopCountForever, -1)

    def testStructs(self):
        v = AVFoundation.AVBeatRange()
        self.assertIsInstance(v.start, float)
        self.assertIsInstance(v.length, float)

    @min_os_level('10.11')
    def testFunctions(self):
        v = AVFoundation.AVMakeBeatRange(1.5, 2.5)
        self.assertIsInstance(v, AVFoundation.AVBeatRange)
        self.assertEqual(v.start, 1.5)
        self.assertEqual(v.length, 2.5)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioSequencer.loadFromURL_options_error_)
        self.assertArgIsOut(AVFoundation.AVAudioSequencer.loadFromURL_options_error_, 2)

        self.assertResultIsBOOL(AVFoundation.AVAudioSequencer.loadFromData_options_error_)
        self.assertArgIsOut(AVFoundation.AVAudioSequencer.loadFromData_options_error_, 2)

        self.assertResultIsBOOL(AVFoundation.AVAudioSequencer.writeToURL_SMPTEResolution_replaceExisting_error_)
        self.assertArgIsBOOL(AVFoundation.AVAudioSequencer.writeToURL_SMPTEResolution_replaceExisting_error_, 2)
        self.assertArgIsOut(AVFoundation.AVAudioSequencer.writeToURL_SMPTEResolution_replaceExisting_error_, 3)

        self.assertArgIsOut(AVFoundation.AVAudioSequencer.dataWithSMPTEResolution_error_, 1)

        self.assertResultIsBOOL(AVFoundation.AVAudioSequencer.isPlaying)

        self.assertArgIsOut(AVFoundation.AVAudioSequencer.hostTimeForBeats_error_, 1)
        self.assertArgIsOut(AVFoundation.AVAudioSequencer.beatsForHostTime_error_, 1)

        self.assertResultIsBOOL(AVFoundation.AVAudioSequencer.startAndReturnError_)
        self.assertArgIsOut(AVFoundation.AVAudioSequencer.startAndReturnError_, 0)

        self.assertResultIsBOOL(AVFoundation.AVMusicTrack.isLoopingEnabled)
        self.assertArgIsBOOL(AVFoundation.AVMusicTrack.setLoopingEnabled_, 0)

        self.assertResultIsBOOL(AVFoundation.AVMusicTrack.isMuted)
        self.assertArgIsBOOL(AVFoundation.AVMusicTrack.setMuted_, 0)

        self.assertResultIsBOOL(AVFoundation.AVMusicTrack.isSoloed)
        self.assertArgIsBOOL(AVFoundation.AVMusicTrack.setSoloed_, 0)

if __name__ == "__main__":
    main()
