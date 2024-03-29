import CoreServices
from PyObjCTools.TestSupport import TestCase, os_release, skipUnless


class TestDictionaryServices(TestCase):
    def testClasses(self):
        self.assertIsCFType(CoreServices.DCSDictionaryRef)

    @skipUnless(
        os_release().rsplit(".", 1)[0] not in ("10.12", "10.13"), "buggy os release"
    )
    def testFunctions(self):
        txt = "the hello world program"
        r = CoreServices.DCSGetTermRangeInString(None, txt, 5)
        self.assertIsInstance(r, CoreServices.CFRange)
        self.assertEqual(r, (4, 5))

        r = CoreServices.DCSCopyTextDefinition(None, txt, r)
        self.assertIsInstance(r, (str, type(None)))

        v = CoreServices.DCSDictionaryGetTypeID()
        self.assertIsInstance(v, int)
