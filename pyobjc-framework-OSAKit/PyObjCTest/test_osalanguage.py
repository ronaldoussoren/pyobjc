from PyObjCTools.TestSupport import *

import OSAKit

class TestOSALanguage (TestCase):
    def testConstants(self):
        self.assertEqual(OSAKit.OSASupportsCompiling, 0x0002)
        self.assertEqual(OSAKit.OSASupportsGetSource, 0x0004)
        self.assertEqual(OSAKit.OSASupportsAECoercion, 0x0008)
        self.assertEqual(OSAKit.OSASupportsAESending, 0x0010)
        self.assertEqual(OSAKit.OSASupportsRecording, 0x0020)
        self.assertEqual(OSAKit.OSASupportsConvenience, 0x0040)
        self.assertEqual(OSAKit.OSASupportsDialects, 0x0080)
        self.assertEqual(OSAKit.OSASupportsEventHandling, 0x0100)

    def testClasses(self):
        OSAKit.OSALanguage

    @min_os_level('10.6')
    def testMethods(self):
        self.assertResultIsBOOL(OSAKit.OSALanguage.isThreadSafe)

if __name__ == "__main__":
    main()
