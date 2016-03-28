from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class NEFilterProviderConfiguration (TestCase):

        @min_os_level('10.11')
        def testMethods(self):
            self.assertResultIsBOOL(NetworkExtension.NEFilterProviderConfiguration.filterBrowsers)
            self.assertArgIsBOOL(NetworkExtension.NEFilterProviderConfiguration.setFilterBrowsers_, 0)

            self.assertResultIsBOOL(NetworkExtension.NEFilterProviderConfiguration.filterSockets)
            self.assertArgIsBOOL(NetworkExtension.NEFilterProviderConfiguration.setFilterSockets_, 0)


if __name__ == "__main__":
    main()
