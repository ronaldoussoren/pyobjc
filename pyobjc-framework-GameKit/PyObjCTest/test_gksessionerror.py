import GameKit
from PyObjCTools.TestSupport import TestCase


class TestGKSessionError(TestCase):
    def testConstants(self):
        self.assertIsInstance(GameKit.GKSessionErrorDomain, str)
