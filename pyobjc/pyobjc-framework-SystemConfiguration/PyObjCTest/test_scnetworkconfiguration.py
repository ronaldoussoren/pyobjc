from PyObjCTools.TestSupport import *

from SystemConfiguration import *
import sys

class TestSCNetworkConfiguration (TestCase):

    def testTypes(self):
        self.assertTrue(isinstance(SCNetworkInterfaceRef, objc.objc_class))
        self.assertTrue(isinstance(SCBondStatusRef, objc.objc_class))
        self.assertTrue(isinstance(SCNetworkProtocolRef, objc.objc_class))
        self.assertTrue(isinstance(SCNetworkServiceRef, objc.objc_class))
        self.assertTrue(isinstance(SCNetworkSetRef, objc.objc_class))

        self.assertTrue(SCBondInterfaceRef is SCNetworkInterfaceRef)
        self.assertTrue(SCVLANInterfaceRef is SCNetworkInterfaceRef)


    def testConstants(self):
        self.assertTrue(isinstance(kSCNetworkInterfaceType6to4, unicode))
        self.assertTrue(isinstance(kSCNetworkInterfaceTypeBluetooth, unicode))
        self.assertTrue(isinstance(kSCNetworkInterfaceTypeBond, unicode))
        self.assertTrue(isinstance(kSCNetworkInterfaceTypeEthernet, unicode))
        self.assertTrue(isinstance(kSCNetworkInterfaceTypeFireWire, unicode))
        self.assertTrue(isinstance(kSCNetworkInterfaceTypeIEEE80211, unicode))
        self.assertTrue(isinstance(kSCNetworkInterfaceTypeL2TP, unicode))
        self.assertTrue(isinstance(kSCNetworkInterfaceTypeIrDA, unicode))
        self.assertTrue(isinstance(kSCNetworkInterfaceTypeModem, unicode))
        self.assertTrue(isinstance(kSCNetworkInterfaceTypePPP, unicode))
        self.assertTrue(isinstance(kSCNetworkInterfaceTypePPTP, unicode))
        self.assertTrue(isinstance(kSCNetworkInterfaceTypeSerial, unicode))
        self.assertTrue(isinstance(kSCNetworkInterfaceTypeVLAN, unicode))
        self.assertTrue(isinstance(kSCNetworkInterfaceTypeWWAN, unicode))
        self.assertTrue(isinstance(kSCNetworkInterfaceTypeIPv4, unicode))

        self.assertTrue(isinstance(kSCNetworkInterfaceIPv4, SCNetworkInterfaceRef))

        self.assertEquals(kSCBondStatusOK, 0)
        self.assertEquals(kSCBondStatusLinkInvalid, 1)
        self.assertEquals(kSCBondStatusNoPartner, 2)
        self.assertEquals(kSCBondStatusNotInActiveGroup, 3)
        self.assertEquals(kSCBondStatusUnknown, 999)

        self.assertTrue(isinstance(kSCBondStatusDeviceAggregationStatus, unicode))
        self.assertTrue(isinstance(kSCBondStatusDeviceCollecting, unicode))
        self.assertTrue(isinstance(kSCBondStatusDeviceDistributing, unicode))

        self.assertTrue(isinstance(kSCNetworkProtocolTypeAppleTalk, unicode))
        self.assertTrue(isinstance(kSCNetworkProtocolTypeDNS, unicode))
        self.assertTrue(isinstance(kSCNetworkProtocolTypeIPv4, unicode))
        self.assertTrue(isinstance(kSCNetworkProtocolTypeIPv6, unicode))
        self.assertTrue(isinstance(kSCNetworkProtocolTypeProxies, unicode))
        self.assertTrue(isinstance(kSCNetworkProtocolTypeSMB, unicode))

    def testFunctions(self):
        r = SCNetworkInterfaceGetTypeID()
        self.assertTrue(isinstance(r, (int, long)))

        r = SCNetworkInterfaceCopyAll()
        self.assertTrue(isinstance(r, CFArrayRef))
        self.assertTrue(len(r) > 0)

        for iface in r:
            if SCNetworkInterfaceGetBSDName(iface).startswith('en'):
                break
        r = SCNetworkInterfaceGetSupportedInterfaceTypes(iface)
        self.assertTrue(isinstance(r, CFArrayRef))
        self.assertTrue(isinstance(r[0], unicode))

        r = SCNetworkInterfaceGetSupportedProtocolTypes(iface)
        self.assertTrue(isinstance(r, CFArrayRef))
        self.assertTrue(isinstance(r[0], unicode))

        r = SCNetworkInterfaceCreateWithInterface(iface, kSCNetworkInterfaceTypeL2TP)
        self.assertTrue(r is None or isinstance(r, SCNetworkInterfaceRef))

        r = SCNetworkInterfaceGetBSDName(iface)
        self.assertTrue(isinstance(r, unicode))

        r = SCNetworkInterfaceGetConfiguration(iface)
        self.assertTrue(r is None or isinstance(r, CFDictionaryRef))

        r = SCNetworkInterfaceGetExtendedConfiguration(iface, "EAPOL")
        self.assertTrue(r is None or isinstance(r, CFDictionaryRef))

        r = SCNetworkInterfaceGetHardwareAddressString(iface)
        self.assertTrue(isinstance(r, unicode))

        r = SCNetworkInterfaceGetInterface(iface)
        self.assertTrue(r is None)

        r = SCNetworkInterfaceGetInterfaceType(iface)
        self.assertTrue(isinstance(r, unicode))

        r = SCNetworkInterfaceGetLocalizedDisplayName(iface)
        self.assertTrue(isinstance(r, unicode))

        r = SCNetworkInterfaceSetConfiguration(iface, {})
        self.assertTrue(r is True or r is False)

        r = SCNetworkInterfaceSetExtendedConfiguration(iface, "OC", {})
        self.assertTrue(r is True or r is False)

        r, current, active, available = SCNetworkInterfaceCopyMediaOptions(iface,
                None, None, None, False)
        self.assertTrue(r is True)
        self.assertTrue(isinstance(current, CFDictionaryRef))
        self.assertTrue(isinstance(active, CFDictionaryRef))
        self.assertTrue(isinstance(available, CFArrayRef))

        r = SCNetworkInterfaceCopyMediaSubTypes(available)
        self.assertTrue(isinstance(r, CFArrayRef))
        for item in r:
            self.assertTrue(isinstance(item, unicode))

        r = SCNetworkInterfaceCopyMediaSubTypeOptions(available, r[1])
        self.assertTrue(isinstance(r, CFArrayRef))

        if sys.byteorder == 'little':
            # These tests crash in Rosetta on an intel machine::
            #
            #   Unhandled transform (1) for ioctl group = 105 (i), number = 68, length = 32
            #   Illegal instruction

            # I haven't filed a bug for this yet.

            r, mtu_cur, mtu_min, mtu_max = SCNetworkInterfaceCopyMTU(iface, None, None, None)
            self.assertTrue(r is True)
            self.assertTrue(isinstance(mtu_cur, (int, long)))
            self.assertTrue(isinstance(mtu_min, (int, long)))
            self.assertTrue(isinstance(mtu_max, (int, long)))
            r = SCNetworkInterfaceSetMediaOptions(iface,
                current['MediaSubType'],
                current['MediaOptions'])
            self.assertTrue(r is True or r is False)

            r = SCNetworkInterfaceSetMTU(iface, mtu_cur)
            self.assertTrue(r is True or r is False)

            r = SCNetworkInterfaceForceConfigurationRefresh(iface)
            self.assertTrue(r is True or r is False)

        prefs = SCPreferencesCreate(None, "SystemConfiguration", None)
        self.assertTrue(isinstance(prefs, SCPreferencesRef))

        a = SCBondInterfaceCopyAll(prefs)
        self.assertTrue(isinstance(a, CFArrayRef))

        a = SCBondInterfaceCopyAvailableMemberInterfaces(prefs)
        self.assertTrue(isinstance(a, CFArrayRef))

        iface = SCBondInterfaceCreate(prefs)
        self.assertTrue(iface is None or isinstance(iface, SCBondInterfaceRef))

        if iface is not None:
            a = SCBondInterfaceGetMemberInterfaces(iface)
            self.assertTrue(isinstance(a, CFArrayRef))

            o = SCBondInterfaceGetOptions(iface)
            self.assertTrue(o is None or isinstance(o, CFDictionaryRef))

            r = SCBondInterfaceSetMemberInterfaces(iface, SCNetworkInterfaceCopyAll())
            self.assertTrue(r is True or r is False)

            r = SCBondInterfaceSetLocalizedDisplayName(iface, "pyobjc.bond")
            self.assertTrue(r is True or r is False)
           

            r = SCBondInterfaceSetOptions(iface, {})
            self.assertTrue(r is True or r is False)

            st = SCBondInterfaceCopyStatus(iface)
            self.assertTrue(st is None or isinstance(st, SCBondStatusRef))

            a = SCBondStatusGetMemberInterfaces(iface)
            self.assertTrue(a is None or isinstance(a, CFArrayRef))

            st = SCBondStatusGetInterfaceStatus(iface, None)
            self.assertTrue(a is None or isinstance(a, CFDictionaryRef))

            r = SCBondInterfaceRemove(iface)
            self.assertTrue(r is True)


        r = SCBondStatusGetTypeID()
        self.assertTrue(isinstance(r, (int, long)))

        a = SCVLANInterfaceCopyAll(prefs)
        self.assertTrue(isinstance(a, CFArrayRef))

        a = SCVLANInterfaceCopyAvailablePhysicalInterfaces()
        self.assertTrue(isinstance(a, CFArrayRef))

        iface = SCVLANInterfaceCreate(prefs, a[0], 99)
        self.assertTrue(isinstance(iface, SCVLANInterfaceRef))

        r = SCVLANInterfaceGetPhysicalInterface(iface)
        self.assertEqual(r, a[0])

        t = SCVLANInterfaceGetTag(iface)
        self.assertEquals(t, 99)

        t = SCVLANInterfaceGetOptions(iface)
        self.assertTrue(t is None or isinstance(t, CFDictionaryRef))

        r = SCVLANInterfaceSetPhysicalInterfaceAndTag(iface, a[0], 42)
        self.assertIs(r, True)

        r = SCVLANInterfaceSetLocalizedDisplayName(iface, "octest")
        self.assertIs(r, True)

        r = SCVLANInterfaceSetOptions(iface, {"name": "foo"})
        self.assertIs(r, True)

        t = SCVLANInterfaceGetOptions(iface)
        self.assertTrue(isinstance(t, CFDictionaryRef))

        r = SCVLANInterfaceRemove(iface)
        self.assertTrue(r is True)

        r = SCNetworkProtocolGetTypeID()
        self.assertTrue(isinstance(r, (int, long)))

        r = SCNetworkServiceGetTypeID()
        self.assertTrue(isinstance(r, (int, long)))

        r = SCNetworkSetGetTypeID()
        self.assertTrue(isinstance(r, (int, long)))

        r = SCNetworkServiceCopyAll(prefs)
        self.assertIsInstance(r, CFArrayRef)

        serv = r[0]
        self.assertIsInstance(serv, SCNetworkServiceRef)
        prot = SCNetworkServiceCopyProtocol(serv, kSCNetworkProtocolTypeIPv4)
        self.assertIsInstance(prot, SCNetworkProtocolRef)

        conf = SCNetworkProtocolGetConfiguration(prot)
        self.assertIsInstance(conf, CFDictionaryRef)

        enabled = SCNetworkProtocolGetEnabled(prot)
        self.assertIsInstance(enabled, bool)

        pr = SCNetworkProtocolGetProtocolType(prot)
        self.assertIsInstance(pr, unicode)

        v = SCNetworkProtocolSetConfiguration(prot, conf)
        self.assertIsInstance(v, bool)

        v = SCNetworkProtocolSetEnabled(prot, enabled)
        self.assertIsInstance(v, bool)

        v = SCNetworkServiceAddProtocolType(serv, pr)
        self.assertIsInstance(v, bool)


        v = SCNetworkServiceCopyProtocols(serv)
        self.assertIsInstance(v, CFArrayRef)
        if v:
            self.assertIsInstance(v[0], SCNetworkProtocolRef)


        iface = SCNetworkServiceGetInterface(serv)
        self.assertIsInstance(iface, SCNetworkInterfaceRef)

        v = SCNetworkServiceCreate(prefs, iface)
        self.assertIsInstance(v, SCNetworkServiceRef)

        v = s2 = SCNetworkServiceCopy(prefs, SCNetworkServiceGetServiceID(serv))
        self.assertIsInstance(v, SCNetworkServiceRef)

        v = SCNetworkServiceGetEnabled(serv)
        self.assertIsInstance(v, bool)

        v = SCNetworkServiceGetName(serv)
        self.assertIsInstance(v, unicode)

        self.assertResultIsCFRetained(SCNetworkServiceCopyProtocol)

        v = SCNetworkServiceRemoveProtocolType(s2, kSCNetworkProtocolTypeIPv4)
        self.assertIsInstance(v, bool)

        v = SCNetworkServiceRemove(s2)
        self.assertIsInstance(v, bool)

        v = SCNetworkServiceSetEnabled(serv, SCNetworkServiceGetEnabled(serv))
        self.assertIsInstance(v, bool)

        v = SCNetworkServiceSetName(serv, SCNetworkServiceGetName(serv))
        self.assertIsInstance(v, bool)

        set = SCNetworkSetCopyCurrent(prefs)
        self.assertIsInstance(set, SCNetworkSetRef)

        s2 = SCNetworkServiceCopy(prefs, SCNetworkServiceGetServiceID(serv))

        v = SCNetworkSetAddService(set,  s2)
        self.assertIsInstance(v, bool)


        v  = SCNetworkSetContainsInterface(set, iface)
        self.assertIsInstance(v, bool)

        v = SCNetworkSetCopyAll(prefs)
        self.assertIsInstance(v, CFArrayRef)

        v = SCNetworkSetCopyServices(set)
        self.assertIsInstance(v, CFArrayRef)

        v = SCNetworkSetCreate(prefs)
        self.assertIsInstance(v, SCNetworkSetRef)

        v = SCNetworkSetCopy(prefs, SCNetworkSetGetSetID(set))
        self.assertIsInstance(v, SCNetworkSetRef)

        v = SCNetworkSetRemove(v)
        self.assertIsInstance(v, bool)

        v = SCNetworkSetGetName(set)
        self.assertIsInstance(v, unicode)

        v = SCNetworkSetGetSetID(set)
        self.assertIsInstance(v, unicode)

        v = SCNetworkSetGetServiceOrder(set)
        self.assertIsInstance(v, CFArrayRef)

        v = SCNetworkSetSetName(set, SCNetworkSetGetName(set))
        self.assertIsInstance(v, bool)

        v = SCNetworkSetSetServiceOrder(set, SCNetworkSetGetServiceOrder(set))
        self.assertIsInstance(v, bool)

        v = SCNetworkSetSetCurrent(SCNetworkSetCopyCurrent(prefs))
        self.assertIsInstance(v, bool)


    @min_os_level('10.5')
    def testFunctions10_5(self):
        prefs = SCPreferencesCreate(None, "SystemConfiguration", None)
        self.assertTrue(isinstance(prefs, SCPreferencesRef))

        r = SCNetworkServiceCopyAll(prefs)
        self.assertIsInstance(r, CFArrayRef)
        serv = SCNetworkServiceCopy(prefs, SCNetworkServiceGetServiceID(r[0]))

        v = SCNetworkServiceEstablishDefaultConfiguration(serv)
        self.assertIsInstance(v, bool)

        

if __name__ == "__main__":
    main()
