import OpenDirectory
from PyObjCTools.TestSupport import TestCase


class TestOpenDirectory(TestCase):
    def testConstants(self):
        self.assertIsInstance(OpenDirectory.ODFrameworkErrorDomain, str)

    def testProtocols(self):
        self.assertProtocolExists("ODQueryDelegate")

    def testIntegration(self):
        import CFOpenDirectory

        for nm in dir(CFOpenDirectory):
            with self.subTest(nm):
                cfod = getattr(CFOpenDirectory, nm)
                od = getattr(OpenDirectory, nm)

                self.assertIs(cfod, od, f"{nm!r}, {type(cfod)}, {type(od)}")


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(
            OpenDirectory,
            exclude_attrs={
                # These are private classes on macOS 12 that are picked up
                # in this test and contain problematic methods. Just ignore
                # all of them.
                "CDDServerResponder",
                "CDDebug",
                "CKAssetDownloadStagingManager",
                "CKAtomBatchMutableProxy",
                "CKAtomBatchProxy",
                "CKAtomMutableProxy",
                "CKAtomProxy",
                "CKAtomReferenceMutableProxy",
                "CKAtomReferenceProxy",
                "CKBehaviorOptions",
                "CKDSObjCType",
                "CKDistributedSiteIdentifierMutableProxy",
                "CKDistributedSiteIdentifierProxy",
                "CKDistributedTimestampMutableProxy",
                "CKDistributedTimestampProxy",
                "CKInternalError",
                "CKMergeableValueIDMutableProxy",
                "CKMergeableValueIDProxy",
                "CKObjCType",
                "CKPrettyError",
                "CKSQLiteError",
                "CKUserDefaults",
                "CKXBackingStore",
                "CKXORCWriter",
                "CKXSchema",
                "CKXStructMutableProxyBase",
                "CKXStructProxyBase",
                "CTMessageCenter",
                "CoreTelephonyClient",
                "INDeferredLocalizedString",
                "MLInt64ProbabilityDictionary",
                "MLLoaderEvent",
                "MLModelAsset",
                "MLMultiArrayAsNSArrayWrapper",
                "MLProbabilityDictionary",
                "MLSequnceAsFeatureValueArray",
                "MLStringProbabilityDictionary",
                "RPConnection",
                "StreamingUnzipper",
                "TRIAllocationStatus",
                "TRIExperimentAllocationStatus",
                "TRILevel",
                "TRINamespaceResolver",
                "TRIPBAutocreatedArray",
                "TRIPBAutocreatedDictionary",
                "TRIPBBoolArray",
                "TRIPBBoolBoolDictionary",
                "TRIPBBoolDoubleDictionary",
                "TRIPBBoolEnumDictionary",
                "TRIPBBoolFloatDictionary",
                "TRIPBBoolInt32Dictionary",
                "TRIPBBoolInt64Dictionary",
                "TRIPBBoolObjectDictionary",
                "TRIPBBoolUInt32Dictionary",
                "TRIPBBoolUInt64Dictionary",
                "TRIPBDescriptor",
                "TRIPBEnumDescriptor",
                "TRIPBExtensionDescriptor",
                "TRIPBInt32BoolDictionary",
                "TRIPBInt64BoolDictionary",
                "TRIPBOneofDescriptor",
                "TRIPBStringBoolDictionary",
                "TRIPBUInt32BoolDictionary",
                "TRIPBUInt64BoolDictionary",
                "TRISystemConfiguration",
            },
        )
