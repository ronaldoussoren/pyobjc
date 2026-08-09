import MediaToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level, NoObjCClass
import objc
import AVFoundation
import CoreFoundation
import CoreMedia
import CoreAudio
import pathlib
import contextlib
import tempfile
import itertools
import os


@contextlib.contextmanager
def saved_system_stderr():
    storage = []

    with tempfile.TemporaryFile() as fp:
        saved = os.dup(2)
        try:
            os.dup2(fp.fileno(), 2)
            yield storage
        finally:
            os.dup2(saved, 2)
            fp.seek(0)
            storage.append(fp.read().decode())


class TestMTAudioProcessingTap(TestCase):
    def test_cftypess(self):
        self.assertIsCFType(MediaToolbox.MTAudioProcessingTapRef)

    def test_functions(self):
        self.assertIsInstance(MediaToolbox.MTAudioProcessingTapGetTypeID(), int)

        self.assertArgIsOut(MediaToolbox.MTAudioProcessingTapGetSourceAudio, 3)
        self.assertArgIsOut(MediaToolbox.MTAudioProcessingTapGetSourceAudio, 4)
        self.assertArgIsOut(MediaToolbox.MTAudioProcessingTapGetSourceAudio, 5)

        # XXX: These two funtions should be tested manually:
        MediaToolbox.MTAudioProcessingTapGetStorage
        MediaToolbox.MTAudioProcessingTapCreate

        events = []

        def init(tap, info, pstorage):
            events.append(("init", tap, info, pstorage))
            return storage

        def finalize(tap):
            events.append("finalize")

        def prepare(tap, maxFrames, processingFormat):
            events.append(("prepare", tap, maxFrames, processingFormat))

        def unprepare(tap):
            events.append("unprepare")

        def process(tap, numberFrames, flags, bufferList, numberFramesOut, flagsOut):
            events.append(
                (
                    "process",
                    tap,
                    numberFrames,
                    flags,
                    bufferList,
                    numberFramesOut,
                    flagsOut,
                )
            )
            return bufferList, numberFrames, 0

        context = object()
        storage = object()

        with self.assertRaisesRegex(TypeError, "expected 4 arguments, got 0"):
            MediaToolbox.MTAudioProcessingTapCreate()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            MediaToolbox.MTAudioProcessingTapCreate(
                NoObjCClass(),
                (0, context, init, finalize, prepare, unprepare, process),
                0,
                None,
            )

        with self.assertRaisesRegex(ValueError, "callbacks should be tuple of 7 items"):
            MediaToolbox.MTAudioProcessingTapCreate(
                None,
                (0, context, init, finalize, prepare),
                0,
                None,
            )

        with self.assertRaisesRegex(
            ValueError, r"callbacks\[0] must be kMTAudioProcessingTapCallbacksVersion_0"
        ):
            MediaToolbox.MTAudioProcessingTapCreate(
                None,
                (1, context, init, finalize, prepare, unprepare, process),
                0,
                None,
            )

        with self.assertRaisesRegex(ValueError, r"callbacks\[2] should be callable"):
            MediaToolbox.MTAudioProcessingTapCreate(
                None,
                (0, context, 42, finalize, prepare, unprepare, process),
                0,
                None,
            )

        with self.assertRaisesRegex(ValueError, r"callbacks\[3] should be callable"):
            MediaToolbox.MTAudioProcessingTapCreate(
                None,
                (0, context, None, 42, prepare, unprepare, process),
                0,
                None,
            )

        with self.assertRaisesRegex(ValueError, r"callbacks\[4] should be callable"):
            MediaToolbox.MTAudioProcessingTapCreate(
                None,
                (0, context, init, None, 42, unprepare, process),
                0,
                None,
            )

        with self.assertRaisesRegex(ValueError, r"callbacks\[5] should be callable"):
            MediaToolbox.MTAudioProcessingTapCreate(
                None,
                (0, context, init, finalize, None, 42, process),
                0,
                None,
            )

        with self.assertRaisesRegex(ValueError, r"callbacks\[6] should be callable"):
            MediaToolbox.MTAudioProcessingTapCreate(
                None,
                (0, context, init, finalize, prepare, None, 42),
                0,
                None,
            )

        with self.assertRaisesRegex(ValueError, r"callbacks\[6] should be callable"):
            MediaToolbox.MTAudioProcessingTapCreate(
                None,
                (0, context, init, finalize, prepare, unprepare, None),
                0,
                None,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            MediaToolbox.MTAudioProcessingTapCreate(
                None,
                (0, context, init, finalize, prepare, unprepare, process),
                "doit",
                None,
            )

        with self.assertRaisesRegex(ValueError, "'tapOut' should be None"):
            MediaToolbox.MTAudioProcessingTapCreate(
                None,
                (0, context, init, finalize, prepare, unprepare, process),
                0,
                42,
            )

        err, tap = MediaToolbox.MTAudioProcessingTapCreate(
            None,
            (0, context, init, finalize, prepare, unprepare, process),
            0,
            None,
        )
        self.assertNotEqual(err, 0)
        self.assertIs(tap, None)

        err, tap = MediaToolbox.MTAudioProcessingTapCreate(
            None,
            (0, context, init, finalize, prepare, unprepare, process),
            MediaToolbox.kMTAudioProcessingTapCreationFlag_PostEffects,
            None,
        )
        self.assertEqual(err, 0)
        self.assertIsInstance(tap, MediaToolbox.MTAudioProcessingTapRef)

        self.assertEqual(events[0], ("init", tap, context, None))

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 0"):
            MediaToolbox.MTAudioProcessingTapGetStorage()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            MediaToolbox.MTAudioProcessingTapGetStorage(NoObjCClass())

        self.assertIs(MediaToolbox.MTAudioProcessingTapGetStorage(tap), storage)

        del tap

        def init_raises(tap, info, pstorage):
            raise RuntimeError("init failed")

        with saved_system_stderr() as stderr:
            err, tap = MediaToolbox.MTAudioProcessingTapCreate(
                None,
                (0, context, init_raises, finalize, prepare, unprepare, process),
                MediaToolbox.kMTAudioProcessingTapCreationFlag_PostEffects,
                None,
            )
        self.assertIn("Ignoring exception in MTAudioProcessing callback", stderr[0])
        self.assertIn("RuntimeError: init failed", stderr[0])
        self.assertEqual(err, 0)
        self.assertIsInstance(tap, MediaToolbox.MTAudioProcessingTapRef)
        self.assertIs(MediaToolbox.MTAudioProcessingTapGetStorage(tap), None)

    @min_os_level("27.0")
    def test_functions27_0(self):
        events = []

        def init(tap, info, pstorage):
            events.append(("init", tap, info, pstorage))
            return storage

        def finalize(tap):
            events.append("finalize")

        def prepare(tap, maxFrames, processingFormat):
            events.append(("prepare", tap, maxFrames, processingFormat))

        def unprepare(tap):
            events.append("unprepare")

        def process(tap, numberFrames, flags, bufferList, numberFramesOut, flagsOut):
            events.append(
                (
                    "process",
                    tap,
                    numberFrames,
                    flags,
                    bufferList,
                    numberFramesOut,
                    flagsOut,
                )
            )
            return bufferList, numberFrames, 0

        context = object()
        storage = object()

        status, format_descr = CoreMedia.CMAudioFormatDescriptionCreate(
            None,
            CoreAudio.AudioStreamBasicDescription(
                mSampleRate=44100.0,
                mFormatID=CoreAudio.kAudioFormatLinearPCM,
                mFormatFlags=CoreAudio.kAudioFormatFlagIsSignedInteger
                | CoreAudio.kAudioFormatFlagIsPacked,
                mBytesPerPacket=4,
                mFramesPerPacket=1,
                mBytesPerFrame=2,
                mChannelsPerFrame=2,
                mBitsPerChannel=16,
            ),
            0,
            None,
            0,
            None,
            None,
            None,
        )
        self.assertEqual(status, 0)

        with self.assertRaisesRegex(TypeError, "expected 5 arguments, got 0"):
            MediaToolbox.MTAudioProcessingTapCreateWithPreferredFormat()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            MediaToolbox.MTAudioProcessingTapCreateWithPreferredFormat(
                NoObjCClass(),
                (0, context, init, finalize, prepare, unprepare, process),
                0,
                format_descr,
                None,
            )
        with self.assertRaisesRegex(ValueError, "callbacks should be tuple of 7 items"):
            MediaToolbox.MTAudioProcessingTapCreateWithPreferredFormat(
                None,
                (0, context, init, finalize, prepare),
                0,
                format_descr,
                None,
            )

        with self.assertRaisesRegex(
            ValueError, r"callbacks\[0] must be kMTAudioProcessingTapCallbacksVersion_0"
        ):
            MediaToolbox.MTAudioProcessingTapCreateWithPreferredFormat(
                None,
                (1, context, init, finalize, prepare, unprepare, process),
                0,
                format_descr,
                None,
            )

        with self.assertRaisesRegex(ValueError, r"callbacks\[2] should be callable"):
            MediaToolbox.MTAudioProcessingTapCreateWithPreferredFormat(
                None,
                (0, context, 42, finalize, prepare, unprepare, process),
                0,
                format_descr,
                None,
            )

        with self.assertRaisesRegex(ValueError, r"callbacks\[3] should be callable"):
            MediaToolbox.MTAudioProcessingTapCreateWithPreferredFormat(
                None,
                (0, context, None, 42, prepare, unprepare, process),
                0,
                format_descr,
                None,
            )

        with self.assertRaisesRegex(ValueError, r"callbacks\[4] should be callable"):
            MediaToolbox.MTAudioProcessingTapCreateWithPreferredFormat(
                None,
                (0, context, init, None, 42, unprepare, process),
                0,
                format_descr,
                None,
            )

        with self.assertRaisesRegex(ValueError, r"callbacks\[5] should be callable"):
            MediaToolbox.MTAudioProcessingTapCreateWithPreferredFormat(
                None,
                (0, context, init, finalize, None, 42, process),
                0,
                format_descr,
                None,
            )

        with self.assertRaisesRegex(ValueError, r"callbacks\[6] should be callable"):
            MediaToolbox.MTAudioProcessingTapCreateWithPreferredFormat(
                None,
                (0, context, init, finalize, prepare, None, 42),
                0,
                format_descr,
                None,
            )

        with self.assertRaisesRegex(ValueError, r"callbacks\[6] should be callable"):
            MediaToolbox.MTAudioProcessingTapCreateWithPreferredFormat(
                None,
                (0, context, init, finalize, prepare, unprepare, None),
                0,
                format_descr,
                None,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            MediaToolbox.MTAudioProcessingTapCreateWithPreferredFormat(
                None,
                (0, context, init, finalize, prepare, unprepare, process),
                "doit",
                format_descr,
                None,
            )

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            MediaToolbox.MTAudioProcessingTapCreateWithPreferredFormat(
                None,
                (0, context, init, finalize, prepare, unprepare, process),
                0,
                NoObjCClass(),
                None,
            )

        with self.assertRaisesRegex(ValueError, "'tapOut' should be None"):
            MediaToolbox.MTAudioProcessingTapCreateWithPreferredFormat(
                None,
                (0, context, init, finalize, prepare, unprepare, process),
                0,
                format_descr,
                42,
            )

        err, tap = MediaToolbox.MTAudioProcessingTapCreateWithPreferredFormat(
            None,
            (0, context, init, finalize, prepare, unprepare, process),
            MediaToolbox.kMTAudioProcessingTapCreationFlag_PostEffects,
            format_descr,
            None,
        )
        self.assertEqual(err, 0)
        self.assertIsInstance(tap, MediaToolbox.MTAudioProcessingTapRef)

        self.assertEqual(events[0], ("init", tap, context, None))

    def test_constants(self):
        self.assertEqual(
            MediaToolbox.kMTAudioProcessingTapCreationFlag_PreEffects, 1 << 0
        )
        self.assertEqual(
            MediaToolbox.kMTAudioProcessingTapCreationFlag_PostEffects, 1 << 1
        )

        self.assertEqual(MediaToolbox.kMTAudioProcessingTapFlag_StartOfStream, 1 << 8)
        self.assertEqual(MediaToolbox.kMTAudioProcessingTapFlag_EndOfStream, 1 << 9)

        self.assertEqual(MediaToolbox.kMTAudioProcessingTapCallbacksVersion_0, 0)

    def test_using(self):
        track = pathlib.Path(__file__).parent / "testtrack.m4a"
        self.assertTrue(track.is_file())

        asset = AVFoundation.AVAsset.assetWithURL_(track)
        self.assertIsNot(asset, None)

        playerItem = AVFoundation.AVPlayerItem.playerItemWithAsset_(asset)
        self.assertIsNot(playerItem, None)

        audioTrack = asset.tracks()[0]
        self.assertIsNot(audioTrack, None)

        record = []

        def init(tap, options, storage):
            record.append(("init", repr(tap), options, storage))
            return options

        def finalize(tap):
            record.append(("finalize", repr(tap)))

        def prepare(tap, maxFrames, processingFormat):
            record.append(("prepare", id(tap), maxFrames, processingFormat))

        def unprepare(tap):
            record.append(("unprepare", repr(tap)))

        def process(tap, numberFrames, flags, bufferList, numberFramesOut, flagsOut):
            _, flags, _timeRange, numberFramesOut = (
                MediaToolbox.MTAudioProcessingTapGetSourceAudio(
                    tap, numberFrames, bufferList, None, None, None
                )
            )
            bl = [len(item.mData) for item in bufferList]
            record.append(
                ("process", str(tap), numberFrames, flags, bl, numberFramesOut)
            )
            return bufferList, numberFramesOut, flags

        def setup():
            callbacks = (0, object(), init, finalize, prepare, unprepare, process)

            err, tap = MediaToolbox.MTAudioProcessingTapCreate(
                None,
                callbacks,
                MediaToolbox.kMTAudioProcessingTapCreationFlag_PostEffects,
                None,
            )
            assert err == 0

            inputParams = AVFoundation.AVMutableAudioMixInputParameters.audioMixInputParametersWithTrack_(
                audioTrack
            )
            inputParams.setAudioTapProcessor_(tap)

            audioMix = AVFoundation.AVMutableAudioMix.audioMix()
            audioMix.setInputParameters_([inputParams])

            playerItem.setAudioMix_(audioMix)
            player = AVFoundation.AVPlayer.playerWithPlayerItem_(playerItem)
            return player

        with objc.autorelease_pool():
            with objc.autorelease_pool():
                player = setup()
                assert player is not None

            player.play()

            # Avoid actually playing sound:
            player.setVolume_(0)

            CoreFoundation.CFRunLoopRunInMode(
                CoreFoundation.kCFRunLoopDefaultMode, 2, False
            )

            player.currentItem().setAudioMix_(None)

            CoreFoundation.CFRunLoopRunInMode(
                CoreFoundation.kCFRunLoopDefaultMode, 0.5, False
            )
            CoreFoundation.CFRunLoopRunInMode(
                CoreFoundation.kCFRunLoopDefaultMode, 0.5, False
            )

            self.assertEqual(record[0][0], "init")
            self.assertEqual(record[1][0], "prepare")

            for rec in record[2:-2]:
                self.assertEqual(rec[0], "process")

            self.assertEqual(record[-2][0], "unprepare")
            self.assertEqual(record[-1][0], "finalize")

    def test_using_failed(self):
        track = pathlib.Path(__file__).parent / "testtrack.m4a"
        self.assertTrue(track.is_file())

        def init(tap, options, storage):
            return options

        def finalize(tap):
            raise RuntimeError("finalize failed")

        def prepare(tap, maxFrames, processingFormat):
            raise RuntimeError("prepare failed")

        def unprepare(tap):
            raise RuntimeError("unprepare error")

        counter = itertools.count()

        def process(tap, numberFrames, flags, bufferList, numberFramesOut, flagsOut):
            _, flags, _timeRange, numberFramesOut = (
                MediaToolbox.MTAudioProcessingTapGetSourceAudio(
                    tap, numberFrames, bufferList, None, None, None
                )
            )
            val = next(counter)
            if val == 0:
                raise RuntimeError("process failed")
            elif val == 1:
                return 42
            elif val == 2:
                return ()
            elif val == 3:
                return (bufferList, "20", flags)
            elif val == 4:
                return (bufferList, numberFramesOut, b"flags")
            else:
                return None, numberFramesOut, flags

        def setup():
            asset = AVFoundation.AVAsset.assetWithURL_(track)
            self.assertIsNot(asset, None)

            playerItem = AVFoundation.AVPlayerItem.playerItemWithAsset_(asset)
            self.assertIsNot(playerItem, None)

            audioTrack = asset.tracks()[0]
            self.assertIsNot(audioTrack, None)

            callbacks = (0, object(), init, None, prepare, unprepare, process)

            err, tap = MediaToolbox.MTAudioProcessingTapCreate(
                None,
                callbacks,
                MediaToolbox.kMTAudioProcessingTapCreationFlag_PostEffects,
                None,
            )
            self.assertEqual(err, 0)

            inputParams = AVFoundation.AVMutableAudioMixInputParameters.audioMixInputParametersWithTrack_(
                audioTrack
            )
            inputParams.setAudioTapProcessor_(tap)

            audioMix = AVFoundation.AVMutableAudioMix.audioMix()
            audioMix.setInputParameters_([inputParams])

            playerItem.setAudioMix_(audioMix)
            player = AVFoundation.AVPlayer.playerWithPlayerItem_(playerItem)
            return player

        with saved_system_stderr() as stderr:
            with objc.autorelease_pool():
                with objc.autorelease_pool():
                    player = setup()
                    assert player is not None

                player.play()

                # Avoid actually playing sound:
                player.setVolume_(0)

                CoreFoundation.CFRunLoopRunInMode(
                    CoreFoundation.kCFRunLoopDefaultMode, 2, False
                )

                player.currentItem().setAudioMix_(None)

                CoreFoundation.CFRunLoopRunInMode(
                    CoreFoundation.kCFRunLoopDefaultMode, 0.5, False
                )
                CoreFoundation.CFRunLoopRunInMode(
                    CoreFoundation.kCFRunLoopDefaultMode, 0.5, False
                )
                del player

        print(stderr[0])
        self.assertIn("Ignoring exception in MTAudioProcessing callback", stderr[0])
        self.assertIn("RuntimeError: prepare failed", stderr[0])
        self.assertIn("RuntimeError: process failed", stderr[0])
        self.assertIn(
            "TypeError: MTAudioProcessing processing callback should return (bufferListInOut, numFrames, flags)",
            stderr[0],
        )
        self.assertIn("ValueError: depythonifying 'long long', got 'str'", stderr[0])
        self.assertIn(
            "ValueError: depythonifying 'unsigned int', got 'bytes'", stderr[0]
        )
        self.assertIn("RuntimeError: unprepare error", stderr[0])
        # self.assertIn("RuntimeError: finalize failed", stderr[0])

        self.assertGreater(next(counter), 5)

        # See #677
        # self.fail("actually using the failing 'finalize' in this test crashes'")
