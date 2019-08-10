"""
Some simple tests to check that the framework is properly wrapped.
"""
import objc
import warnings
from PyObjCTools.TestSupport import *

with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    import DictionaryServices


class TestDictionaryServices(TestCase):
    def testClasses(self):
        self.assertIsCFType(DictionaryServices.DCSDictionaryRef)

    @onlyIf(os_release().rsplit(".", 1)[0] not in ("10.12", "10.13"))
    def testFunctions(self):
        txt = b"the hello world program".decode("latin1")
        r = DictionaryServices.DCSGetTermRangeInString(None, txt, 5)
        self.assertIsInstance(r, DictionaryServices.CFRange)
        self.assertEqual(r, (4, 5))

        r = DictionaryServices.DCSCopyTextDefinition(None, txt, r)
        self.assertIsInstance(r, (unicode, type(None)))

        v = DictionaryServices.DCSDictionaryGetTypeID()
        self.assertIsInstance(v, (int, long))


if __name__ == "__main__":
    main()
