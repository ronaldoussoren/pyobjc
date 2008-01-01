'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import SystemConfiguration

class TestSystemConfiguration (unittest.TestCase):
    def testClasses(self):
        # Not-tollfree CF-type:
        self.assert_( hasattr(SystemConfiguration, 'SCDynamicStoreRef') )
        self.assert_( issubclass(SystemConfiguration.SCDynamicStoreRef, objc.lookUpClass('NSCFType')) )
        self.assert_( SystemConfiguration.SCDynamicStoreRef is not objc.lookUpClass('NSCFType') )

    def testValues(self):
        self.assert_( hasattr(SystemConfiguration, 'kSCNetworkFlagsConnectionAutomatic') )
        self.assert_( isinstance(SystemConfiguration.kSCNetworkFlagsConnectionAutomatic, (int, long)) )
        self.assertEquals(SystemConfiguration.kSCNetworkFlagsConnectionAutomatic, 1 << 3)

        self.assert_( hasattr(SystemConfiguration, 'kSCNetworkInterfaceIPv4') )
        self.assert_( isinstance(SystemConfiguration.kSCNetworkInterfaceIPv4, SystemConfiguration.SCNetworkInterfaceRef) )

        self.assert_( hasattr(SystemConfiguration, 'kSCNetworkConnectionBytesIn') )
        self.assert_( isinstance(SystemConfiguration.kSCNetworkConnectionBytesIn, (str, unicode)) )
        self.assert_( hasattr(SystemConfiguration, 'kSCPropUsersConsoleUserGID') )
        self.assert_( isinstance(SystemConfiguration.kSCPropUsersConsoleUserGID, (str, unicode)) )

    def testVariables(self):
        self.assert_( hasattr(SystemConfiguration, 'kSCDynamicStoreUseSessionKeys') )
        self.assert_( isinstance(SystemConfiguration.kSCDynamicStoreUseSessionKeys, unicode) )
        self.assert_( hasattr(SystemConfiguration, 'kSCNetworkInterfaceType6to4') )
        self.assert_( isinstance(SystemConfiguration.kSCNetworkInterfaceType6to4, unicode) )
        self.assert_( hasattr(SystemConfiguration, 'kSCResvLink') )
        self.assert_( isinstance(SystemConfiguration.kSCResvLink, unicode) )

    def testFunctions(self):
        self.assert_( hasattr(SystemConfiguration, 'SCDynamicStoreCopyKeyList') )
        self.assert_( hasattr(SystemConfiguration, 'SCDynamicStoreAddValue') )



if __name__ == "__main__":
    unittest.main()

