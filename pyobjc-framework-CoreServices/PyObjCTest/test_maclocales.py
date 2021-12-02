import CoreServices
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestMacLocales(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), f"{name!r} exposed in bindings"
        )

    def test_constants(self):
        self.assertEqual(CoreServices.kLocaleLanguageMask, 1 << 0)
        self.assertEqual(CoreServices.kLocaleLanguageVariantMask, 1 << 1)
        self.assertEqual(CoreServices.kLocaleScriptMask, 1 << 2)
        self.assertEqual(CoreServices.kLocaleScriptVariantMask, 1 << 3)
        self.assertEqual(CoreServices.kLocaleRegionMask, 1 << 4)
        self.assertEqual(CoreServices.kLocaleRegionVariantMask, 1 << 5)
        self.assertEqual(CoreServices.kLocaleAllPartsMask, 0x0000003F)

        self.assertEqual(CoreServices.kLocaleNameMask, 1 << 0)
        self.assertEqual(CoreServices.kLocaleOperationVariantNameMask, 1 << 1)
        self.assertEqual(CoreServices.kLocaleAndVariantNameMask, 0x00000003)

    def test_structs(self):
        v = CoreServices.LocaleAndVariant()
        self.assertEqual(v.locale, None)
        self.assertEqual(v.opVariant, 0)
        self.assertPickleRoundTrips(v)

    def test_functions(self):
        self.assertArgIsOut(CoreServices.LocaleRefFromLangOrRegionCode, 2)
        self.assertArgIsOut(CoreServices.LocaleRefFromLocaleString, 1)

        self.assertArgIsOut(CoreServices.LocaleRefGetPartString, 3)
        # self.assertArgSizeInArg(CoreServices.LocaleRefGetPartString, 3, 2) #
        self.assertArgIsNullTerminated(CoreServices.LocaleRefGetPartString, 3)

        self.assertArgIsIn(CoreServices.LocaleStringToLangAndRegionCodes, 0)
        self.assertArgIsNullTerminated(CoreServices.LocaleStringToLangAndRegionCodes, 0)
        self.assertArgIsOut(CoreServices.LocaleStringToLangAndRegionCodes, 1)
        self.assertArgIsOut(CoreServices.LocaleStringToLangAndRegionCodes, 2)

        self.assert_not_wrapped("LocaleOperationCountLocales")
        self.assert_not_wrapped("LocaleOperationGetLocales")
        self.assert_not_wrapped("LocaleGetName")
        self.assert_not_wrapped("LocaleCountNames")
        self.assert_not_wrapped("LocaleGetIndName")
        self.assert_not_wrapped("LocaleGetRegionLanguageName")

        self.assertArgIsOut(CoreServices.LocaleOperationGetName, 3)
        self.assertArgIsOut(CoreServices.LocaleOperationGetName, 4)
        self.assertArgSizeInArg(CoreServices.LocaleOperationGetName, 4, (2, 3))

        self.assertArgIsOut(CoreServices.LocaleOperationGetIndName, 3)
        self.assertArgIsOut(CoreServices.LocaleOperationGetIndName, 4)
        self.assertArgSizeInArg(CoreServices.LocaleOperationGetIndName, 4, (2, 3))
        self.assertArgIsOut(CoreServices.LocaleOperationGetIndName, 5)

    @expectedFailure
    def test_functions_not_present(self):
        self.assertArgIsOut(
            CoreServices.LocaleOperationCountNames.LocaleOperationGetName, 1
        )
