from PyObjCTools.TestSupport import *

from SystemConfiguration import *

class TestSCNetworkConfiguration (TestCase):

    def testTypes(self):
        self.failUnless(isinstance(SCNetworkInterfaceRef, objc.objc_class))
        self.failUnless(isinstance(SCBondStatusRef, objc.objc_class))
        self.failUnless(isinstance(SCNetworkProtocolRef, objc.objc_class))
        self.failUnless(isinstance(SCNetworkServiceRef, objc.objc_class))
        self.failUnless(isinstance(SCNetworkSetRef, objc.objc_class))

        self.failUnless(SCBondInterfaceRef is SCNetworkInterfaceRef)
        self.failUnless(SCVLANInterfaceRef is SCNetworkInterfaceRef)


    def testConstants(self):
        self.failUnless(isinstance(kSCNetworkInterfaceType6to4, unicode))
        self.failUnless(isinstance(kSCNetworkInterfaceTypeBluetooth, unicode))
        self.failUnless(isinstance(kSCNetworkInterfaceTypeBond, unicode))
        self.failUnless(isinstance(kSCNetworkInterfaceTypeEthernet, unicode))
        self.failUnless(isinstance(kSCNetworkInterfaceTypeFireWire, unicode))
        self.failUnless(isinstance(kSCNetworkInterfaceTypeIEEE80211, unicode))
        self.failUnless(isinstance(kSCNetworkInterfaceTypeL2TP, unicode))
        self.failUnless(isinstance(kSCNetworkInterfaceTypeIrDA, unicode))
        self.failUnless(isinstance(kSCNetworkInterfaceTypeModem, unicode))
        self.failUnless(isinstance(kSCNetworkInterfaceTypePPP, unicode))
        self.failUnless(isinstance(kSCNetworkInterfaceTypePPTP, unicode))
        self.failUnless(isinstance(kSCNetworkInterfaceTypeSerial, unicode))
        self.failUnless(isinstance(kSCNetworkInterfaceTypeVLAN, unicode))
        self.failUnless(isinstance(kSCNetworkInterfaceTypeWWAN, unicode))
        self.failUnless(isinstance(kSCNetworkInterfaceTypeIPv4, unicode))

        self.failUnless(isinstance(kSCNetworkInterfaceIPv4, SCNetworkInterfaceRef))

        self.assertEquals(kSCBondStatusOK, 0)
        self.assertEquals(kSCBondStatusLinkInvalid, 1)
        self.assertEquals(kSCBondStatusNoPartner, 2)
        self.assertEquals(kSCBondStatusNotInActiveGroup, 3)
        self.assertEquals(kSCBondStatusUnknown, 999)

        self.failUnless(isinstance(kSCBondStatusDeviceAggregationStatus, unicode))
        self.failUnless(isinstance(kSCBondStatusDeviceCollecting, unicode))
        self.failUnless(isinstance(kSCBondStatusDeviceDistributing, unicode))

        self.failUnless(isinstance(kSCNetworkProtocolTypeAppleTalk, unicode))
        self.failUnless(isinstance(kSCNetworkProtocolTypeDNS, unicode))
        self.failUnless(isinstance(kSCNetworkProtocolTypeIPv4, unicode))
        self.failUnless(isinstance(kSCNetworkProtocolTypeIPv6, unicode))
        self.failUnless(isinstance(kSCNetworkProtocolTypeProxies, unicode))
        self.failUnless(isinstance(kSCNetworkProtocolTypeSMB, unicode))

    def testFunctions(self):

        r = SCNetworkInterfaceGetTypeID()
        self.failUnless(isinstance(r, (int, long)))

        r = SCNetworkInterfaceCopyAll()
        self.failUnless(isinstance(r, CFArrayRef))
        self.failUnless(len(r) > 0)

        for iface in r:
            if SCNetworkInterfaceGetBSDName(iface).startswith('en'):
                break

        r = SCNetworkInterfaceGetSupportedInterfaceTypes(iface)
        self.failUnless(isinstance(r, CFArrayRef))
        self.failUnless(isinstance(r[0], unicode))

        r = SCNetworkInterfaceGetSupportedProtocolTypes(iface)
        self.failUnless(isinstance(r, CFArrayRef))
        self.failUnless(isinstance(r[0], unicode))

        r = SCNetworkInterfaceCreateWithInterface(iface, kSCNetworkInterfaceTypeL2TP)
        self.failUnless(r is None or isinstance(r, SCNetworkInterfaceRef))

        r = SCNetworkInterfaceGetBSDName(iface)
        self.failUnless(isinstance(r, unicode))

        r = SCNetworkInterfaceGetConfiguration(iface)
        self.failUnless(r is None or isinstance(r, CFDictionaryRef))

        r = SCNetworkInterfaceGetExtendedConfiguration(iface, "EAPOL")
        self.failUnless(r is None or isinstance(r, CFDictionaryRef))

        r = SCNetworkInterfaceGetHardwareAddressString(iface)
        self.failUnless(isinstance(r, unicode))

        r = SCNetworkInterfaceGetInterface(iface)
        self.failUnless(r is None)

        r = SCNetworkInterfaceGetInterfaceType(iface)
        self.failUnless(isinstance(r, unicode))

        r = SCNetworkInterfaceGetLocalizedDisplayName(iface)
        self.failUnless(isinstance(r, unicode))

        r = SCNetworkInterfaceSetConfiguration(iface, {})
        self.failUnless(r is True or r is False)

        r = SCNetworkInterfaceSetExtendedConfiguration(iface, "OC", {})
        self.failUnless(r is True or r is False)

        r, current, active, available = SCNetworkInterfaceCopyMediaOptions(iface,
                None, None, None, False)
        self.failUnless(r is True)
        self.failUnless(isinstance(current, CFDictionaryRef))
        self.failUnless(isinstance(active, CFDictionaryRef))
        self.failUnless(isinstance(available, CFArrayRef))

        r = SCNetworkInterfaceCopyMediaSubTypes(available)
        self.failUnless(isinstance(r, CFArrayRef))
        for item in r:
            self.failUnless(isinstance(item, unicode))

        r = SCNetworkInterfaceCopyMediaSubTypeOptions(available, r[1])
        self.failUnless(isinstance(r, CFArrayRef))

        r, mtu_cur, mtu_min, mtu_max = SCNetworkInterfaceCopyMTU(iface, None, None, None)
        self.failUnless(r is True)
        self.failUnless(isinstance(mtu_cur, (int, long)))
        self.failUnless(isinstance(mtu_min, (int, long)))
        self.failUnless(isinstance(mtu_max, (int, long)))

        r = SCNetworkInterfaceSetMediaOptions(iface,
                current['MediaSubType'],
                current['MediaOptions'])
        self.failUnless(r is True or r is False)

        r = SCNetworkInterfaceSetMTU(iface, mtu_cur)
        self.failUnless(r is True or r is False)

        r = SCNetworkInterfaceForceConfigurationRefresh(iface)
        self.failUnless(r is True or r is False)

        prefs = SCPreferencesCreate(None, "SystemConfiguration", None)
        self.failUnless(isinstance(prefs, SCPreferencesRef))

        a = SCBondInterfaceCopyAll(prefs)
        self.failUnless(isinstance(a, CFArrayRef))

        a = SCBondInterfaceCopyAvailableMemberInterfaces(prefs)
        self.failUnless(isinstance(a, CFArrayRef))

        iface = SCBondInterfaceCreate(prefs)
        self.failUnless(iface is None or isinstance(iface, SCBondInterfaceRef))

        if iface is not None:
            a = SCBondInterfaceGetMemberInterfaces(iface)
            self.failUnless(isinstance(a, CFArrayRef))

            o = SCBondInterfaceGetOptions(iface)
            self.failUnless(o is None or isinstance(o, CFDictionaryRef))

            r = SCBondInterfaceSetMemberInterfaces(iface, SCNetworkInterfaceCopyAll())
            self.failUnless(r is True or r is False)

            r = SCBondInterfaceSetLocalizedDisplayName(iface, "pyobjc.bond")
            self.failUnless(r is True or r is False)
           

            r = SCBondInterfaceSetOptions(iface, {})
            self.failUnless(r is True or r is False)

            st = SCBondInterfaceCopyStatus(iface)
            self.failUnless(st is None or isinstance(st, SCBondStatusRef))

            a = SCBondStatusGetMemberInterfaces(iface)
            self.failUnless(a is None or isinstance(a, CFArrayRef))

            st = SCBondStatusGetInterfaceStatus(iface, None)
            self.failUnless(a is None or isinstance(a, CFDictionaryRef))

            r = SCBondInterfaceRemove(iface)
            self.failUnless(r is True)

        r = SCBondStatusGetTypeID()
        self.failUnless(isinstance(r, (int, long)))

        a = SCVLANInterfaceCopyAll(prefs)
        self.failUnless(isinstance(a, CFArrayRef))

        a = SCVLANInterfaceCopyAvailablePhysicalInterfaces()
        self.failUnless(isinstance(a, CFArrayRef))

        iface = SCVLANInterfaceCreate(prefs, a[0], 99)
        self.failUnless(isinstance(iface, SCVLANInterfaceRef))

        r = SCVLANInterfaceGetPhysicalInterface(iface)
        self.failUnless(r is a[0])

        t = SCVLANInterfaceGetTag(iface)
        self.assertEquals(t, 99)

        t = SCVLANInterfaceGetOptions(iface)
        self.failUnless(t is None or isinstance(t, CFDictionaryRef))

        r = SCVLANInterfaceSetPhysicalInterfaceAndTag(iface, a[0], 42)
        self.failUnless(r is True)

        r = SCVLANInterfaceSetLocalizedDisplayName(iface, "octest")
        self.failUnless(r is True)

        r = SCVLANInterfaceSetOptions(iface, {"name": "foo"})
        self.failUnless(r is True)

        t = SCVLANInterfaceGetOptions(iface)
        self.failUnless(isinstance(t, CFDictionaryRef))

        r = SCVLANInterfaceRemove(iface)
        self.failUnless(r is True)

        r = SCNetworkProtocolGetTypeID()
        self.failUnless(isinstance(r, (int, long)))

        r = SCNetworkServiceGetTypeID()
        self.failUnless(isinstance(r, (int, long)))

        r = SCNetworkSetGetTypeID()
        self.failUnless(isinstance(r, (int, long)))

        r = SCNetworkServiceCopyAll(prefs)
        self.failUnlessIsInstance(r, CFArrayRef)

        serv = r[0]
        self.failUnlessIsInstance(serv, SCNetworkServiceRef)
        prot = SCNetworkServiceCopyProtocol(serv, kSCNetworkProtocolTypeIPv4)
        self.failUnlessIsInstance(prot, SCNetworkProtocolRef)

        conf = SCNetworkProtocolGetConfiguration(prot)
        self.failUnlessIsInstance(conf, CFDictionaryRef)

        enabled = SCNetworkProtocolGetEnabled(prot)
        self.failUnlessIsInstance(enabled, bool)

        pr = SCNetworkProtocolGetProtocolType(prot)
        self.failUnlessIsInstance(pr, unicode)

        v = SCNetworkProtocolSetConfiguration(prot, conf)
        self.failUnlessIsInstance(v, bool)

        v = SCNetworkProtocolSetEnabled(prot, enabled)
        self.failUnlessIsInstance(v, bool)

        v = SCNetworkServiceAddProtocolType(serv, pr)
        self.failUnlessIsInstance(v, bool)


        v = SCNetworkServiceCopyProtocols(serv)
        self.failUnlessIsInstance(v, CFArrayRef)
        if v:
            self.failUnlessIsInstance(v[0], SCNetworkProtocolRef)


        iface = SCNetworkServiceGetInterface(serv)
        self.failUnlessIsInstance(iface, SCNetworkInterfaceRef)

        v = SCNetworkServiceCreate(prefs, iface)
        self.failUnlessIsInstance(v, SCNetworkServiceRef)

        v = s2 = SCNetworkServiceCopy(prefs, SCNetworkServiceGetServiceID(serv))
        self.failUnlessIsInstance(v, SCNetworkServiceRef)

        v = SCNetworkServiceGetEnabled(serv)
        self.failUnlessIsInstance(v, bool)

        v = SCNetworkServiceGetName(serv)
        self.failUnlessIsInstance(v, unicode)

        self.failUnlessResultIsCFRetained(SCNetworkServiceCopyProtocol)

        v = SCNetworkServiceRemoveProtocolType(s2, kSCNetworkProtocolTypeIPv4)
        self.failUnlessIsInstance(v, bool)

        v = SCNetworkServiceRemove(s2)
        self.failUnlessIsInstance(v, bool)

        v = SCNetworkServiceSetEnabled(serv, SCNetworkServiceGetEnabled(serv))
        self.failUnlessIsInstance(v, bool)

        v = SCNetworkServiceSetName(serv, SCNetworkServiceGetName(serv))
        self.failUnlessIsInstance(v, bool)

        set = SCNetworkSetCopyCurrent(prefs)
        self.failUnlessIsInstance(set, SCNetworkSetRef)

        s2 = SCNetworkServiceCopy(prefs, SCNetworkServiceGetServiceID(serv))

        v = SCNetworkSetAddService(set,  s2)
        self.failUnlessIsInstance(v, bool)


        v  = SCNetworkSetContainsInterface(set, iface)
        self.failUnlessIsInstance(v, bool)

        v = SCNetworkSetCopyAll(prefs)
        self.failUnlessIsInstance(v, CFArrayRef)

        v = SCNetworkSetCopyServices(set)
        self.failUnlessIsInstance(v, CFArrayRef)

        v = SCNetworkSetCreate(prefs)
        self.failUnlessIsInstance(v, SCNetworkSetRef)

        v = SCNetworkSetCopy(prefs, SCNetworkSetGetSetID(set))
        self.failUnlessIsInstance(v, SCNetworkSetRef)

        v = SCNetworkSetRemove(v)
        self.failUnlessIsInstance(v, bool)

        v = SCNetworkSetGetName(set)
        self.failUnlessIsInstance(v, unicode)

        v = SCNetworkSetGetSetID(set)
        self.failUnlessIsInstance(v, unicode)

        v = SCNetworkSetGetServiceOrder(set)
        self.failUnlessIsInstance(v, CFArrayRef)

        v = SCNetworkSetSetName(set, SCNetworkSetGetName(set))
        self.failUnlessIsInstance(v, bool)

        v = SCNetworkSetSetServiceOrder(set, SCNetworkSetGetServiceOrder(set))
        self.failUnlessIsInstance(v, bool)

        v = SCNetworkSetSetCurrent(SCNetworkSetCopyCurrent(prefs))
        self.failUnlessIsInstance(v, bool)


    @min_os_level('10.5')
    def testFunctions10_5(self):
        prefs = SCPreferencesCreate(None, "SystemConfiguration", None)
        self.failUnless(isinstance(prefs, SCPreferencesRef))

        r = SCNetworkServiceCopyAll(prefs)
        self.failUnlessIsInstance(r, CFArrayRef)
        serv = SCNetworkServiceCopy(prefs, SCNetworkServiceGetServiceID(r[0]))

        v = SCNetworkServiceEstablishDefaultConfiguration(serv)
        self.failUnlessIsInstance(v, bool)

        

if __name__ == "__main__":
    main()
