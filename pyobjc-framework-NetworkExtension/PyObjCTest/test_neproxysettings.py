from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNEProxySettings (TestCase):
        @min_os_level('10.11')
        def testMethods(self):
            self.assertResultIsBOOL(NetworkExtension.NEProxyServer.authenticationRequired)
            self.assertArgIsBOOL(NetworkExtension.NEProxyServer.setAuthenticationRequired_, 0)

            self.assertResultIsBOOL(NetworkExtension.NEProxySettings.autoProxyConfigurationEnabled)
            self.assertArgIsBOOL(NetworkExtension.NEProxySettings.setAutoProxyConfigurationEnabled_, 0)

            self.assertResultIsBOOL(NetworkExtension.NEProxySettings.HTTPEnabled)
            self.assertArgIsBOOL(NetworkExtension.NEProxySettings.setHTTPEnabled_, 0)

            self.assertResultIsBOOL(NetworkExtension.NEProxySettings.HTTPSEnabled)
            self.assertArgIsBOOL(NetworkExtension.NEProxySettings.setHTTPSEnabled_, 0)

            self.assertResultIsBOOL(NetworkExtension.NEProxySettings.excludeSimpleHostnames)
            self.assertArgIsBOOL(NetworkExtension.NEProxySettings.setExcludeSimpleHostnames_, 0)


if __name__ == "__main__":
    main()
