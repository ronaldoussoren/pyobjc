import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CoreML

    class TestMLDictionaryFeatureProvider (TestCase):
        @min_sdk_level("10.13")
        def testProtocols(self):
            objc.protocolNamed('MLFeatureProvider')

if __name__ == "__main__":
    main()
