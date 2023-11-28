from PyObjCTools.TestSupport import TestCase, min_os_level, max_os_level
import SystemConfiguration
import objc


class TestSCNetworkConfiguration(TestCase):
    def testTypes(self):
        self.assertTrue(
            isinstance(SystemConfiguration.SCNetworkInterfaceRef, objc.objc_class)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.SCBondStatusRef, objc.objc_class)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.SCNetworkProtocolRef, objc.objc_class)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.SCNetworkServiceRef, objc.objc_class)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.SCNetworkSetRef, objc.objc_class)
        )

        self.assertTrue(
            SystemConfiguration.SCBondInterfaceRef
            is SystemConfiguration.SCNetworkInterfaceRef
        )
        self.assertTrue(
            SystemConfiguration.SCVLANInterfaceRef
            is SystemConfiguration.SCNetworkInterfaceRef
        )

    def testConstants(self):
        self.assertTrue(
            isinstance(SystemConfiguration.kSCNetworkInterfaceType6to4, str)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.kSCNetworkInterfaceTypeBluetooth, str)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.kSCNetworkInterfaceTypeBond, str)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.kSCNetworkInterfaceTypeEthernet, str)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.kSCNetworkInterfaceTypeFireWire, str)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.kSCNetworkInterfaceTypeIEEE80211, str)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.kSCNetworkInterfaceTypeL2TP, str)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.kSCNetworkInterfaceTypeIrDA, str)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.kSCNetworkInterfaceTypeModem, str)
        )
        self.assertTrue(isinstance(SystemConfiguration.kSCNetworkInterfaceTypePPP, str))
        self.assertTrue(
            isinstance(SystemConfiguration.kSCNetworkInterfaceTypePPTP, str)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.kSCNetworkInterfaceTypeSerial, str)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.kSCNetworkInterfaceTypeVLAN, str)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.kSCNetworkInterfaceTypeWWAN, str)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.kSCNetworkInterfaceTypeIPv4, str)
        )

        self.assertTrue(
            isinstance(
                SystemConfiguration.kSCNetworkInterfaceIPv4,
                SystemConfiguration.SCNetworkInterfaceRef,
            )
        )

        self.assertEqual(SystemConfiguration.kSCBondStatusOK, 0)
        self.assertEqual(SystemConfiguration.kSCBondStatusLinkInvalid, 1)
        self.assertEqual(SystemConfiguration.kSCBondStatusNoPartner, 2)
        self.assertEqual(SystemConfiguration.kSCBondStatusNotInActiveGroup, 3)
        self.assertEqual(SystemConfiguration.kSCBondStatusUnknown, 999)

        self.assertTrue(
            isinstance(SystemConfiguration.kSCBondStatusDeviceAggregationStatus, str)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.kSCBondStatusDeviceCollecting, str)
        )
        self.assertTrue(
            isinstance(SystemConfiguration.kSCBondStatusDeviceDistributing, str)
        )

        self.assertTrue(isinstance(SystemConfiguration.kSCNetworkProtocolTypeDNS, str))
        self.assertTrue(isinstance(SystemConfiguration.kSCNetworkProtocolTypeIPv4, str))
        self.assertTrue(isinstance(SystemConfiguration.kSCNetworkProtocolTypeIPv6, str))
        self.assertTrue(
            isinstance(SystemConfiguration.kSCNetworkProtocolTypeProxies, str)
        )
        self.assertTrue(isinstance(SystemConfiguration.kSCNetworkProtocolTypeSMB, str))

    @max_os_level("10.11")
    def testConstantsUpto10_12(self):
        self.assertTrue(
            isinstance(SystemConfiguration.kSCNetworkProtocolTypeAppleTalk, str)
        )

    @min_os_level("10.6")
    def testConstants10_5(self):
        self.assertIsInstance(SystemConfiguration.kSCNetworkInterfaceTypeIPSec, str)

    def testFunctions(self):
        r = SystemConfiguration.SCNetworkInterfaceGetTypeID()
        self.assertTrue(isinstance(r, int))

        r = SystemConfiguration.SCNetworkInterfaceCopyAll()
        self.assertTrue(isinstance(r, SystemConfiguration.CFArrayRef))
        self.assertTrue(len(r) > 0)

        for iface in r:
            if SystemConfiguration.SCNetworkInterfaceGetBSDName(iface).startswith("en"):
                break

        r = SystemConfiguration.SCNetworkInterfaceGetSupportedInterfaceTypes(iface)
        self.assertTrue(isinstance(r, SystemConfiguration.CFArrayRef))
        self.assertTrue(isinstance(r[0], str))

        r = SystemConfiguration.SCNetworkInterfaceGetSupportedProtocolTypes(iface)
        self.assertTrue(isinstance(r, SystemConfiguration.CFArrayRef))
        self.assertTrue(isinstance(r[0], str))

        r = SystemConfiguration.SCNetworkInterfaceCreateWithInterface(
            iface, SystemConfiguration.kSCNetworkInterfaceTypeL2TP
        )
        self.assertTrue(
            r is None or isinstance(r, SystemConfiguration.SCNetworkInterfaceRef)
        )

        r = SystemConfiguration.SCNetworkInterfaceGetBSDName(iface)
        self.assertTrue(isinstance(r, str))

        r = SystemConfiguration.SCNetworkInterfaceGetConfiguration(iface)
        self.assertTrue(r is None or isinstance(r, SystemConfiguration.CFDictionaryRef))

        r = SystemConfiguration.SCNetworkInterfaceGetExtendedConfiguration(
            iface, "EAPOL"
        )
        self.assertTrue(r is None or isinstance(r, SystemConfiguration.CFDictionaryRef))

        r = SystemConfiguration.SCNetworkInterfaceGetHardwareAddressString(iface)
        self.assertTrue(isinstance(r, str))

        r = SystemConfiguration.SCNetworkInterfaceGetInterface(iface)
        self.assertTrue(r is None)

        r = SystemConfiguration.SCNetworkInterfaceGetInterfaceType(iface)
        self.assertTrue(isinstance(r, str))

        r = SystemConfiguration.SCNetworkInterfaceGetLocalizedDisplayName(iface)
        self.assertTrue(isinstance(r, str))

        r = SystemConfiguration.SCNetworkInterfaceSetConfiguration(iface, {})
        self.assertTrue(r is True or r is False)

        r = SystemConfiguration.SCNetworkInterfaceSetExtendedConfiguration(
            iface, "OC", {}
        )
        self.assertTrue(r is True or r is False)

        (
            r,
            current,
            active,
            available,
        ) = SystemConfiguration.SCNetworkInterfaceCopyMediaOptions(
            iface, None, None, None, False
        )
        self.assertTrue(r is True)
        self.assertTrue(isinstance(current, SystemConfiguration.CFDictionaryRef))
        self.assertTrue(isinstance(active, SystemConfiguration.CFDictionaryRef))
        self.assertTrue(isinstance(available, SystemConfiguration.CFArrayRef))

        r = SystemConfiguration.SCNetworkInterfaceCopyMediaSubTypes(available)
        self.assertTrue(isinstance(r, SystemConfiguration.CFArrayRef))
        for item in r:
            self.assertTrue(isinstance(item, str))

        r = SystemConfiguration.SCNetworkInterfaceCopyMediaSubTypeOptions(
            available, r[0]
        )
        self.assertTrue(isinstance(r, SystemConfiguration.CFArrayRef))

        r, mtu_cur, mtu_min, mtu_max = SystemConfiguration.SCNetworkInterfaceCopyMTU(
            iface, None, None, None
        )
        self.assertTrue(r is True)
        self.assertTrue(isinstance(mtu_cur, int))
        self.assertTrue(isinstance(mtu_min, int))
        self.assertTrue(isinstance(mtu_max, int))
        r = SystemConfiguration.SCNetworkInterfaceSetMediaOptions(
            iface, current["MediaSubType"], current["MediaOptions"]
        )
        self.assertTrue(r is True or r is False)

        r = SystemConfiguration.SCNetworkInterfaceSetMTU(iface, mtu_cur)
        self.assertTrue(r is True or r is False)

        r = SystemConfiguration.SCNetworkInterfaceForceConfigurationRefresh(iface)
        self.assertTrue(r is True or r is False)

        prefs = SystemConfiguration.SCPreferencesCreate(
            None, "SystemConfiguration", None
        )
        self.assertTrue(isinstance(prefs, SystemConfiguration.SCPreferencesRef))

        a = SystemConfiguration.SCBondInterfaceCopyAll(prefs)
        self.assertTrue(isinstance(a, SystemConfiguration.CFArrayRef))

        a = SystemConfiguration.SCBondInterfaceCopyAvailableMemberInterfaces(prefs)
        self.assertTrue(isinstance(a, SystemConfiguration.CFArrayRef))

        self.assertResultIsCFRetained(SystemConfiguration.SCBondInterfaceCreate)
        iface = SystemConfiguration.SCBondInterfaceCreate(prefs)
        self.assertTrue(
            iface is None or isinstance(iface, SystemConfiguration.SCBondInterfaceRef)
        )

        if iface is not None:
            a = SystemConfiguration.SCBondInterfaceGetMemberInterfaces(iface)
            self.assertTrue(isinstance(a, SystemConfiguration.CFArrayRef))

            o = SystemConfiguration.SCBondInterfaceGetOptions(iface)
            self.assertTrue(
                o is None or isinstance(o, SystemConfiguration.CFDictionaryRef)
            )

            r = SystemConfiguration.SCBondInterfaceSetMemberInterfaces(
                iface, SystemConfiguration.SCNetworkInterfaceCopyAll()
            )
            self.assertTrue(r is True or r is False)

            r = SystemConfiguration.SCBondInterfaceSetLocalizedDisplayName(
                iface, "pyobjc.bond"
            )
            self.assertTrue(r is True or r is False)

            r = SystemConfiguration.SCBondInterfaceSetOptions(iface, {})
            self.assertTrue(r is True or r is False)

            st = SystemConfiguration.SCBondInterfaceCopyStatus(iface)
            self.assertTrue(
                st is None or isinstance(st, SystemConfiguration.SCBondStatusRef)
            )

            a = SystemConfiguration.SCBondStatusGetMemberInterfaces(iface)
            self.assertTrue(a is None or isinstance(a, SystemConfiguration.CFArrayRef))

            st = SystemConfiguration.SCBondStatusGetInterfaceStatus(iface, None)
            self.assertTrue(
                a is None or isinstance(a, SystemConfiguration.CFDictionaryRef)
            )

            r = SystemConfiguration.SCBondInterfaceRemove(iface)
            self.assertTrue(r is True)

        r = SystemConfiguration.SCBondStatusGetTypeID()
        self.assertTrue(isinstance(r, int))

        a = SystemConfiguration.SCVLANInterfaceCopyAll(prefs)
        self.assertTrue(isinstance(a, SystemConfiguration.CFArrayRef))

        a = SystemConfiguration.SCVLANInterfaceCopyAvailablePhysicalInterfaces()
        self.assertTrue(isinstance(a, SystemConfiguration.CFArrayRef))

        if len(a) != 0:
            iface = SystemConfiguration.SCVLANInterfaceCreate(prefs, a[0], 99)
            self.assertTrue(isinstance(iface, SystemConfiguration.SCVLANInterfaceRef))

            r = SystemConfiguration.SCVLANInterfaceGetPhysicalInterface(iface)
            self.assertEqual(r, a[0])

            t = SystemConfiguration.SCVLANInterfaceGetTag(iface)
            self.assertEqual(t, 99)

            t = SystemConfiguration.SCVLANInterfaceGetOptions(iface)
            self.assertTrue(
                t is None or isinstance(t, SystemConfiguration.CFDictionaryRef)
            )

            r = SystemConfiguration.SCVLANInterfaceSetPhysicalInterfaceAndTag(
                iface, a[0], 42
            )
            self.assertIs(r, True)

            r = SystemConfiguration.SCVLANInterfaceSetLocalizedDisplayName(
                iface, "octest"
            )
            self.assertIs(r, True)

            r = SystemConfiguration.SCVLANInterfaceSetOptions(iface, {"name": "foo"})
            self.assertIs(r, True)

            t = SystemConfiguration.SCVLANInterfaceGetOptions(iface)
            self.assertIsInstance(t, (dict, SystemConfiguration.CFDictionaryRef))

            r = SystemConfiguration.SCVLANInterfaceRemove(iface)
            self.assertTrue(r is True)

        self.assertResultIsCFRetained(SystemConfiguration.SCVLANInterfaceCreate)
        SystemConfiguration.SCVLANInterfaceRemove
        SystemConfiguration.SCVLANInterfaceGetPhysicalInterface
        SystemConfiguration.SCVLANInterfaceGetTag
        SystemConfiguration.SCVLANInterfaceGetOptions
        SystemConfiguration.SCVLANInterfaceSetPhysicalInterfaceAndTag
        SystemConfiguration.SCVLANInterfaceSetLocalizedDisplayName
        SystemConfiguration.SCVLANInterfaceSetOptions

        r = SystemConfiguration.SCNetworkProtocolGetTypeID()
        self.assertTrue(isinstance(r, int))

        r = SystemConfiguration.SCNetworkServiceGetTypeID()
        self.assertTrue(isinstance(r, int))

        r = SystemConfiguration.SCNetworkSetGetTypeID()
        self.assertTrue(isinstance(r, int))

        r = SystemConfiguration.SCNetworkServiceCopyAll(prefs)
        self.assertIsInstance(r, SystemConfiguration.CFArrayRef)

        serv = r[0]
        self.assertIsInstance(serv, SystemConfiguration.SCNetworkServiceRef)
        prot = SystemConfiguration.SCNetworkServiceCopyProtocol(
            serv, SystemConfiguration.kSCNetworkProtocolTypeIPv4
        )
        self.assertIsInstance(prot, SystemConfiguration.SCNetworkProtocolRef)

        conf = SystemConfiguration.SCNetworkProtocolGetConfiguration(prot)
        self.assertIsInstance(conf, SystemConfiguration.CFDictionaryRef)

        enabled = SystemConfiguration.SCNetworkProtocolGetEnabled(prot)
        self.assertIsInstance(enabled, bool)

        pr = SystemConfiguration.SCNetworkProtocolGetProtocolType(prot)
        self.assertIsInstance(pr, str)

        v = SystemConfiguration.SCNetworkProtocolSetConfiguration(prot, conf)
        self.assertIsInstance(v, bool)

        v = SystemConfiguration.SCNetworkProtocolSetEnabled(prot, enabled)
        self.assertIsInstance(v, bool)

        v = SystemConfiguration.SCNetworkServiceAddProtocolType(serv, pr)
        self.assertIsInstance(v, bool)

        v = SystemConfiguration.SCNetworkServiceCopyProtocols(serv)
        self.assertIsInstance(v, SystemConfiguration.CFArrayRef)
        if v:
            self.assertIsInstance(v[0], SystemConfiguration.SCNetworkProtocolRef)

        iface = SystemConfiguration.SCNetworkServiceGetInterface(serv)
        self.assertIsInstance(iface, SystemConfiguration.SCNetworkInterfaceRef)

        v = SystemConfiguration.SCNetworkServiceCreate(prefs, iface)
        self.assertIsInstance(v, SystemConfiguration.SCNetworkServiceRef)

        v = s2 = SystemConfiguration.SCNetworkServiceCopy(
            prefs, SystemConfiguration.SCNetworkServiceGetServiceID(serv)
        )
        self.assertIsInstance(v, SystemConfiguration.SCNetworkServiceRef)

        v = SystemConfiguration.SCNetworkServiceGetEnabled(serv)
        self.assertIsInstance(v, bool)

        v = SystemConfiguration.SCNetworkServiceGetName(serv)
        self.assertIsInstance(v, str)

        self.assertResultIsCFRetained(SystemConfiguration.SCNetworkServiceCopyProtocol)

        v = SystemConfiguration.SCNetworkServiceRemoveProtocolType(
            s2, SystemConfiguration.kSCNetworkProtocolTypeIPv4
        )
        self.assertIsInstance(v, bool)

        v = SystemConfiguration.SCNetworkServiceRemove(s2)
        self.assertIsInstance(v, bool)

        v = SystemConfiguration.SCNetworkServiceSetEnabled(
            serv, SystemConfiguration.SCNetworkServiceGetEnabled(serv)
        )
        self.assertIsInstance(v, bool)

        v = SystemConfiguration.SCNetworkServiceSetName(
            serv, SystemConfiguration.SCNetworkServiceGetName(serv)
        )
        self.assertIsInstance(v, bool)

        a_set = SystemConfiguration.SCNetworkSetCopyCurrent(prefs)
        self.assertIsInstance(a_set, SystemConfiguration.SCNetworkSetRef)

        s2 = SystemConfiguration.SCNetworkServiceCopy(
            prefs, SystemConfiguration.SCNetworkServiceGetServiceID(serv)
        )

        v = SystemConfiguration.SCNetworkSetAddService(set, s2)
        self.assertIsInstance(v, bool)

        v = SystemConfiguration.SCNetworkSetContainsInterface(set, iface)
        self.assertIsInstance(v, bool)

        v = SystemConfiguration.SCNetworkSetCopyAll(prefs)
        self.assertIsInstance(v, SystemConfiguration.CFArrayRef)

        v = SystemConfiguration.SCNetworkSetCopyServices(a_set)
        self.assertIsInstance(v, SystemConfiguration.CFArrayRef)

        v = SystemConfiguration.SCNetworkSetCreate(prefs)
        self.assertIsInstance(v, SystemConfiguration.SCNetworkSetRef)

        v = SystemConfiguration.SCNetworkSetCopy(
            prefs, SystemConfiguration.SCNetworkSetGetSetID(a_set)
        )
        self.assertIsInstance(v, SystemConfiguration.SCNetworkSetRef)

        v = SystemConfiguration.SCNetworkSetRemove(v)
        self.assertIsInstance(v, bool)

        v = SystemConfiguration.SCNetworkSetGetName(a_set)
        self.assertIsInstance(v, str)

        v = SystemConfiguration.SCNetworkSetGetSetID(a_set)
        self.assertIsInstance(v, str)

        v = SystemConfiguration.SCNetworkSetGetServiceOrder(a_set)
        self.assertIsInstance(v, (SystemConfiguration.CFArrayRef, type(None)))

        v = SystemConfiguration.SCNetworkSetSetName(
            a_set, SystemConfiguration.SCNetworkSetGetName(a_set)
        )
        self.assertIsInstance(v, bool)

        v = SystemConfiguration.SCNetworkSetSetServiceOrder(
            a_set, SystemConfiguration.SCNetworkSetGetServiceOrder(a_set)
        )
        self.assertIsInstance(v, bool)

        v = SystemConfiguration.SCNetworkSetSetCurrent(
            SystemConfiguration.SCNetworkSetCopyCurrent(prefs)
        )
        self.assertIsInstance(v, bool)

        self.assertResultIsBOOL(SystemConfiguration.SCNetworkSetRemoveService)

    @min_os_level("10.5")
    def testFunctions10_5(self):
        prefs = SystemConfiguration.SCPreferencesCreate(
            None, "SystemConfiguration", None
        )
        self.assertTrue(isinstance(prefs, SystemConfiguration.SCPreferencesRef))

        r = SystemConfiguration.SCNetworkServiceCopyAll(prefs)
        self.assertIsInstance(r, SystemConfiguration.CFArrayRef)
        serv = SystemConfiguration.SCNetworkServiceCopy(
            prefs, SystemConfiguration.SCNetworkServiceGetServiceID(r[0])
        )

        v = SystemConfiguration.SCNetworkServiceEstablishDefaultConfiguration(serv)
        self.assertIsInstance(v, bool)
