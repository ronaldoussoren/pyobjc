from PyObjCTools.TestSupport import *
import sys

SLRequestHandler = b'v@@@'

if sys.maxsize > 2**32:
    import Social

    class TestSLRequest (TestCase):
        @min_os_level("10.8")
        def testConstants(self):
            self.assertEqual(Social.SLRequestMethodGET, 0)
            self.assertEqual(Social.SLRequestMethodPOST, 1)
            self.assertEqual(Social.SLRequestMethodDELETE, 2)

        @min_os_level("10.8")
        def testMethods(self):
            self.assertArgIsBlock(Social.SLRequest.performRequestWithHandler_, 0, SLRequestHandler)

if __name__ == "__main__":
    main()
