from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNEAppProxyFlow (TestCase):
        @min_os_level('10.11')
        def testConstants(self):
            self.assertEqual(NetworkExtension.NEFilterManagerErrorConfigurationInvalid, 1)
            self.assertEqual(NetworkExtension.NEFilterManagerErrorConfigurationDisabled, 2)
            self.assertEqual(NetworkExtension.NEFilterManagerErrorConfigurationStale, 3)
            self.assertEqual(NetworkExtension.NEFilterManagerErrorConfigurationCannotBeRemoved, 4)

            self.assertIsInstance(NetworkExtension.NEFilterErrorDomain, unicode)
            self.assertIsInstance(NetworkExtension.NEFilterConfigurationDidChangeNotification, unicode)

        @min_os_level('10.11')
        def testMethods(self):
            self.assertArgIsBlock(NetworkExtension.NEFilterManager.loadFromPreferencesWithCompletionHandler_, 0, b'v@')
            self.assertArgIsBlock(NetworkExtension.NEFilterManager.removeFromPreferencesWithCompletionHandler_, 0, b'v@')
            self.assertArgIsBlock(NetworkExtension.NEFilterManager.saveToPreferencesWithCompletionHandler_, 0, b'v@')
            self.assertResultIsBOOL(NetworkExtension.NEFilterManager.isEnabled)
            self.assertArgIsBOOL(NetworkExtension.NEFilterManager.setEnabled_, 0)


if __name__ == "__main__":
    main()
