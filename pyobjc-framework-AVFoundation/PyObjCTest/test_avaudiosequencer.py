import AVFoundation
import sys
from PyObjCTools.TestSupport import TestCase, min_os_level

AVAudioSequencerUserCallback = b"v@@d"
AVMusicEventEnumerationBlock = b"v@N^dN^Z"


class TestAVAudioSequencer(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVMusicSequenceLoadOptions)
        self.assertIsEnumType(AVFoundation.AVMusicTrackLoopCount)
        self.assertIsTypedEnum(AVFoundation.AVAudioSequencerInfoDictionaryKey, str)

    def testConstants(self):
        self.assertEqual(AVFoundation.AVMusicSequenceLoadSMF_PreserveTracks, 0)
        self.assertEqual(
            AVFoundation.AVMusicSequenceLoadSMF_ChannelsToTracks, 1
        )  # noqa: B950

        self.assertEqual(AVFoundation.AVMusicTrackLoopCountForever, -1)

        self.assertEqual(AVFoundation.AVMusicTimeStampEndOfTrack, sys.float_info.max)

    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(AVFoundation.AVAudioSequencerInfoDictionaryKeyAlbum, str)
        self.assertIsInstance(
            AVFoundation.AVAudioSequencerInfoDictionaryKeyApproximateDurationInSeconds,
            str,
        )
        self.assertIsInstance(AVFoundation.AVAudioSequencerInfoDictionaryKeyArtist, str)
        self.assertIsInstance(
            AVFoundation.AVAudioSequencerInfoDictionaryKeyChannelLayout, str
        )
        self.assertIsInstance(
            AVFoundation.AVAudioSequencerInfoDictionaryKeyComments, str
        )
        self.assertIsInstance(
            AVFoundation.AVAudioSequencerInfoDictionaryKeyComposer, str
        )
        self.assertIsInstance(
            AVFoundation.AVAudioSequencerInfoDictionaryKeyCopyright, str
        )
        self.assertIsInstance(
            AVFoundation.AVAudioSequencerInfoDictionaryKeyEncodingApplication, str
        )
        self.assertIsInstance(AVFoundation.AVAudioSequencerInfoDictionaryKeyGenre, str)
        self.assertIsInstance(AVFoundation.AVAudioSequencerInfoDictionaryKeyISRC, str)
        self.assertIsInstance(
            AVFoundation.AVAudioSequencerInfoDictionaryKeyKeySignature, str
        )
        self.assertIsInstance(
            AVFoundation.AVAudioSequencerInfoDictionaryKeyLyricist, str
        )
        self.assertIsInstance(
            AVFoundation.AVAudioSequencerInfoDictionaryKeyNominalBitRate, str
        )
        self.assertIsInstance(
            AVFoundation.AVAudioSequencerInfoDictionaryKeyRecordedDate, str
        )
        self.assertIsInstance(
            AVFoundation.AVAudioSequencerInfoDictionaryKeySourceBitDepth, str
        )
        self.assertIsInstance(
            AVFoundation.AVAudioSequencerInfoDictionaryKeySourceEncoder, str
        )
        self.assertIsInstance(
            AVFoundation.AVAudioSequencerInfoDictionaryKeySubTitle, str
        )
        self.assertIsInstance(AVFoundation.AVAudioSequencerInfoDictionaryKeyTempo, str)
        self.assertIsInstance(
            AVFoundation.AVAudioSequencerInfoDictionaryKeyTimeSignature, str
        )
        self.assertIsInstance(AVFoundation.AVAudioSequencerInfoDictionaryKeyTitle, str)
        self.assertIsInstance(
            AVFoundation.AVAudioSequencerInfoDictionaryKeyTrackNumber, str
        )
        self.assertIsInstance(AVFoundation.AVAudioSequencerInfoDictionaryKeyYear, str)

    def testStructs(self):
        v = AVFoundation.AVBeatRange()
        self.assertIsInstance(v.start, float)
        self.assertIsInstance(v.length, float)
        self.assertPickleRoundTrips(v)

    @min_os_level("10.11")
    def testFunctions(self):
        v = AVFoundation.AVMakeBeatRange(1.5, 2.5)
        self.assertIsInstance(v, AVFoundation.AVBeatRange)
        self.assertEqual(v.start, 1.5)
        self.assertEqual(v.length, 2.5)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAudioSequencer.loadFromURL_options_error_
        )
        self.assertArgIsOut(
            AVFoundation.AVAudioSequencer.loadFromURL_options_error_, 2
        )  # noqa: B950

        self.assertResultIsBOOL(
            AVFoundation.AVAudioSequencer.loadFromData_options_error_
        )
        self.assertArgIsOut(
            AVFoundation.AVAudioSequencer.loadFromData_options_error_, 2
        )

        self.assertResultIsBOOL(
            AVFoundation.AVAudioSequencer.writeToURL_SMPTEResolution_replaceExisting_error_  # noqa: B950
        )
        self.assertArgIsBOOL(
            AVFoundation.AVAudioSequencer.writeToURL_SMPTEResolution_replaceExisting_error_,  # noqa: B950
            2,
        )
        self.assertArgIsOut(
            AVFoundation.AVAudioSequencer.writeToURL_SMPTEResolution_replaceExisting_error_,  # noqa: B950
            3,
        )

        self.assertArgIsOut(
            AVFoundation.AVAudioSequencer.dataWithSMPTEResolution_error_, 1
        )

        self.assertResultIsBOOL(AVFoundation.AVAudioSequencer.isPlaying)

        self.assertArgIsOut(
            AVFoundation.AVAudioSequencer.hostTimeForBeats_error_, 1
        )  # noqa: B950
        self.assertArgIsOut(
            AVFoundation.AVAudioSequencer.beatsForHostTime_error_, 1
        )  # noqa: B950

        self.assertResultIsBOOL(
            AVFoundation.AVAudioSequencer.startAndReturnError_
        )  # noqa: B950
        self.assertArgIsOut(
            AVFoundation.AVAudioSequencer.startAndReturnError_, 0
        )  # noqa: B950

        self.assertResultIsBOOL(AVFoundation.AVMusicTrack.isLoopingEnabled)
        self.assertArgIsBOOL(AVFoundation.AVMusicTrack.setLoopingEnabled_, 0)

        self.assertResultIsBOOL(AVFoundation.AVMusicTrack.isMuted)
        self.assertArgIsBOOL(AVFoundation.AVMusicTrack.setMuted_, 0)

        self.assertResultIsBOOL(AVFoundation.AVMusicTrack.isSoloed)
        self.assertArgIsBOOL(AVFoundation.AVMusicTrack.setSoloed_, 0)

    @min_os_level("13.0")
    def testMethods13_0(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioSequencer.removeTrack_)
        self.assertArgIsBlock(
            AVFoundation.AVAudioSequencer.setUserCallback_,
            0,
            AVAudioSequencerUserCallback,
        )

        self.assertResultIsBOOL(AVFoundation.AVMusicTrack.usesAutomatedParameters)
        self.assertArgIsBOOL(AVFoundation.AVMusicTrack.setUsesAutomatedParameters_, 0)

        self.assertArgIsBlock(
            AVFoundation.AVMusicTrack.enumerateEventsInRange_usingBlock_,
            1,
            AVMusicEventEnumerationBlock,
        )
