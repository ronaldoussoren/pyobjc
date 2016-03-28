from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNWPath (TestCase):
        @min_os_level('10.11')
        def testConstants(self):
            self.assertEqual(NetworkExtension.NWPathStatusInvalid, 0)
            self.assertEqual(NetworkExtension.NWPathStatusSatisfied, 1)
            self.assertEqual(NetworkExtension.NWPathStatusUnsatisfied, 2)
            self.assertEqual(NetworkExtension.NWPathStatusSatisfiable, 3)

        @min_os_level('10.11')
        def testMethods(self):
            self.assertResultIsBOOL(NetworkExtension.NWPath.isExpensive)
            self.assertResultIsBOOL(NetworkExtension.NWPath.isEqualToPath_)


if __name__ == "__main__":
    main()
