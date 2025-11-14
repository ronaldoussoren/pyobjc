from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc

import GameController


class TestGCPhysicalInputExtentsHelper(GameController.NSObject):
    def scaledValue(self):
        return 1

    def minimumValue(self):
        return 1

    def maximumValue(self):
        return 1


class TestGCPhysicalInputExtents(TestCase):
    @min_sdk_level("26.2")
    def test_protocols(self):
        self.assertProtocolExists("GCPhysicalInputExtents")

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestGCPhysicalInputExtentsHelper.scaledValue, objc._C_DBL
        )
        self.assertResultHasType(
            TestGCPhysicalInputExtentsHelper.minimumValue, objc._C_DBL
        )
        self.assertResultHasType(
            TestGCPhysicalInputExtentsHelper.maximumValue, objc._C_DBL
        )
