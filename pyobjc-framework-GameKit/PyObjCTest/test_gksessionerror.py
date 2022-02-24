import GameKit
from PyObjCTools.TestSupport import TestCase


class TestGKSessionError(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameKit.GKSessionError)

    def testConstants(self):
        self.assertIsInstance(GameKit.GKSessionErrorDomain, str)
