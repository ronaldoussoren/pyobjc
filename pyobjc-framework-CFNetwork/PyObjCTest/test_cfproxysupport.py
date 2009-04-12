from PyObjCTools.TestSupport import *
from CFNetwork import *

SCRIPT="""
function FindProxyForURL(url, host) {
   if (shExpMatch(host, "*.apple.com")) {
      return "PROXY proxy.apple.com:8080";
   }
   return "DIRECT";
}
"""

class TestCFProxySupport (TestCase):

    @min_os_level('10.5')
    def testFunctions(self):
        self.failUnlessResultIsCFRetained(CFNetworkCopyProxiesForURL)
        url = CFURLCreateWithString(None, "http://www.apple.com/", None)
        v = CFNetworkCopyProxiesForURL(url, None)
        self.failUnlessIsInstance(v, CFArrayRef)

        self.failUnlessResultIsCFRetained(CFNetworkCopyProxiesForAutoConfigurationScript)
        self.failUnlessArgIsOut(CFNetworkCopyProxiesForAutoConfigurationScript, 2)
        v, err  = CFNetworkCopyProxiesForAutoConfigurationScript(
                SCRIPT, url, None)
        self.failUnless(err is None)
        self.failUnlessIsInstance(v, CFArrayRef)
        x = v[0]
        self.failUnlessEqual(x[kCFProxyTypeKey], kCFProxyTypeHTTP)
        self.failUnlessEqual(x[kCFProxyHostNameKey], "proxy.apple.com")
        self.failUnlessEqual(x[kCFProxyPortNumberKey], 8080)

        self.failUnlessResultIsCFRetained(CFNetworkCopySystemProxySettings)
        v = CFNetworkCopySystemProxySettings()
        self.failUnlessIsInstance(v, CFDictionaryRef)


    @min_os_level('10.5')
    def testUnsupported(self):
        self.fail("CFNetworkExecuteProxyAutoConfigurationScript") # Manual wrapper needed
        self.fail("CFNetworkExecuteProxyAutoConfigurationURL") # Manual wrapper needed
        

    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(kCFProxyTypeKey, unicode)
        self.failUnlessIsInstance(kCFProxyHostNameKey, unicode)
        self.failUnlessIsInstance(kCFProxyPortNumberKey, unicode)
        self.failUnlessIsInstance(kCFProxyAutoConfigurationURLKey, unicode)
        self.failUnlessIsInstance(kCFProxyUsernameKey, unicode)
        self.failUnlessIsInstance(kCFProxyPasswordKey, unicode)
        self.failUnlessIsInstance(kCFProxyTypeNone, unicode)
        self.failUnlessIsInstance(kCFProxyTypeHTTP, unicode)
        self.failUnlessIsInstance(kCFProxyTypeHTTPS, unicode)
        self.failUnlessIsInstance(kCFProxyTypeSOCKS, unicode)
        self.failUnlessIsInstance(kCFProxyTypeFTP, unicode)
        self.failUnlessIsInstance(kCFProxyTypeAutoConfigurationURL, unicode)
        self.failUnlessIsInstance(kCFNetworkProxiesHTTPEnable, unicode)
        self.failUnlessIsInstance(kCFNetworkProxiesHTTPPort, unicode)
        self.failUnlessIsInstance(kCFNetworkProxiesHTTPProxy, unicode)
        self.failUnlessIsInstance(kCFNetworkProxiesProxyAutoConfigEnable, unicode)
        self.failUnlessIsInstance(kCFNetworkProxiesProxyAutoConfigURLString, unicode)


if __name__ == "__main__":
    main()
