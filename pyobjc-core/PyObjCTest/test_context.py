import objc
from PyObjCTools.TestSupport import TestCase


class TestContext(TestCase):
    def test_context(self):
        self.assertEqual(objc.context._registry, {})

        v = object()

        h = objc.context.register(v)
        self.assertIsInstance(h, int)
        self.assertIn(h, objc.context._registry)
        self.assertIs(objc.context._registry[h], v)

        self.assertIs(objc.context.get(h), v)

        objc.context.unregister(object())
        self.assertIn(h, objc.context._registry)
        self.assertIs(objc.context._registry[h], v)

        objc.context.unregister(v)
        self.assertNotIn(h, objc.context._registry)

        with self.assertRaisesRegex(KeyError, str(h)):
            objc.context.get(h)
