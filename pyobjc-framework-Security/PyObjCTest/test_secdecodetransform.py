import Security
from PyObjCTools.TestSupport import TestCase
import objc


class TestSecDecodeTransform(TestCase):
    def test_constants(self):
        self.assertIsInstance(Security.kSecDecodeTypeAttribute, str)

    def test_functions(self):
        self.assertResultHasType(Security.SecDecodeTransformCreate, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecDecodeTransformCreate)
        self.assertArgHasType(Security.SecDecodeTransformCreate, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecDecodeTransformCreate, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
