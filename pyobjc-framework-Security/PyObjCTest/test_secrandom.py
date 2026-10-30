import Security
from PyObjCTools.TestSupport import TestCase
import objc


class TestSecRandom(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(Security.SecRandomRef)

    def test_constants(self):
        self.assertIsInstance(
            Security.kSecRandomDefault, (type(None), Security.SecRandomRef)
        )

    def test_functions(self):
        self.assertResultHasType(Security.SecRandomCopyBytes, objc._C_INT)
        self.assertArgHasType(
            Security.SecRandomCopyBytes, 0, Security.SecRandomRef.__typestr__
        )
        self.assertArgHasType(Security.SecRandomCopyBytes, 1, objc._C_ULNG)
        self.assertArgHasType(
            Security.SecRandomCopyBytes, 2, objc._C_OUT + objc._C_PTR + objc._C_VOID
        )
        self.assertArgSizeInArg(Security.SecRandomCopyBytes, 2, 1)
