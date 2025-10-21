import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestlMTL4CompilerTaskHelper(Metal.NSObject):
    def status(self):
        return 1


class TestlMTL4CompilerTask(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Metal.MTL4CompilerTaskStatus)
        self.assertEqual(Metal.MTL4CompilerTaskStatusNone, 0)
        self.assertEqual(Metal.MTL4CompilerTaskStatusScheduled, 1)
        self.assertEqual(Metal.MTL4CompilerTaskStatusCompiling, 2)
        self.assertEqual(Metal.MTL4CompilerTaskStatusFinished, 3)

    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTL4CompilerTask")

    def test_protocol_methods(self):
        self.assertResultHasType(TestlMTL4CompilerTaskHelper.status, b"q")
