from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNEAppProxyFlow (TestCase):
        @min_os_level('10.11')
        def testConstants(self):
            self.assertEqual(NetworkExtension.NEFilterFlowBytesMax, (1<<64) - 1)


if __name__ == "__main__":
    main()
