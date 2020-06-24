from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class NEFilterProviderConfiguration(TestCase):
    @min_os_level("10.11")
    def testMethods(self):
        self.assertResultIsBOOL(
            NetworkExtension.NEFilterProviderConfiguration.filterBrowsers
        )
        self.assertArgIsBOOL(
            NetworkExtension.NEFilterProviderConfiguration.setFilterBrowsers_, 0
        )

        self.assertResultIsBOOL(
            NetworkExtension.NEFilterProviderConfiguration.filterSockets
        )
        self.assertArgIsBOOL(
            NetworkExtension.NEFilterProviderConfiguration.setFilterSockets_, 0
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(
            NetworkExtension.NEFilterProviderConfiguration.filterPackets
        )
        self.assertArgIsBOOL(
            NetworkExtension.NEFilterProviderConfiguration.setFilterPackets_, 0
        )
