from objc import selector
from PyObjCTools.TestSupport import TestCase


class TestDefaultSelectors(TestCase):
    def test_python_only(self):
        def method(self, a, b):
            pass

        s = selector(method)
        self.assertEqual(s.selector, b"method")
        self.assertEqual(s.signature, b"v@:")

        def method_pep8(self, a, b):
            pass

        s = selector(method_pep8)
        self.assertEqual(s.selector, b"method_pep8")
        self.assertEqual(s.signature, b"v@:")

    def test_objective_c(self):
        def foo_(self, a):
            pass

        s = selector(foo_)
        self.assertEqual(s.selector, b"foo:")
        self.assertEqual(s.signature, b"v@:@")

        def foo_bar_(self, a):
            pass

        s = selector(foo_bar_)
        self.assertEqual(s.selector, b"foo:bar:")
        self.assertEqual(s.signature, b"v@:@@")

        def foo_bar_(self, a):
            return 1

        s = selector(foo_bar_)
        self.assertEqual(s.selector, b"foo:bar:")
        self.assertEqual(s.signature, b"@@:@@")
