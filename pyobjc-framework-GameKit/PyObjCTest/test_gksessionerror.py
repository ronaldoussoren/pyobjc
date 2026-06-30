import GameKit
from PyObjCTools.TestSupport import TestCase


class TestGKSessionError(TestCase):
    def test_constants(self):
        self.assertIsInstance(GameKit.GKSessionErrorDomain, str)
