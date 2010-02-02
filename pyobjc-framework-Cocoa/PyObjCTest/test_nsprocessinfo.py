from __future__ import with_statement
from PyObjCTools.TestSupport import *

from Foundation import *



class TestNSProcessInfo (TestCase):
    def testConstants(self):
        self.assertEqual(NSWindowsNTOperatingSystem, 1)
        self.assertEqual(NSWindows95OperatingSystem, 2)
        self.assertEqual(NSSolarisOperatingSystem, 3)
        self.assertEqual(NSHPUXOperatingSystem, 4)
        self.assertEqual(NSMACHOperatingSystem, 5)
        self.assertEqual(NSSunOSOperatingSystem, 6)
        self.assertEqual(NSOSF1OperatingSystem, 7)

    def testNSDisabledSuddenTermination(self):
        # annoyingly we cannot easily test if this has an effect, but
        # this at least guards against typos.
        with NSDisabledSuddenTermination:
            pass

        class TestException (Exception):
            pass
        try:
            with NSDisabledSuddenTermination:
                raise TestException(1)

        except TestException:
            pass



if __name__ == "__main__":
    main()
