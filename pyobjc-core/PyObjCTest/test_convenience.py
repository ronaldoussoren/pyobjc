from PyObjCTools.TestSupport import *
import objc
import objc._convenience as convenience

class TestConvenienceHelpers (TestCase):
    def test_add_for_selector(self):
        methods = [
            ('add', lambda self, x: self.testMethod_(x))
        ]

        with filterWarnings("error", DeprecationWarning):
            self.assertRaises(DeprecationWarning, objc.addConvenienceForSelector, b'testMethod:', methods)
            if b'testMethod' in convenience._CONVENIENCE_METHODS:
                del convenience._CONVENIENCE_METHODS[b'testMethods:']

        with filterWarnings("ignore", DeprecationWarning):
            self.assertNotIn(b'testMethod:', convenience._CONVENIENCE_METHODS)
            try:
                objc.addConvenienceForSelector(b'testMethod:', methods)

                self.assertEqual(convenience._CONVENIENCE_METHODS[b'testMethod:'], methods)

            finally:
                if b'testMethod' in convenience._CONVENIENCE_METHODS:
                    del convenience._CONVENIENCE_METHODS[b'testMethods:']


    def test_add_for_class(self):
        self.assertNotIn("MyObject", convenience.CLASS_METHODS)

        methods = [
            ('info', lambda self: self.description())
        ]

        try:
            objc.addConvenienceForClass("MyObject", methods)
            self.assertEqual(convenience.CLASS_METHODS["MyObject"], methods)

        finally:
            if 'MyObject' in convenience.CLASS_METHODS:
                del convenience.CLASS_METHODS["MyObject"]


# TODO: Explicit tests for add_convenience_methods.

if __name__ == "__main__":
    main()
