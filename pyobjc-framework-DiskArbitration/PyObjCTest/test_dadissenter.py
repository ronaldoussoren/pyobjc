from PyObjCTools.TestSupport import *

import DiskArbitration

class TestDADissenter (TestCase):
    def test_constants(self):

        self.assertEqual(DiskArbitration.kDAReturnSuccess, 0)
        self.assertEqual(DiskArbitration.kDAReturnError, 0xF8DA0001)
        self.assertEqual(DiskArbitration.kDAReturnBusy, 0xF8DA0002)
        self.assertEqual(DiskArbitration.kDAReturnBadArgument, 0xF8DA0003)
        self.assertEqual(DiskArbitration.kDAReturnExclusiveAccess, 0xF8DA0004)
        self.assertEqual(DiskArbitration.kDAReturnNoResources, 0xF8DA0005)
        self.assertEqual(DiskArbitration.kDAReturnNotFound, 0xF8DA0006)
        self.assertEqual(DiskArbitration.kDAReturnNotMounted, 0xF8DA0007)
        self.assertEqual(DiskArbitration.kDAReturnNotPermitted, 0xF8DA0008)
        self.assertEqual(DiskArbitration.kDAReturnNotPrivileged, 0xF8DA0009)
        self.assertEqual(DiskArbitration.kDAReturnNotReady, 0xF8DA000A)
        self.assertEqual(DiskArbitration.kDAReturnNotWritable, 0xF8DA000B)
        self.assertEqual(DiskArbitration.kDAReturnUnsupported, 0xF8DA000C)

    def test_types(self):
        self.assertIsCFType(DiskArbitration.DADissenterRef)

    def test_functions(self):
        self.assertResultIsCFRetained(DiskArbitration.DADissenterCreate)

        obj = DiskArbitration.DADissenterCreate(None, 42, "hello world")
        self.assertIsInstance(obj, DiskArbitration.DADissenterRef)

        self.assertIsEqual(DiskArbitration.DADissenterGetStatus(obj), 42)
        self.assertIsEqual(DiskArbitration.DADissenterGetStatusString(obj), "hello world")

if __name__ == "__main__":
    main()
