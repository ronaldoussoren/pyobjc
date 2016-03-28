from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNEDNSSettings (TestCase):
        @min_os_level('10.11')
        def testMethods(self):
            self.assertResultIsBOOL(NetworkExtension.NEDNSSettings.matchDomainsNoSearch, b'Z')
            self.assertArgIsBOOL(NetworkExtension.NEDNSSettings.setMatchDomainsNoSearch_, 0, b'Z')


if __name__ == "__main__":
    main()
