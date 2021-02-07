import DiskArbitration
from PyObjCTools.TestSupport import TestCase, cast_int
import objc


class TestDADissenter(TestCase):
    def test_constants(self):

        self.assertEqual(DiskArbitration.kDAReturnSuccess, 0)
        self.assertEqual(DiskArbitration.kDAReturnError, cast_int(0xf8da0001))
        self.assertEqual(DiskArbitration.kDAReturnBusy, cast_int(0xf8da0002))
        self.assertEqual(DiskArbitration.kDAReturnBadArgument, cast_int(0xf8da0003))
        self.assertEqual(DiskArbitration.kDAReturnExclusiveAccess, cast_int(0xf8da0004))
        self.assertEqual(DiskArbitration.kDAReturnNoResources, cast_int(0xf8da0005))
        self.assertEqual(DiskArbitration.kDAReturnNotFound, cast_int(0xf8da0006))
        self.assertEqual(DiskArbitration.kDAReturnNotMounted, cast_int(0xf8da0007))
        self.assertEqual(DiskArbitration.kDAReturnNotPermitted, cast_int(0xf8da0008))
        self.assertEqual(DiskArbitration.kDAReturnNotPrivileged, cast_int(0xf8da0009))
        self.assertEqual(DiskArbitration.kDAReturnNotReady, cast_int(0xf8da000a))
        self.assertEqual(DiskArbitration.kDAReturnNotWritable, cast_int(0xf8da000b))
        self.assertEqual(DiskArbitration.kDAReturnUnsupported, cast_int(0xf8da000c))

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
