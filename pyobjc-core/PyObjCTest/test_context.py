from PyObjCTools.TestSupport import *

import objc

try:
    long
except NameError:
    long = int

class TestContext (TestCase):
    def test_context(self):
        self.assertEqual(objc.context._registry, {})

        v = object()

        h = objc.context.register(v)
        self.assertIsInstance(h, (int, long))
        self.assertIn(h, objc.context._registry)
        self.assertIs(objc.context._registry[h], v)

        self.assertIs(objc.context.get(h), v)

        objc.context.unregister(object())
        self.assertIn(h, objc.context._registry)
        self.assertIs(objc.context._registry[h], v)

        objc.context.unregister(v)
        self.assertNotIn(h, objc.context._registry)

        self.assertRaises(KeyError, objc.context.get, h)


if __name__ == "__main__":
    main()
