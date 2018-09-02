'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *

import CoreServices

class TestDictionaryServices (TestCase):
    def testClasses(self):
        self.assertIsCFType(CoreServices.DCSDictionaryRef)

    @onlyIf(os_release().rsplit('.', 1)[0] not in ('10.12', '10.13'))
    def testFunctions(self):
        txt = b"the hello world program".decode('latin1')
        r = CoreServices.DCSGetTermRangeInString(None, txt, 5)
        self.assertIsInstance(r, CoreServices.CFRange)
        self.assertEqual(r, (4, 5))

        r = CoreServices.DCSCopyTextDefinition(None, txt, r)
        self.assertIsInstance(r, (unicode, type(None)))

        v = CoreServices.DCSDictionaryGetTypeID()
        self.assertIsInstance(v, (int, long))


if __name__ == "__main__":
    main()
