from PyObjCTools.TestSupport import TestCase
import AudioVideoBridging
import objc


class TestAVB17221EntityDiscoveryDelegateHelper(AudioVideoBridging.NSObject):
    def didUpdateRemoteEntity_changedProperties_on17221EntityDiscovery_(self, a, b, c):
        pass

    def didUpdateLocalEntity_changedProperties_on17221EntityDiscovery_(self, a, b, c):
        pass


class TestAVB17221EntityDiscoveryDelegate(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AudioVideoBridging.AVB17221EntityPropertyChanged)

    def test_constants(self):
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedTimeToLive, 0x00000001
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedGUID, 0x00000002
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedEntityID, 0x00000002
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedVendorID, 0x00000004
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedModelID, 0x00000008
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedEntityCapabilities,
            0x00000010,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedTalkerStreamSources,
            0x00000020,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedTalkerCapabilities,
            0x00000040,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedListenerStreamSinks,
            0x00000080,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedListenerCapabilities,
            0x00000100,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedControllerCapabilities,
            0x00000200,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedAvailableIndex, 0x00000400
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedASGrandmasterID, 0x00000800
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedGPTPGrandmasterID,
            0x00000800,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedMACAddress, 0x00001000
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedAssociationID, 0x00008000
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedEntityType, 0x00010000
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedIdentifyControlIndex,
            0x00020000,
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedInterfaceIndex, 0x00040000
        )
        self.assertEqual(
            AudioVideoBridging.AVB17221EntityPropertyChangedGPTPDomainNumber, 0x00080000
        )

        self.assertEqual(
            AudioVideoBridging.kAVB17221EntityPropertyChangedShouldntChangeMask,
            (
                AudioVideoBridging.AVB17221EntityPropertyChangedEntityID
                | AudioVideoBridging.AVB17221EntityPropertyChangedVendorID
                | AudioVideoBridging.AVB17221EntityPropertyChangedModelID
                | AudioVideoBridging.AVB17221EntityPropertyChangedTalkerStreamSources
                | AudioVideoBridging.AVB17221EntityPropertyChangedTalkerCapabilities
                | AudioVideoBridging.AVB17221EntityPropertyChangedListenerStreamSinks
                | AudioVideoBridging.AVB17221EntityPropertyChangedListenerCapabilities
                | AudioVideoBridging.AVB17221EntityPropertyChangedControllerCapabilities
                | AudioVideoBridging.AVB17221EntityPropertyChangedMACAddress
                | AudioVideoBridging.AVB17221EntityPropertyChangedAssociationID
                | AudioVideoBridging.AVB17221EntityPropertyChangedEntityType
                | AudioVideoBridging.AVB17221EntityPropertyChangedIdentifyControlIndex
                | AudioVideoBridging.AVB17221EntityPropertyChangedInterfaceIndex
            ),
        )

        self.assertEqual(
            AudioVideoBridging.kAVB17221EntityPropertyChangedCanChangeMask,
            (
                AudioVideoBridging.AVB17221EntityPropertyChangedTimeToLive
                | AudioVideoBridging.AVB17221EntityPropertyChangedAvailableIndex
                | AudioVideoBridging.AVB17221EntityPropertyChangedGPTPGrandmasterID
                | AudioVideoBridging.AVB17221EntityPropertyChangedGPTPDomainNumber
                | AudioVideoBridging.AVB17221EntityPropertyChangedEntityCapabilities
            ),
        )

    def test_protocols(self):
        objc.protocolNamed("AVB17221EntityDiscoveryDelegate")

    def test_methods(self):
        self.assertArgHasType(
            TestAVB17221EntityDiscoveryDelegateHelper.didUpdateRemoteEntity_changedProperties_on17221EntityDiscovery_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestAVB17221EntityDiscoveryDelegateHelper.didUpdateLocalEntity_changedProperties_on17221EntityDiscovery_,
            1,
            objc._C_NSUInteger,
        )
