from PyObjCTools.TestSupport import TestCase

import Virtualization


class TestVZMACAddress(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Virtualization.VZMACAddress.isBroadcastAddress)
        self.assertResultIsBOOL(Virtualization.VZMACAddress.isMulticastAddress)
        self.assertResultIsBOOL(Virtualization.VZMACAddress.isUnicastAddress)
        self.assertResultIsBOOL(
            Virtualization.VZMACAddress.isLocallyAdministeredAddress
        )
        self.assertResultIsBOOL(
            Virtualization.VZMACAddress.isUniversallyAdministeredAddress
        )
