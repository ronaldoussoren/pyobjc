import Security
from PyObjCTools.TestSupport import TestCase


class TestSecDecodeTransform(TestCase):
    def test_constants(self):
        self.assertIsInstance(Security.kSecDecodeTypeAttribute, str)

    def test_functions(self):
        self.assertResultIsCFRetained(Security.SecDecodeTransformCreate)
        self.assertArgIsOut(Security.SecDecodeTransformCreate, 1)
