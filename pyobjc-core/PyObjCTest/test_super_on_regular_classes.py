from PyObjCTools.TestSupport import TestCase

from objc import super  # noqa: A004


class TestUsingObjCSuperWithPlainClasses(TestCase):
    def test_basic(self):
        class MyBaseClass:
            def meth(self):
                return 42

        class MySubClass(MyBaseClass):
            def meth(self):
                return super().meth() + 4

        o = MyBaseClass()
        self.assertEqual(o.meth(), 42)

        o = MySubClass()
        self.assertEqual(o.meth(), 46)
