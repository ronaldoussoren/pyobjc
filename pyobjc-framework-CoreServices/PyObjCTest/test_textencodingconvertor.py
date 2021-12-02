import CoreServices
from PyObjCTools.TestSupport import TestCase, fourcc


class TestTextEncodingConvertor(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), f"{name!r} exposed in bindings"
        )

    def test_constants(self):
        self.assertEqual(CoreServices.kTECSignature, fourcc(b"encv"))
        self.assertEqual(CoreServices.kTECUnicodePluginSignature, fourcc(b"puni"))
        self.assertEqual(CoreServices.kTECJapanesePluginSignature, fourcc(b"pjpn"))
        self.assertEqual(CoreServices.kTECChinesePluginSignature, fourcc(b"pzho"))
        self.assertEqual(CoreServices.kTECKoreanPluginSignature, fourcc(b"pkor"))

        self.assertEqual(CoreServices.kTECInternetNameDefaultUsageMask, 0)
        self.assertEqual(CoreServices.kTECInternetNameStrictUsageMask, 1)
        self.assertEqual(CoreServices.kTECInternetNameTolerantUsageMask, 2)

        self.assertEqual(CoreServices.kTEC_MIBEnumDontCare, -1)

        self.assertEqual(CoreServices.kTECDisableFallbacksBit, 16)
        self.assertEqual(CoreServices.kTECDisableLooseMappingsBit, 17)

        self.assertEqual(
            CoreServices.kTECDisableFallbacksMask,
            1 << CoreServices.kTECDisableFallbacksBit,
        )
        self.assertEqual(
            CoreServices.kTECDisableLooseMappingsMask,
            1 << CoreServices.kTECDisableLooseMappingsBit,
        )

    def test_types(self):
        self.assertIsOpaquePointer(CoreServices.TECObjectRef)
        self.assertIsOpaquePointer(CoreServices.TECSnifferObjectRef)

    def test_structs(self):
        v = CoreServices.TECConversionInfo()
        self.assertEqual(v.sourceEncoding, 0)
        self.assertEqual(v.destinationEncoding, 0)
        self.assertEqual(v.reserved1, 0)
        self.assertEqual(v.reserved2, 0)
        self.assertPickleRoundTrips(v)

    def test_functions(self):
        self.assertArgIsOut(CoreServices.TECCountAvailableTextEncodings, 0)

        self.assertArgIsOut(CoreServices.TECGetAvailableTextEncodings, 0)
        self.assertArgSizeInArg(CoreServices.TECGetAvailableTextEncodings, 0, (1, 2))
        self.assertArgIsOut(CoreServices.TECGetAvailableTextEncodings, 2)

        self.assertArgIsOut(CoreServices.TECCountDirectTextEncodingConversions, 0)

        self.assertArgIsOut(CoreServices.TECGetDirectTextEncodingConversions, 0)
        self.assertArgSizeInArg(
            CoreServices.TECGetDirectTextEncodingConversions, 0, (1, 2)
        )
        self.assertArgIsOut(CoreServices.TECGetDirectTextEncodingConversions, 2)

        self.assertArgIsOut(CoreServices.TECCountDestinationTextEncodings, 1)

        self.assertArgIsOut(CoreServices.TECGetDestinationTextEncodings, 1)
        self.assertArgSizeInArg(CoreServices.TECGetDestinationTextEncodings, 1, (2, 3))
        self.assertArgIsOut(CoreServices.TECGetDestinationTextEncodings, 3)

        self.assertArgIsOut(CoreServices.TECGetTextEncodingInternetName, 1)

        # self.assertArgIsIn(CoreServices.TECGetTextEncodingFromInternetName, 0)
        CoreServices.TECGetTextEncodingFromInternetName

        self.assertArgIsOut(CoreServices.TECCreateConverter, 0)

        self.assertArgIsOut(CoreServices.TECCreateConverterFromPath, 0)
        self.assertArgIsIn(CoreServices.TECCreateConverterFromPath, 1)
        self.assertArgSizeInArg(CoreServices.TECCreateConverterFromPath, 1, 2)

        CoreServices.TECDisposeConverter
        CoreServices.TECClearConverterContextInfo

        self.assertArgIsIn(CoreServices.TECConvertText, 1)
        self.assertArgSizeInArg(CoreServices.TECConvertText, 1, 2)
        self.assertArgIsOut(CoreServices.TECConvertText, 3)
        self.assertArgIsOut(CoreServices.TECConvertText, 4)
        self.assertArgSizeInArg(CoreServices.TECConvertText, 4, (5, 6))
        self.assertArgIsOut(CoreServices.TECConvertText, 6)

        self.assertArgIsOut(CoreServices.TECFlushText, 1)
        self.assertArgSizeInArg(CoreServices.TECFlushText, 1, (2, 3))
        self.assertArgIsOut(CoreServices.TECFlushText, 3)

        self.assertArgIsOut(CoreServices.TECCountSubTextEncodings, 1)

        self.assertArgIsOut(CoreServices.TECGetSubTextEncodings, 1)
        self.assertArgSizeInArg(CoreServices.TECGetSubTextEncodings, 1, (2, 3))
        self.assertArgIsOut(CoreServices.TECGetSubTextEncodings, 3)

        self.assert_not_wrapped("TECGetEncodingList")

        self.assertArgIsOut(CoreServices.TECCreateOneToManyConverter, 0)
        self.assertArgIsIn(CoreServices.TECCreateOneToManyConverter, 3)
        self.assertArgSizeInArg(CoreServices.TECCreateOneToManyConverter, 3, 2)

        self.assertArgIsIn(CoreServices.TECConvertTextToMultipleEncodings, 1)
        self.assertArgSizeInArg(CoreServices.TECConvertTextToMultipleEncodings, 1, 2)
        self.assertArgIsOut(CoreServices.TECConvertTextToMultipleEncodings, 3)
        self.assertArgIsOut(CoreServices.TECConvertTextToMultipleEncodings, 4)
        self.assertArgSizeInArg(
            CoreServices.TECConvertTextToMultipleEncodings, 4, (5, 6)
        )
        self.assertArgIsOut(CoreServices.TECConvertTextToMultipleEncodings, 6)
        self.assertArgIsOut(CoreServices.TECConvertTextToMultipleEncodings, 7)
        self.assertArgSizeInArg(
            CoreServices.TECConvertTextToMultipleEncodings, 7, (8, 9)
        )
        self.assertArgIsOut(CoreServices.TECConvertTextToMultipleEncodings, 9)

        self.assertArgIsOut(CoreServices.TECFlushMultipleEncodings, 1)
        self.assertArgSizeInArg(CoreServices.TECFlushMultipleEncodings, 1, (2, 3))
        self.assertArgIsOut(CoreServices.TECFlushMultipleEncodings, 3)
        self.assertArgIsOut(CoreServices.TECFlushMultipleEncodings, 4)
        self.assertArgSizeInArg(CoreServices.TECFlushMultipleEncodings, 4, (5, 6))
        self.assertArgIsOut(CoreServices.TECFlushMultipleEncodings, 6)

        self.assertArgIsOut(CoreServices.TECCountWebTextEncodings, 1)

        self.assertArgIsOut(CoreServices.TECGetWebTextEncodings, 1)
        self.assertArgSizeInArg(CoreServices.TECGetWebTextEncodings, 1, (2, 3))
        self.assertArgIsOut(CoreServices.TECGetWebTextEncodings, 3)

        self.assertArgIsOut(CoreServices.TECCountMailTextEncodings, 1)

        self.assertArgIsOut(CoreServices.TECGetMailTextEncodings, 1)
        self.assertArgSizeInArg(CoreServices.TECGetMailTextEncodings, 1, (2, 3))
        self.assertArgIsOut(CoreServices.TECGetMailTextEncodings, 3)

        self.assertArgIsOut(CoreServices.TECCountAvailableSniffers, 0)

        self.assertArgIsOut(CoreServices.TECGetAvailableSniffers, 0)
        self.assertArgSizeInArg(CoreServices.TECGetAvailableSniffers, 0, (1, 2))
        self.assertArgIsOut(CoreServices.TECGetAvailableSniffers, 2)

        self.assertArgIsOut(CoreServices.TECCreateSniffer, 0)
        self.assertArgIsIn(CoreServices.TECCreateSniffer, 1)
        self.assertArgSizeInArg(CoreServices.TECCreateSniffer, 1, 2)

        self.assertArgIsIn(CoreServices.TECSniffTextEncoding, 1)
        self.assertArgSizeInArg(CoreServices.TECSniffTextEncoding, 1, 2)
        self.assertArgIsOut(CoreServices.TECSniffTextEncoding, 3)
        self.assertArgSizeInArg(CoreServices.TECSniffTextEncoding, 3, 4)
        self.assertArgIsOut(CoreServices.TECSniffTextEncoding, 5)
        self.assertArgSizeInArg(CoreServices.TECSniffTextEncoding, 5, 6)
        self.assertArgIsOut(CoreServices.TECSniffTextEncoding, 7)
        self.assertArgSizeInArg(CoreServices.TECSniffTextEncoding, 7, 8)

        CoreServices.TECDisposeSniffer
        CoreServices.TECClearSnifferContextInfo
        CoreServices.TECSetBasicOptions

        self.assertArgIsOut(CoreServices.TECCopyTextEncodingInternetNameAndMIB, 2)
        self.assertArgIsCFRetained(
            CoreServices.TECCopyTextEncodingInternetNameAndMIB, 2
        )
        self.assertArgIsOut(CoreServices.TECCopyTextEncodingInternetNameAndMIB, 3)

        self.assertArgIsOut(CoreServices.TECGetTextEncodingFromInternetNameOrMIB, 0)
