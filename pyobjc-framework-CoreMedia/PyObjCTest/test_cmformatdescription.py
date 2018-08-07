from PyObjCTools.TestSupport import *

import CoreMedia

class TestCMFormatDescription (TestCase):
    def test_constants(self):
        self.assertEqual(CoreMedia.kCMFormatDescriptionError_InvalidParameter, -12710)
        self.assertEqual(CoreMedia.kCMFormatDescriptionError_AllocationFailed, -12711)
        self.assertEqual(CoreMedia.kCMFormatDescriptionError_ValueNotAvailable, -12718)

        self.assertEqual(CoreMedia.kCMMediaType_Video, fourcc(b'vide'))
        self.assertEqual(CoreMedia.kCMMediaType_Audio, fourcc(b'soun'))
        self.assertEqual(CoreMedia.kCMMediaType_Muxed, fourcc(b'muxx'))
        self.assertEqual(CoreMedia.kCMMediaType_Text, fourcc(b'text'))
        self.assertEqual(CoreMedia.kCMMediaType_ClosedCaption, fourcc(b'clcp'))
        self.assertEqual(CoreMedia.kCMMediaType_Subtitle, fourcc(b'sbtl'))
        self.assertEqual(CoreMedia.kCMMediaType_TimeCode, fourcc(b'tmcd'))
        self.assertEqual(CoreMedia.kCMMediaType_Metadata, fourcc(b'meta'))

        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes422, fourcc(b'apcn'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes422LT, fourcc(b'apcs'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProRes422Proxy, fourcc(b'apco'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProResRAW, fourcc(b'aprn'))
        self.assertEqual(CoreMedia.kCMVideoCodecType_AppleProResRAWHQ, fourcc(b'aprh'))


    @min_os_level('10.7')
    def test_constants10_7(self):
        kCMFormatDescriptionExtension_OriginalCompressionSettings
        kCMFormatDescriptionExtension_SampleDescriptionExtensionAtoms
        kCMFormatDescriptionExtension_VerbatimSampleDescription
        kCMFormatDescriptionExtension_VerbatimISOSampleEntry

        # XXX:


    def test_types(self):
        self.assertIsCFType(CoreMedia.CMFormatDescriptionRef)

    @min_os_level('10.7')
    def test_functions(self):
        self.assertArgIsOut(CoreMedia.CMFormatDescriptionCreate, 4)
        self.assertArgIsCFRetained(CoreMedia.CMFormatDescriptionCreate, 4)

        self.assertIsInstance(CoreMedia.CMFormatDescriptionGetTypeID(), (int, long))

        self.assertResultIsBOOL(CoreMedia.CMFormatDescriptionEqual)

        self.assertResultIsBOOL(CoreMedia.CMFormatDescriptionEqualIgnoringExtensionKeys)

        CoreMedia.CMFormatDescriptionGetMediaType
        CoreMedia.CMFormatDescriptionGetMediaSubType
        CoreMedia.CMFormatDescriptionGetExtensions
        CoreMedia.CMFormatDescriptionGetExtension

        self.assertArgIsOut(CoreMedia.CMAudioFormatDescriptionCreate, 6)
        self.assertArgIsCFRetained(CoreMedia.CMAudioFormatDescriptionCreate, 6)

        CoreMedia.CMAudioFormatDescriptionGetStreamBasicDescription

        self.assertArgIsOut(CoreMedia.CMAudioFormatDescriptionGetMagicCookie, 1)
        self.assertResultSizeInArg(CoreMedia.CMAudioFormatDescriptionGetMagicCookie, 1)

        self.assertArgIsOut(CoreMedia.CMAudioFormatDescriptionGetChannelLayout, 1)
        self.assertResultSizeInArg(CoreMedia.CMAudioFormatDescriptionGetChannelLayout, 1)

        self.assertArgIsOut(CoreMedia.CMAudioFormatDescriptionGetFormatList, 1)
        self.assertResultSizeInArg(CoreMedia.CMAudioFormatDescriptionGetFormatList, 1)

        CoreMedia.CMAudioFormatDescriptionGetRichestDecodableFormat

        self.fail()

if __name__ == "__main__":
    main()
