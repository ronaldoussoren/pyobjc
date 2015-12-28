from PyObjCTools.TestSupport import *

import CoreWLAN

class TestCoreWLAN (TestCase):
    @min_os_level('10.7')
    def testConstants(self):
        self.assertEqual(CoreWLAN.CoreWLANFrameworkVersionNumber2_0, 200)
        self.assertIsInstance(CoreWLAN.CoreWLANFrameworkVersionNumber, float)

if __name__ == "__main__":
    main()
