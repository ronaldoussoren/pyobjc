import DiskArbitration
from PyObjCTools.TestSupport import TestCase, cast_int
import objc


class TestDADissenter(TestCase):
    def test_constants(self):

        self.assertEqual(DiskArbitration.kDAReturnSuccess, 0)
        self.assertEqual(DiskArbitration.kDAReturnError, cast_int(0xF8DA0001))
        self.assertEqual(DiskArbitration.kDAReturnBusy, cast_int(0xF8DA0002))
        self.assertEqual(DiskArbitration.kDAReturnBadArgument, cast_int(0xF8DA0003))
        self.assertEqual(DiskArbitration.kDAReturnExclusiveAccess, cast_int(0xF8DA0004))
        self.assertEqual(DiskArbitration.kDAReturnNoResources, cast_int(0xF8DA0005))
        self.assertEqual(DiskArbitration.kDAReturnNotFound, cast_int(0xF8DA0006))
        self.assertEqual(DiskArbitration.kDAReturnNotMounted, cast_int(0xF8DA0007))
        self.assertEqual(DiskArbitration.kDAReturnNotPermitted, cast_int(0xF8DA0008))
        self.assertEqual(DiskArbitration.kDAReturnNotPrivileged, cast_int(0xF8DA0009))
        self.assertEqual(DiskArbitration.kDAReturnNotReady, cast_int(0xF8DA000A))
        self.assertEqual(DiskArbitration.kDAReturnNotWritable, cast_int(0xF8DA000B))
        self.assertEqual(DiskArbitration.kDAReturnUnsupported, cast_int(0xF8DA000C))

    def test_types(self):
        # XXX: DADissenterRef isn't a separate CF Type
        # self.assertIsCFType(DiskArbitration.DADissenterRef)
        pass

    def test_functions(self):
        self.assertResultIsCFRetained(DiskArbitration.DADissenterCreate)

        obj = DiskArbitration.DADissenterCreate(None, 42, "hello world")
        self.assertIsInstance(obj, objc.objc_object)

        self.assertEqual(DiskArbitration.DADissenterGetStatus(obj), 42)
        self.assertEqual(DiskArbitration.DADissenterGetStatusString(obj), "hello world")
