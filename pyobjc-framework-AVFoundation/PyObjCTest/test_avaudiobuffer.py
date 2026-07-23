import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestAVAudioBuffer(TestCase):
    @min_os_level("10.11")
    def test_methods(self):
        self.assertResultIsVariableSize(
            AVFoundation.AVAudioCompressedBuffer.packetDescriptions
        )
        self.assertResultIsVariableSize(AVFoundation.AVAudioCompressedBuffer.data)

    @expectedFailure
    def test_methods_manual(self):
        # Not quite sure how to test this
        self.fail("check floatChannelData,int16ChannelData, int32ChannelData")

    @min_os_level("12.0")
    def test_methods12_0(self):
        # No special handling is needed for the audiobufferlist, this type has
        # special handling in the CoreAudio bindings
        self.assertArgIsBlock(
            AVFoundation.AVAudioPCMBuffer.initWithPCMFormat_bufferListNoCopy_deallocator_,
            2,
            b"v^{AudioBufferList=I[1{AudioBuffer=II^v}]}",
        )

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsVariableSize(
            AVFoundation.AVAudioCompressedBuffer.packetDependencies
        )

    @min_os_level("12.0")
    def test_manual_bindings(self):
        fmt = AVFoundation.AVAudioFormat.alloc().initStandardFormatWithSampleRate_channels_(
            42000, 2
        )
        buf = AVFoundation.AVAudioPCMBuffer.alloc().initWithPCMFormat_frameCapacity_(
            fmt, 100000
        )
        r = buf.floatChannelData()
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 2)
        for item in r:
            self.assertIsInstance(item, objc.varlist)
            self.assertEqual(item.__typestr__, objc._C_FLT)

        self.assertIs(buf.int16ChannelData(), None)
        self.assertIs(buf.int32ChannelData(), None)

        imp = buf.methodForSelector_(b"floatChannelData")
        r = imp(buf)
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 2)

        fmt = AVFoundation.AVAudioFormat.alloc().initWithCommonFormat_sampleRate_channels_interleaved_(
            AVFoundation.AVAudioPCMFormatInt16, 42000, 2, True
        )
        buf = AVFoundation.AVAudioPCMBuffer.alloc().initWithPCMFormat_frameCapacity_(
            fmt, 100000
        )
        self.assertIs(buf.floatChannelData(), None)
        self.assertIs(buf.int32ChannelData(), None)

        r = buf.int16ChannelData()
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 2)
        for item in r:
            self.assertIsInstance(item, objc.varlist)
            self.assertEqual(item.__typestr__, objc._C_SHT)

        imp = buf.methodForSelector_(b"int16ChannelData")
        r = imp(buf)
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 2)

        fmt = AVFoundation.AVAudioFormat.alloc().initWithCommonFormat_sampleRate_channels_interleaved_(
            AVFoundation.AVAudioPCMFormatInt32, 42000, 2, True
        )
        buf = AVFoundation.AVAudioPCMBuffer.alloc().initWithPCMFormat_frameCapacity_(
            fmt, 100000
        )
        self.assertIs(buf.floatChannelData(), None)
        self.assertIs(buf.int16ChannelData(), None)

        r = buf.int32ChannelData()
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 2)
        for item in r:
            self.assertIsInstance(item, objc.varlist)
            self.assertEqual(item.__typestr__, objc._C_INT)

        imp = buf.methodForSelector_(b"int32ChannelData")
        r = imp(buf)
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 2)

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 1"):
            buf.floatChannelData(1)

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 1"):
            buf.int16ChannelData(1)

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 1"):
            buf.int32ChannelData(1)
