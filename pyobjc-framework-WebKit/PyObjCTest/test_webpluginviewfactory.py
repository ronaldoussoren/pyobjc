
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebPluginViewFactory (TestCase):
    def testConstants(self):
        self.assertIsInstance(WebPlugInBaseURLKey, unicode)
        self.assertIsInstance(WebPlugInAttributesKey, unicode)
        self.assertIsInstance(WebPlugInContainerKey, unicode)
        self.assertIsInstance(WebPlugInContainingElementKey, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(WebPlugInShouldLoadMainResourceKey, unicode)

    @min_sdk_level('10.6')
    def testProtocols(self):
        objc.protocolNamed('WebPlugInViewFactory')

if __name__ == "__main__":
    main()
