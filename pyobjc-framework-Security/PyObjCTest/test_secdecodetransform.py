import Security
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestSecDecodeTransform(TestCase):
    @min_os_level("10.7")
    def test_constants(self):
        self.assertIsInstance(Security.kSecDecodeTypeAttribute, str)

    @min_os_level("10.7")
    def test_functions10_7(self):
        self.assertResultHasType(Security.SecDecodeTransformCreate, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecDecodeTransformCreate)
        self.assertArgHasType(Security.SecDecodeTransformCreate, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecDecodeTransformCreate, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
