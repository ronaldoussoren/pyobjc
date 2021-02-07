import warnings

from PyObjCTools.TestSupport import TestCase, os_release, onlyIf

with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    import DictionaryServices


class TestDictionaryServices(TestCase):
    def testClasses(self):
        self.assertIsCFType(DictionaryServices.DCSDictionaryRef)

    @onlyIf(os_release().rsplit(".", 1)[0] not in ("10.12", "10.13"))
    def testFunctions(self):
        txt = "the hello world program"
        r = DictionaryServices.DCSGetTermRangeInString(None, txt, 5)
        self.assertIsInstance(r, DictionaryServices.CFRange)
        self.assertEqual(r, (4, 5))

        r = DictionaryServices.DCSCopyTextDefinition(None, txt, r)
        self.assertIsInstance(r, (str, type(None)))

        v = DictionaryServices.DCSDictionaryGetTypeID()
        self.assertIsInstance(v, int)
