import Security
from PyObjCTools.TestSupport import TestCase
import objc


class TestSecTransformReadTransform(TestCase):
    def test_functions(self):
        self.assertResultHasType(
            Security.SecTransformCreateReadTransformWithReadStream, objc._C_ID
        )
        self.assertResultIsCFRetained(
            Security.SecTransformCreateReadTransformWithReadStream
        )
        self.assertArgHasType(
            Security.SecTransformCreateReadTransformWithReadStream, 0, objc._C_ID
        )
